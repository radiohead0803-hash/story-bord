#!/usr/bin/env python3
"""100-point student brand and character selection factory.

This script does not claim legal clearance. It turns candidate names and mascot ideas
plus optional market/IP/competitor evidence CSVs into a proof-oriented decision pack.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
from urllib.parse import quote_plus
from dataclasses import dataclass, asdict
from difflib import SequenceMatcher
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple

POSITIVE_TERMS = [
    "칭찬", "스티커", "반장", "교실", "별", "문구", "도장", "체크", "습관", "상점",
    "친구", "미션", "알림장", "공부", "선물", "학급", "응원", "쑥쑥", "반짝", "하루",
]
CATEGORY_TERMS = ["스티커", "문구", "굿즈", "칭찬", "체크", "도장", "상점", "교실", "판", "쿠폰", "카드"]
CHARACTER_TERMS = ["반장", "친구", "몽", "깨비", "토끼", "햄", "별", "요정", "곰", "콩", "봇", "쌤"]
RISKY_TERMS = [
    "디즈니", "산리오", "포켓몬", "피카츄", "카카오", "라인프렌즈", "춘식", "뽀로로",
    "짱구", "도라에몽", "마블", "해리포터", "미키", "쿠로미", "시나모롤", "헬로키티",
]
CLAIM_RISK_TERMS = ["100%", "무조건", "성적향상", "성적 향상", "보장", "치료", "adhd", "집중력 개선", "완치"]
GENERIC_TERMS = ["스티커샵", "문구스토어", "문구샵", "굿즈샵", "상점", "스토어", "문구"]

NAME_WEIGHTS = {
    "memorability": 10,
    "pronunciation": 8,
    "searchability": 10,
    "student_fit": 10,
    "buyer_trust": 10,
    "category_fit": 10,
    "expansion": 10,
    "character_potential": 10,
    "market_evidence": 12,
    "ip_low_risk": 10,
}
CHAR_WEIGHTS = {
    "cuteness": 10,
    "originality": 13,
    "silhouette": 12,
    "print_simplicity": 12,
    "expression_expandability": 12,
    "merch_expandability": 12,
    "age_fit": 10,
    "emotional_scene": 9,
    "ip_low_risk": 10,
}


def clean_text(value: object) -> str:
    return re.sub(r"\s+", "", str(value or "").strip().lower())


def clamp(value: float, lo: float = 0.0, hi: float = 1.0) -> float:
    return max(lo, min(hi, value))


def contains_any(text: str, terms: Iterable[str]) -> bool:
    low = text.lower()
    return any(str(term).lower() in low for term in terms)


def count_any(text: str, terms: Iterable[str]) -> int:
    low = text.lower()
    return sum(1 for term in terms if str(term).lower() in low)


def number(value: object, default: float = 0.0) -> float:
    try:
        if value is None or value == "":
            return default
        return float(str(value).replace(",", ""))
    except ValueError:
        return default


def load_csv(path: Optional[str]) -> List[Dict[str, str]]:
    if not path:
        return []
    with Path(path).open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: List[Dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8-sig")
        return
    fields: List[str] = []
    for row in rows:
        for key in row:
            if key not in fields:
                fields.append(key)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def similarity(a: str, b: str) -> float:
    a2, b2 = clean_text(a), clean_text(b)
    if not a2 or not b2:
        return 0.0
    base = SequenceMatcher(None, a2, b2).ratio()
    containment = min(len(a2), len(b2)) / max(len(a2), len(b2)) if (a2 in b2 or b2 in a2) else 0
    return max(base, containment)


def best_similarity(candidate: str, evidence_rows: List[Dict[str, str]], columns: List[str]) -> Tuple[float, str, str]:
    best = (0.0, "", "")
    for row in evidence_rows:
        for col in columns:
            term = row.get(col, "")
            sim = similarity(candidate, term)
            if sim > best[0]:
                best = (sim, term, row.get("source", row.get("platform", "")))
    return best




def sales_proxy_index(rows: List[Dict[str, str]]) -> Dict[str, Dict[str, float]]:
    idx: Dict[str, Dict[str, float]] = {}
    for r in rows:
        keyword = clean_text(r.get("keyword") or r.get("candidate") or r.get("query"))
        if not keyword:
            continue
        avg_price = number(r.get("avg_price"), 0)
        reviews = number(r.get("review_count_top5"), 0)
        ad_comp = number(r.get("ad_competition"), 50)
        season = number(r.get("seasonality_fit"), 50)
        gift = number(r.get("giftability"), 50)
        repeat = number(r.get("repeat_purchase_fit"), 50)
        bundle = number(r.get("bundle_fit"), 50)
        price_fit = 1.0 if 4900 <= avg_price <= 12900 else 0.7 if 3000 <= avg_price <= 19900 else 0.45
        review_signal = clamp(reviews / 500.0)
        score = clamp(0.18*price_fit + 0.16*review_signal + 0.14*(1-ad_comp/100) + 0.16*(season/100) + 0.16*(gift/100) + 0.10*(repeat/100) + 0.10*(bundle/100))
        idx[keyword] = {"score": score, "avg_price": avg_price, "reviews": reviews}
    return idx


def lookup_sales(candidate: str, concept: str, sales: Dict[str, Dict[str, float]]) -> Tuple[float, str]:
    text = clean_text(candidate + " " + concept)
    matches = [(k, v["score"]) for k, v in sales.items() if k and (k in text or text in k)]
    if not matches:
        return 0.0, "no sales proxy evidence"
    k, score = max(matches, key=lambda item: item[1])
    return score, f"sales proxy matched: {k}; score={score:.2f}"


def visual_index(rows: List[Dict[str, str]]) -> Dict[str, Dict[str, object]]:
    idx: Dict[str, Dict[str, object]] = {}
    for r in rows:
        pair = clean_text(r.get("pair") or r.get("candidate") or r.get("brand"))
        if not pair:
            continue
        mobile = number(r.get("mobile_readability"), 0)
        sticker = number(r.get("small_sticker_readability"), 0)
        cutline = number(r.get("cutline_safe_area"), 0)
        mono = number(r.get("monochrome_identifiability"), 0)
        risk = str(r.get("ip_visual_similarity_risk", "")).lower().strip()
        blocked = risk == "high" or min(mobile, sticker, cutline) < 60
        score = clamp((mobile + sticker + cutline + mono) / 400.0 - (0.35 if risk == "medium" else 0) - (0.9 if risk == "high" else 0))
        idx[pair] = {"score": score, "blocked": blocked, "risk": risk, "note": r.get("notes", "")}
    return idx


def search_url(source: str, query: str) -> str:
    q = quote_plus(query)
    if source == "KIPRIS":
        return f"https://www.kipris.or.kr/khome/main.jsp?searchKeyword={q}"
    if source.startswith("NAVER") or source == "SmartStore":
        return f"https://search.shopping.naver.com/search/all?query={q}"
    if source.startswith("Coupang"):
        return f"https://www.coupang.com/np/search?q={q}"
    if source.startswith("Instagram"):
        return f"https://www.instagram.com/explore/tags/{q}/"
    if source == "YouTube":
        return f"https://www.youtube.com/results?search_query={q}"
    if source == "TikTok":
        return f"https://www.tiktok.com/search?q={q}"
    if source == "Domain":
        return f"https://www.google.com/search?q={q}+domain+availability"
    return f"https://www.google.com/search?q={q}"

def market_index(rows: List[Dict[str, str]]) -> Dict[str, Dict[str, float]]:
    if not rows:
        return {}
    volumes = [number(r.get("search_volume")) for r in rows]
    comps = [number(r.get("competition_count")) for r in rows]
    max_volume = max(volumes) or 1
    max_comp = max(comps) or 1
    idx: Dict[str, Dict[str, float]] = {}
    for r in rows:
        keyword = clean_text(r.get("keyword") or r.get("candidate") or r.get("query"))
        if not keyword:
            continue
        volume = number(r.get("search_volume"))
        comp = number(r.get("competition_count"))
        trend = number(r.get("trend_score"), 50)
        buyer_fit = number(r.get("buyer_fit"), 50)
        click_fit = number(r.get("thumbnail_click_fit"), 50)
        price_fit = number(r.get("price_fit"), 50)
        volume_score = volume / max_volume
        comp_penalty = comp / max_comp
        score = clamp(
            0.25 * volume_score
            + 0.20 * (trend / 100)
            + 0.20 * (buyer_fit / 100)
            + 0.15 * (click_fit / 100)
            + 0.10 * (price_fit / 100)
            + 0.10 * (1 - comp_penalty)
        )
        idx[keyword] = {"score": score, "volume": volume, "competition": comp}
    return idx


def lookup_market(candidate: str, concept: str, market: Dict[str, Dict[str, float]], competitors: List[Dict[str, str]], sales: Dict[str, Dict[str, float]]) -> Tuple[float, str]:
    text = clean_text(candidate + " " + concept)
    matches = [(k, v["score"]) for k, v in market.items() if k and (k in text or text in k)]
    comp_sim, comp_term, comp_src = best_similarity(candidate, competitors, ["brand", "store", "product", "keyword", "name"])
    sales_score, sales_note = lookup_sales(candidate, concept, sales)
    if matches:
        k, score = max(matches, key=lambda item: item[1])
        combined = clamp(score * 0.70 + sales_score * 0.30) if sales_score else score
        adjusted = clamp(combined - max(0, comp_sim - 0.72) * 0.8)
        return adjusted, f"market keyword matched: {k}; {sales_note}; competitor similarity {comp_sim:.2f} {comp_term} {comp_src}".strip()
    baseline = 0.30 if market or competitors else 0.18
    combined = clamp(baseline * 0.70 + sales_score * 0.30) if sales_score else baseline
    adjusted = clamp(combined - max(0, comp_sim - 0.72) * 0.8)
    return adjusted, f"no direct market keyword; {sales_note}; competitor similarity {comp_sim:.2f} {comp_term} {comp_src}".strip()


def lookup_ip(candidate: str, ip_rows: List[Dict[str, str]]) -> Tuple[float, str, str]:
    text = clean_text(candidate)
    auto = []
    if contains_any(text, RISKY_TERMS):
        auto.append("famous/protected term")
    if contains_any(text, CLAIM_RISK_TERMS):
        auto.append("unsupported education/medical claim")
    if text in [clean_text(g) for g in GENERIC_TERMS]:
        auto.append("too generic")
    explicit_row = None
    for r in ip_rows:
        if clean_text(r.get("candidate")) == text:
            explicit_row = r
            break
    level = (explicit_row or {}).get("risk_level", "").lower()
    if auto:
        return 0.0 if "famous/protected term" in auto else 0.25, "; ".join(auto), "blocked"
    if level == "high":
        return 0.0, f"high ip risk from provided CSV: {(explicit_row or {}).get('matched_term','')}", "blocked"
    if level == "medium":
        return 0.35, f"medium ip risk from provided CSV: {(explicit_row or {}).get('matched_term','')}", "needs_research"
    if level == "low":
        return 0.85, "low risk in provided IP CSV; still not legal clearance", "conditional_pass"
    sim, term, source = best_similarity(candidate, ip_rows, ["matched_term", "registered_name", "brand", "mark"])
    if sim >= 0.88:
        return 0.0, f"high ip/similarity risk: {term}; sim={sim:.2f}", "blocked"
    if sim >= 0.76:
        return 0.35, f"medium ip/similarity risk: {term}; sim={sim:.2f}; source={source}", "needs_research"
    if ip_rows:
        return 0.72, f"no strong IP match in provided CSV; best similarity {sim:.2f} {term}", "conditional_pass"
    return 0.50, "no IP evidence provided; manual KIPRIS/platform search required", "needs_research"


def rhythm_score(candidate: str) -> float:
    n = len(clean_text(candidate))
    if 3 <= n <= 6:
        return 1.0
    if 2 <= n <= 8:
        return 0.80
    if n <= 11:
        return 0.55
    return 0.35


def decision_from(total: float, ip_status: str, evidence_level: str, visual_ready: bool = False) -> str:
    if ip_status == "blocked":
        return "blocked"
    if total >= 82 and evidence_level in {"csv_supported", "proof_complete"} and visual_ready:
        return "conditional_pass"
    if total >= 72 and evidence_level in {"csv_supported", "proof_complete"}:
        return "recommend"
    if total >= 68:
        return "needs_research"
    return "revise"


def score_name(row: Dict[str, str], market: Dict[str, Dict[str, float]], ip_rows: List[Dict[str, str]], competitors: List[Dict[str, str]], sales: Dict[str, Dict[str, float]], evidence_level: str) -> Dict[str, object]:
    cand = row.get("candidate", "").strip()
    concept = " ".join([row.get("concept", ""), row.get("notes", ""), row.get("lane", "")])
    text = clean_text(cand + " " + concept)
    length = len(clean_text(cand))
    positive = count_any(text, POSITIVE_TERMS)
    category = count_any(text, CATEGORY_TERMS)
    char = count_any(text, CHARACTER_TERMS)
    ip_score, ip_note, ip_status = lookup_ip(cand, ip_rows)
    market_score, market_note = lookup_market(cand, concept, market, competitors, sales)
    generic_penalty = 0.35 if clean_text(cand) in [clean_text(g) for g in GENERIC_TERMS] else 0
    values = {
        "memorability": clamp((1.0 if 3 <= length <= 6 else 0.75 if length <= 8 else 0.45) + min(0.15, positive * 0.03)),
        "pronunciation": rhythm_score(cand),
        "searchability": clamp((0.88 if 3 <= length <= 8 else 0.55) - generic_penalty),
        "student_fit": clamp(0.42 + min(0.45, positive * 0.08) + (0.10 if contains_any(text, ["별", "친구", "반장", "토끼", "햄", "깨비", "몽"]) else 0)),
        "buyer_trust": clamp(0.62 + (0.14 if contains_any(text, ["교실", "습관", "체크", "알림장", "문구", "하루"]) else 0) - (0.45 if contains_any(text, CLAIM_RISK_TERMS) else 0)),
        "category_fit": clamp(0.40 + min(0.48, category * 0.12)),
        "expansion": clamp(0.42 + (0.25 if contains_any(text, ["상점", "랩", "교실", "반장", "친구", "하우스"]) else 0) + min(0.20, positive * 0.03)),
        "character_potential": clamp(0.32 + min(0.45, char * 0.12) + (0.14 if contains_any(text, ["몽", "깨비", "친구", "요정", "반장"]) else 0)),
        "market_evidence": market_score,
        "ip_low_risk": ip_score,
    }
    weighted = {k: round(values[k] * NAME_WEIGHTS[k], 1) for k in NAME_WEIGHTS}
    total = round(sum(weighted.values()), 1)
    return {**row, "type": row.get("type", "name"), **weighted, "total_score": total, "market_note": market_note, "ip_note": ip_note, "decision": decision_from(total, ip_status, evidence_level), "evidence_level": evidence_level}


def score_character(row: Dict[str, str], ip_rows: List[Dict[str, str]], evidence_level: str) -> Dict[str, object]:
    cand = row.get("candidate", "").strip()
    concept = " ".join([row.get("concept", ""), row.get("notes", "")])
    text = clean_text(cand + " " + concept)
    positive = count_any(text, POSITIVE_TERMS + CHARACTER_TERMS)
    ip_score, ip_note, ip_status = lookup_ip(cand, ip_rows)
    identifiers = count_any(text, ["별", "도장", "배지", "연필", "가방", "체크", "스티커"])
    simple = contains_any(text, ["단순", "둥근", "배지", "별", "두꺼운", "심플"])
    values = {
        "cuteness": clamp(0.50 + min(0.35, positive * 0.05)),
        "originality": clamp(0.72 - (0.60 if contains_any(text, RISKY_TERMS) else 0) - (0.18 if contains_any(text, ["토끼", "곰", "햄"]) and positive < 2 else 0)),
        "silhouette": clamp(0.50 + min(0.32, identifiers * 0.10)),
        "print_simplicity": clamp(0.55 + (0.20 if simple else 0) - (0.18 if contains_any(text, ["복잡", "화려", "세밀"]) else 0)),
        "expression_expandability": clamp(0.55 + (0.25 if contains_any(text, ["반장", "친구", "몽", "깨비", "요정", "봇"]) else 0)),
        "merch_expandability": clamp(0.55 + (0.24 if contains_any(text, ["상점", "반장", "도장", "별", "스티커", "배지"]) else 0)),
        "age_fit": clamp(0.60 + (0.20 if contains_any(text, ["초등", "교실", "칭찬", "친구", "미션"]) else 0)),
        "emotional_scene": clamp(0.52 + (0.26 if contains_any(text, ["칭찬", "응원", "체크", "습관", "미션", "실수"]) else 0)),
        "ip_low_risk": ip_score,
    }
    weighted = {k: round(values[k] * CHAR_WEIGHTS[k], 1) for k in CHAR_WEIGHTS}
    total = round(sum(weighted.values()), 1)
    return {**row, "type": row.get("type", "character"), **weighted, "total_score": total, "ip_note": ip_note, "decision": decision_from(total, ip_status, evidence_level), "evidence_level": evidence_level}


def create_pair_rows(name_rows: List[Dict[str, object]], char_rows: List[Dict[str, object]], evidence_level: str, visual: Dict[str, Dict[str, object]]) -> List[Dict[str, object]]:
    names = [r for r in name_rows if r.get("decision") != "blocked"][:8]
    chars = [r for r in char_rows if r.get("decision") != "blocked"][:8]
    rows: List[Dict[str, object]] = []
    for n in names:
        for c in chars:
            score = round(float(n["total_score"]) * 0.55 + float(c["total_score"]) * 0.45, 1)
            pair_key = clean_text(str(n.get("candidate", "")) + " + " + str(c.get("candidate", "")))
            visual_row = visual.get(pair_key) or visual.get(clean_text(str(n.get("candidate", "")) + str(c.get("candidate", ""))))
            visual_score = float(visual_row.get("score", 0)) if visual_row else 0.0
            visual_blocked = bool(visual_row.get("blocked", False)) if visual_row else False
            if visual:
                score = round(score + (4.0 * visual_score if visual_row else -3.0), 1)
            if visual_blocked:
                status = "blocked"
            elif score >= 80 and evidence_level == "proof_complete" and visual_score >= 0.75:
                status = "conditional_pass"
            elif score >= 80 and evidence_level != "idea_only":
                status = "recommend"
            elif score >= 72:
                status = "needs_research"
            else:
                status = "revise"
            if status != "blocked" and (n.get("decision") == "needs_research" or c.get("decision") == "needs_research"):
                status = "needs_research"
            rows.append({
                "brand": n.get("candidate", ""),
                "character": c.get("candidate", ""),
                "pair_score": score,
                "first_product": "A4 칭찬스티커판 + 30구 원형 칭찬스티커",
                "series_extension": "네임스티커, 학급쿠폰, 미션카드, 선생님용 칭찬라벨, 시즌 행사 굿즈",
                "proof_status": status,
                "market_note": n.get("market_note", ""),
                "risk_note": f"name: {n.get('ip_note','')}; character: {c.get('ip_note','')}",
                "visual_score": visual_score,
                "visual_note": (visual_row or {}).get("note", "visual audit missing"),
            })
    return sorted(rows, key=lambda r: float(r["pair_score"]), reverse=True)[:15]


def prompt_for_pair(brand: str, character: str, concept: str = "") -> str:
    return f"""## {brand} + {character}\n\n```text\n학생 대상 스티커 및 판촉물 스토어를 위한 상업용 후보 시안을 제작해줘.\n\n브랜드명: {brand}\n캐릭터명: {character}\n타깃 구매자: 학부모, 초등교사, 학원/공부방 운영자\n실사용자: 초등 1-3학년 학생\n첫 상품: A4 칭찬스티커판 + 30구 원형 칭찬스티커\n확장 상품: 네임스티커, 학급쿠폰, 공부습관 체크리스트, 행사 답례 스티커\n컨셉 메모: {concept}\n\n캐릭터 IP 설정:\n- 역할: 아이의 작은 성공을 기록해주는 교실 친구\n- 성격: 밝음, 성실함, 약간 장난기, 실패해도 다시 응원\n- 실루엣: 작은 스티커에서도 식별 가능한 둥근 얼굴 + 단일 시그니처 아이템\n- 시그니처 아이템: 별 배지, 칭찬 도장, 체크 연필 중 1개만 선택\n- 표정 7종: 칭찬, 응원, 집중, 완료, 감사, 실수해도괜찮아, 미션성공\n- 포즈 6종: 정면, 손흔들기, 스티커 들기, 체크 가리키기, 점프, 집중\n\n스타일 토큰:\n- line: thick rounded outline, consistent stroke width\n- shape: simple rounded geometric shapes, no complex texture\n- color: pastel base with print-safe contrast, avoid low contrast yellow text\n- face: large eyes but not franchise-like, simple mouth, no copied mascot proportions\n- layout: mobile thumbnail readable at small size\n\n필수 산출물:\n1. 로고 3종: 워드마크형, 심볼+글자형, 캐릭터 결합형\n2. 캐릭터 정면 3종\n3. 표정 7종\n4. 포즈 6종\n5. 칭찬스티커 아이콘 10종\n6. 스마트스토어 썸네일 1종\n7. 상세페이지 첫 화면 1종\n8. 포장 스티커/감사카드 1종\n9. 흑백 단색 버전 1종\n\n인쇄 제약:\n- 3 mm bleed note, cutline safe area, no tiny text\n- sticker icon must remain readable at 15-20 mm size\n- brand name must be readable on mobile thumbnail\n- provide high-contrast and monochrome fallback\n\n금지:\n- famous character/franchise/platform/school logo/celebrity likeness\n- named artist or brand style mimicry\n- guaranteed academic, medical, psychological outcome claims\n- thin lines, tiny text, complex background, over-detailed accessories\n\n검증 요청:\n- mark any IP similarity risk\n- mark mobile thumbnail readability risk\n- mark small-sticker print risk\n- create v1/v2/v3 with clear differences\n```\n"""


def write_prompts(path: Path, pairs: List[Dict[str, object]]) -> None:
    lines = ["# Claude Design Prompt Pack", "", "Use only after IP/market research tasks are completed or accepted as preliminary.", ""]
    for p in pairs[:3]:
        lines.append(prompt_for_pair(str(p["brand"]), str(p["character"]), str(p.get("risk_note", ""))))
    path.write_text("\n".join(lines), encoding="utf-8")


def write_research_checklist(path: Path, candidates: List[Dict[str, object]]) -> None:
    tasks = []
    for c in candidates:
        name = str(c.get("candidate", ""))
        for task, source in [
            ("exact and similar trademark search", "KIPRIS"),
            ("design-right/patent keyword search if visual/mechanism is unique", "KIPRIS"),
            ("exact product/store search", "NAVER SmartStore"),
            ("exact product/store search", "Coupang"),
            ("hashtag/account/handle search", "Instagram/YouTube/TikTok"),
            ("domain and social handle availability", "domain/social"),
            ("famous-character visual similarity review after Claude Design output", "operator proof"),
            ("mobile thumbnail readability screenshot", "design proof"),
            ("15-20 mm sticker readability and cutline proof", "print proof"),
        ]:
            tasks.append({"candidate": name, "task": task, "source": source, "search_url": search_url(source.split("/")[0], name), "status": "todo", "evidence_url_or_note": "", "result": ""})
    write_csv(path, tasks)


def write_visual_proof_template(path: Path, pairs: List[Dict[str, object]]) -> None:
    rows = []
    for p in pairs[:5]:
        label = f"{p.get('brand')} + {p.get('character')}"
        for check in [
            "logo readable at 120px width", "thumbnail readable on mobile", "15mm sticker icon readable",
            "cutline safe area clear", "monochrome version identifiable", "no famous-character similarity",
            "no copied font/logo feel", "A4 print test readable", "parent buyer trust tone acceptable",
        ]:
            rows.append({"pair": label, "check": check, "pass_fail": "", "evidence_file_or_note": "", "fix_needed": ""})
    write_csv(path, rows)


def write_productization_plan(path: Path, pairs: List[Dict[str, object]]) -> None:
    top = pairs[0] if pairs else {"brand": "", "character": ""}
    content = f"""# Productization Handoff\n\n## Selected draft direction\n- Brand: {top.get('brand','')}\n- Character: {top.get('character','')}\n- Status: {top.get('proof_status','draft')}\n\n## First MVP product\n1. A4 reward sticker board PDF\n2. 30-piece round sticker sheet\n3. usage instruction card\n4. package label and thank-you card\n5. smartstore thumbnail and detail-page first screen\n\n## Next workflow after approval\n1. Complete manual research checklist.\n2. Generate Claude Design v1/v2/v3.\n3. Fill visual proof checklist with screenshots/photos.\n4. Run print sample or vendor template proof.\n5. Create listing draft and FAQ.\n6. Operator approves before public upload.\n\n## Hard blockers\n- high IP/trademark similarity\n- weak mobile readability\n- copied mascot style\n- unsupported education/medical claims\n- no operator approval\n"""
    path.write_text(content, encoding="utf-8")


def write_dossier(path: Path, pairs: List[Dict[str, object]], evidence_level: str, counts: Dict[str, int]) -> None:
    top = pairs[0] if pairs else {}
    content = f"""# Brand Character Proof Dossier\n\n## Decision\n- Selected brand: {top.get('brand', '')}\n- Selected character: {top.get('character', '')}\n- Pair score: {top.get('pair_score', '')}\n- Decision label: {top.get('proof_status', 'draft')}\n- Evidence level: {evidence_level}\n\n## Evidence inventory\n- Name candidates scored: {counts.get('names', 0)}\n- Character candidates scored: {counts.get('characters', 0)}\n- Pair combinations scored: {counts.get('pairs', 0)}\n- Market evidence CSV: {'provided' if evidence_level in ['csv_supported', 'proof_complete'] else 'missing'}\n- IP/competitor evidence CSV: {'provided' if evidence_level in ['csv_supported', 'proof_complete'] else 'missing'}\n- Claude Design prompts: generated\n- Visual/print proof template: generated\n- Operator approval: pending\n\n## Launch decision rule\nThis dossier supports prototype/design selection only. Public sale requires completed manual research, visual proof, print proof, and operator approval. It is not legal clearance.\n\n## Required proof before public listing\n- [ ] KIPRIS exact/similar trademark search saved\n- [ ] KIPRIS design/patent keyword search saved if applicable\n- [ ] NAVER/SmartStore/Coupang conflict search saved\n- [ ] Instagram/YouTube/TikTok handle/hashtag search saved\n- [ ] Domain/social handle availability checked\n- [ ] Claude Design output reviewed for famous-character similarity\n- [ ] Mobile thumbnail readability screenshot saved\n- [ ] 15-20 mm sticker readability proof saved\n- [ ] A4 print proof saved\n- [ ] Refund/delivery/education-claim wording approved\n- [ ] Operator approval recorded\n"""
    path.write_text(content, encoding="utf-8")


def evidence_level(args: argparse.Namespace) -> str:
    if args.proof_complete:
        return "proof_complete"
    if args.market_csv or args.ip_csv or args.competitor_csv or getattr(args, "sales_proxy_csv", None) or getattr(args, "visual_audit_csv", None):
        return "csv_supported"
    return "idea_only"


def create_templates(out: Path) -> None:
    write_csv(out / "templates" / "candidates_template.csv", [
        {"candidate": "스티커반장", "type": "name", "lane": "칭찬/보상", "concept": "초등 칭찬스티커 브랜드", "notes": ""},
        {"candidate": "반장이", "type": "character", "lane": "교실친구", "concept": "별 배지를 단 반장 캐릭터", "notes": "둥근 얼굴 두꺼운 선"},
    ])
    write_csv(out / "templates" / "market_template.csv", [
        {"keyword": "칭찬스티커", "search_volume": 1000, "competition_count": 300, "trend_score": 70, "buyer_fit": 85, "thumbnail_click_fit": 80, "price_fit": 75},
    ])
    write_csv(out / "templates" / "ip_template.csv", [
        {"candidate": "예시후보", "risk_level": "low", "matched_term": "", "registered_name": "", "source": "KIPRIS", "notes": ""},
    ])
    write_csv(out / "templates" / "competitor_template.csv", [
        {"brand": "경쟁브랜드예시", "store": "", "product": "", "platform": "SmartStore", "keyword": "칭찬스티커", "price": "", "review_count": "", "source": "manual"},
    ])
    write_csv(out / "templates" / "visual_audit_template.csv", [
        {"pair": "스티커반장 + 반장이", "mobile_readability": 85, "small_sticker_readability": 82, "cutline_safe_area": 90, "monochrome_identifiability": 80, "ip_visual_similarity_risk": "low", "notes": "attach screenshot/photo path"},
    ])
    write_csv(out / "templates" / "sales_proxy_template.csv", [
        {"keyword": "칭찬스티커", "avg_price": 7900, "review_count_top5": 250, "ad_competition": 45, "seasonality_fit": 70, "giftability": 85, "repeat_purchase_fit": 60, "bundle_fit": 90},
    ])


def main() -> None:
    parser = argparse.ArgumentParser(description="Score brand and character candidates and generate proof artifacts.")
    parser.add_argument("--candidates", required=True, help="CSV with candidate,type,concept,lane,notes")
    parser.add_argument("--market-csv", default=None, help="Optional keyword market evidence CSV")
    parser.add_argument("--ip-csv", default=None, help="Optional IP/trademark evidence CSV")
    parser.add_argument("--competitor-csv", default=None, help="Optional competitor/platform evidence CSV")
    parser.add_argument("--sales-proxy-csv", default=None, help="Optional sales proxy CSV for price/review/repeat/bundle evidence")
    parser.add_argument("--visual-audit-csv", default=None, help="Optional visual audit CSV after Claude Design output")
    parser.add_argument("--proof-complete", action="store_true", help="Use only when operator has completed all proof evidence outside this script")
    parser.add_argument("--output-dir", default="brand_character_out")
    args = parser.parse_args()

    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)
    candidates = load_csv(args.candidates)
    market = market_index(load_csv(args.market_csv))
    ip_rows = load_csv(args.ip_csv)
    competitors = load_csv(args.competitor_csv)
    sales = sales_proxy_index(load_csv(args.sales_proxy_csv))
    visual = visual_index(load_csv(args.visual_audit_csv))
    level = evidence_level(args)

    names = [r for r in candidates if (r.get("type") or r.get("kind") or "name").lower() in ["name", "brand", "상호명", "브랜드"]]
    chars = [r for r in candidates if (r.get("type") or r.get("kind") or "").lower() in ["character", "캐릭터", "mascot"]]
    if not names:
        names = candidates
    if not chars:
        chars = [r for r in candidates if contains_any(r.get("candidate", "") + r.get("concept", ""), CHARACTER_TERMS)]

    name_scores = sorted([score_name(r, market, ip_rows, competitors, sales, level) for r in names], key=lambda r: float(r["total_score"]), reverse=True)
    char_scores = sorted([score_character(r, ip_rows, level) for r in chars], key=lambda r: float(r["total_score"]), reverse=True)
    pairs = create_pair_rows(name_scores, char_scores, level, visual)

    write_csv(out / "candidate_scores.csv", name_scores + char_scores)
    write_csv(out / "top_pairs.csv", pairs)
    write_prompts(out / "claude_design_prompts.md", pairs)
    write_research_checklist(out / "manual_research_checklist.csv", (name_scores + char_scores)[:12])
    write_visual_proof_template(out / "visual_print_proof_checklist.csv", pairs)
    write_productization_plan(out / "productization_handoff.md", pairs)
    create_templates(out)
    write_dossier(out / "proof_dossier.md", pairs, level, {"names": len(name_scores), "characters": len(char_scores), "pairs": len(pairs)})
    summary = {"evidence_level": level, "name_count": len(name_scores), "character_count": len(char_scores), "pair_count": len(pairs), "sales_proxy_rows": len(sales), "visual_audit_rows": len(visual), "top_pair": pairs[0] if pairs else None}
    (out / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
