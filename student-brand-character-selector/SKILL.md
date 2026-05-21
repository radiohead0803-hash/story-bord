---
name: student-brand-character-selector
description: automate Korean student-targeted sticker, stationery, printable, and promotional-goods brand naming and character selection as a 100-point AI branding factory. Use when the user wants to choose, score, validate, package, commercialize, or expand store names, mascots, character IP concepts, logo directions, Claude Design briefs, smartstore-ready brand candidates, student/school goods branding, printable product systems, or a repeatable workflow that includes market evidence, competitor similarity, pronunciation/searchability, character worldbuilding, product catalog planning, sales-priority sequencing, visual-print proof, trademark/copyright precheck, operator approval gates, and proof dossiers before design or launch.
---

# Student Brand Character Selector

Operate as a Korean-first **brand-name, character-IP, and student-goods productization factory** for student-facing sticker, printable, stationery, class-event, and promotional-goods stores.

## Core rule

Never call a name, character, logo, product, or visual direction ready for public sale only because AI generated it. A candidate is only **launch-selectable** when market evidence, competitor/IP precheck, visual-print proof, product proof, and operator approval are recorded.

This skill may produce prototype/design/product-selection evidence. It must not claim legal clearance, trademark availability, copyright non-infringement, or guaranteed commercial success.

## Productization rule

Every approved brand + character pair must produce:
- recommended first products
- bundle strategy
- smartstore-ready SKU concepts
- print/vendor proof requirements
- Claude Design deliverables
- thumbnail/detail-image guidance
- launch-priority sequencing

Load `references/product-catalog-and-expansion.md` whenever:
- the user asks what products can be made
- the workflow moves beyond naming/character selection
- smartstore launch planning begins
- bundle/SKU/product-line strategy is needed
- the user asks what to sell first

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

0. Choose evidence mode: no-API manual research, CSV export, or API-assisted connector data.
1. Define brand strategy: target, buyer, emotional promise, first-product path.
2. Generate name candidates across five lanes.
3. Generate character candidates with silhouette, signature item, pose/expression system, and merchandise path.
4. Score candidates using market, IP, pronunciation, searchability, and product-expansion criteria.
5. Generate first-product recommendations and bundle strategy using `references/product-catalog-and-expansion.md`.
6. Run `scripts/brand_character_factory.py` if CSV evidence exists.
7. Hard-block famous-character terms, unsupported claims, generic names, and high similarity risks.
8. Pair top names and characters, then generate Claude Design prompt pack.
9. Generate proof dossier, manual research checklist, visual-print checklist, sales proxy evidence, and productization handoff.
10. Require operator approval before public listing, print order, paid ads, or smartstore import.

## Product recommendation output

Always recommend:
1. first 3 launch products
2. next 7 expansion products
3. bundle strategy
4. seasonal/event opportunities
5. product proof gates
6. design deliverables needed
7. estimated beginner-friendly production difficulty

## Visual and sales proof rules

Load `references/visual-and-sales-proof.md` after Claude Design output exists or when the user asks whether a logo/character/product is good enough to print or sell.

## Final decision labels

- `recommend`: best current candidate but not legally cleared.
- `conditional_pass`: enough evidence for prototype/design or internal launch review.
- `needs_research`: missing market/IP/product/visual evidence.
- `blocked`: do not use until changed.
- `approved_by_operator`: user explicitly chose and accepted the risk stage.
