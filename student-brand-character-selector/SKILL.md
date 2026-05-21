---
name: student-brand-character-selector
description: automate Korean student-targeted sticker, stationery, printable, and promotional-goods brand naming and character selection as a 100-point AI branding factory. Use when the user wants to choose, score, validate, or package store names, mascots, character IP concepts, logo directions, Claude Design briefs, smartstore-ready brand candidates, school/student goods branding, or a repeatable workflow that includes market evidence, competitor similarity, pronunciation/searchability, character worldbuilding, visual-print proof, trademark/copyright precheck, operator approval gates, and proof dossiers before design or launch.
---

# Student Brand Character Selector

Operate as a Korean-first **brand-name and character-IP selection factory** for student-facing sticker, printable, stationery, class-event, and promotional-goods stores.

## Core rule

Never call a name, character, logo, or visual direction ready for public sale only because AI generated it. A candidate is only **launch-selectable** when market evidence, competitor/IP precheck, visual-print proof, and operator approval are recorded. If evidence is missing, mark the decision as `draft`, `needs_research`, `recommend`, `conditional_pass`, or `blocked`.

This skill may produce **prototype/design selection** evidence. It must not claim legal clearance, trademark availability, copyright non-infringement, or guaranteed commercial success.

## Default context

- Business: stickers, reward boards, school promotional goods, stationery-style printables, event gifts.
- Buyers: parents, elementary teachers, academies, school-event organizers.
- Users: preschool to elementary students, default 초등 1-3학년.
- Tool handoff: Claude Design, Claude Code, smartstore/listing agents, print vendors.
- Default first product: A4 칭찬스티커판 + 30구 원형 칭찬스티커.

## Required intake

Proceed with defaults if the user gives little information, but state assumptions.

| Field | Default |
|---|---|
| target user | 초등 1-3학년 학생 |
| buyer | 학부모, 초등교사 |
| category | 칭찬스티커, 판촉물, 학급 굿즈 |
| tone | 귀여움, 밝음, 신뢰감, 학교 친화 |
| avoid | 유명 캐릭터, 기존 브랜드 유사명, 과장된 교육효과 주장 |
| output count | 상호명 30개, 캐릭터 15개, 최종 조합 5개 |
| evidence | idea_only unless CSV/proof evidence exists |

## 100-point workflow

0. Choose evidence mode: no-API manual research, CSV export, or API-assisted connector data. Load `references/external-evidence-and-api-connectors.md`.
1. Define brand strategy: target, buyer, use scene, emotional promise, product expansion path.
2. Generate name candidates across five lanes: 칭찬/보상, 학교/문구, 캐릭터/세계관, 제작소/디자인랩, 프리미엄/선물.
3. Generate character candidates with silhouette, signature item, color, personality, catchphrase, expression set, pose set, and merchandise path.
4. Score name and character candidates with the 100-point rubric.
5. If CSVs are provided, run `scripts/brand_character_factory.py` to add market, competitor, and IP evidence.
6. Hard-block famous-character terms, unsupported educational/medical claims, generic names, and high similarity to protected terms.
7. Pair top names and characters, then generate Claude Design prompt pack.
8. Generate proof dossier, URL-ready manual research checklist, visual-print checklist, sales proxy evidence template, and productization handoff.
9. Require operator approval before public listing, print order, paid ads, or smartstore import.

## Evidence levels

| Level | Meaning | Allowed decision |
|---|---|---|
| `idea_only` | AI-generated only, no external evidence | draft/needs_research only |
| `manual_research` | operator will manually check KIPRIS/platform/search/social | recommend with caution |
| `csv_supported` | market/IP/competitor CSV evidence scored by script | recommend/conditional_pass possible |
| `proof_complete` | operator approval plus search/design/print evidence recorded | launch-selectable candidate possible |

## Script usage

Use the script when the user provides candidate CSVs or wants repeatable scoring.

```bash
python scripts/brand_character_factory.py \
  --candidates candidates.csv \
  --market-csv market.csv \
  --ip-csv ip.csv \
  --competitor-csv competitors.csv \
  --sales-proxy-csv sales_proxy.csv \
  --visual-audit-csv visual_audit.csv \
  --output-dir out/brand-selection
```

Accepted inputs:

- `--candidates`: required. Columns: `candidate`, optional `type`, `concept`, `lane`, `notes`.
- `--market-csv`: optional. Columns: `keyword`, `search_volume`, `competition_count`, `trend_score`, `buyer_fit`, `thumbnail_click_fit`, `price_fit`.
- `--ip-csv`: optional. Columns: `candidate`, `risk_level`, `matched_term`, `registered_name`, `source`, `notes`.
- `--competitor-csv`: optional. Columns: `brand`, `store`, `product`, `platform`, `keyword`, `price`, `review_count`, `source`.
- `--sales-proxy-csv`: optional. Columns: `keyword`, `avg_price`, `review_count_top5`, `ad_competition`, `seasonality_fit`, `giftability`, `repeat_purchase_fit`, `bundle_fit`.
- `--visual-audit-csv`: optional after Claude Design output. Columns: `pair`, `mobile_readability`, `small_sticker_readability`, `cutline_safe_area`, `monochrome_identifiability`, `ip_visual_similarity_risk`, `notes`.
- `--proof-complete`: use only when the operator has completed external proof evidence.

Outputs:

- `candidate_scores.csv`
- `top_pairs.csv`
- `claude_design_prompts.md`
- `manual_research_checklist.csv`
- `visual_print_proof_checklist.csv`
- `productization_handoff.md`
- `proof_dossier.md`
- `templates/*.csv`, including market, IP, competitor, visual audit, and sales proxy templates
- `summary.json`

If no CSV is provided, ChatGPT may score conceptually but must mark evidence as `idea_only` or `manual_research`.

## Hard stop rules

Immediately mark `blocked` if a candidate:

- Contains famous characters, celebrities, franchises, platforms, schools, or protected brands.
- Uses claims like `100%`, `무조건`, `성적향상 보장`, `집중력 치료`, `ADHD 개선`, or guaranteed outcomes.
- Closely resembles an IP/trademark/competitor term from user-provided evidence.
- Is too generic for search/discovery, such as `스티커샵`, `문구스토어`, unless modified into a distinctive brand.

## Scoring model

Use 100 points. Higher IP score means lower apparent risk.

| Name metric | Points |
|---|---:|
| 기억 용이성 | 10 |
| 발음/리듬감 | 8 |
| 검색/썸네일 식별성 | 10 |
| 초등학생 친화성 | 10 |
| 학부모/교사 신뢰감 | 10 |
| 상품 카테고리 적합성 | 10 |
| 굿즈/시리즈 확장성 | 10 |
| 캐릭터화 가능성 | 10 |
| 시장성 근거 | 12 |
| 상표/저작권 리스크 낮음 | 10 |

| Character metric | Points |
|---|---:|
| 귀여움 | 10 |
| 독창성 | 13 |
| 실루엣 식별성 | 12 |
| 인쇄 단순성 | 12 |
| 표정 확장성 | 12 |
| 굿즈 확장성 | 12 |
| 연령 적합성 | 10 |
| 감정/사용장면 | 9 |
| IP 리스크 낮음 | 10 |

See `references/scoring-rubric.md` for detailed interpretation.

## Output pattern

```markdown
# 상호명·캐릭터 선정 결과

## 1. 결론
[recommended direction and evidence level]

## 2. 브랜드 전략
[target, buyer, promise, product expansion]

## 3. 상호명 후보 점수표
| 순위 | 상호명 | Lane | 점수 | 강점 | 리스크 | 판정 |

## 4. 캐릭터 후보 점수표
| 순위 | 캐릭터 | 실루엣/아이템 | 점수 | 상품화 방향 | 리스크 | 판정 |

## 5. 최종 조합 추천
| 추천 | 상호명 + 캐릭터 | 첫 상품 | 이유 | Proof status |

## 6. Claude Design 프롬프트
[copy-paste prompt]

## 7. 검증 게이트
| Gate | 확인사항 | 통과 기준 | 현재 상태 |

## 8. 운영자 다음 행동
[manual search, approval, print proof, design brief]
```

## Claude Design prompt rules

Always include brand name, character name, target buyer/user, first product, style tokens, line thickness, shape rules, facial proportion, color contrast, sticker cutline, mobile thumbnail, negative prompts, versioning, and proof checklist. Load `references/claude-design-brief-template.md` when the user asks for logo/character 시안 or design prompts.

## IP, market, API, and sales evidence rules

Load `references/ip-market-research-checklist.md` and `references/external-evidence-and-api-connectors.md` when the user asks for a real final decision or commercialization. Generate URL-ready KIPRIS, NAVER, Coupang, Instagram/YouTube/TikTok, domain, social-handle, competitor, and sales-proxy tasks. Use API-assisted mode only if the user provides keys, exports, or connector results. Do not claim legal clearance or guaranteed demand.

## Character IP quality rules

Load `references/character-worldbuilding.md` for character packs. A strong character must have one clear silhouette, 2-3 identifiers only, a repeatable expression/pose system, a catchphrase, a use scene, and a merchandise path.

## Visual and sales proof rules

Load `references/visual-and-sales-proof.md` after Claude Design output exists or when the user asks whether a logo/character is good enough to print or sell. Require mobile thumbnail readability, 15-20 mm sticker readability, cutline safe area, monochrome recognizability, and visual IP similarity checks. Without visual audit evidence, the best decision is prototype/design selection only, not launch-selectable.

## Productization rule

After a candidate pair is selected, produce a handoff for first MVP product, listing assets, print proof, package label, thank-you card, and smartstore thumbnail. Public launch remains blocked until proof dossier and operator approval are complete.

## Final decision labels

- `recommend`: best current candidate but not legally cleared.
- `conditional_pass`: enough evidence for prototype/design, or launch-selectable internally only when proof_complete plus visual/print/operator evidence exists; never legal clearance.
- `needs_research`: good idea but missing market/IP/visual evidence.
- `blocked`: do not use until changed.
- `approved_by_operator`: user explicitly chose and accepted the risk stage.
