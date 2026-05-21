# IP, Market, and Competitor Research Checklist

This is a preliminary operating workflow, not legal advice.

## Minimum manual research before public use

| Area | Search task | Evidence to save |
|---|---|---|
| Trademark | KIPRIS exact and similar search for brand and character names | screenshot/link/search date |
| Design/patent | KIPRIS design/patent keyword search if the product has unique shape, mechanism, layout, or package | screenshot/link/search date |
| Platform conflict | NAVER SmartStore and Coupang exact/similar search | top 10 result notes |
| Social conflict | Instagram, YouTube, TikTok handles and hashtags | handle/hashtag availability notes |
| Domain/handle | .com/.co.kr/.kr and social handle availability | search result notes |
| Visual similarity | compare Claude Design output against famous characters and competitors | side-by-side proof note |
| Claims | check listing text for education/medical/performance guarantees | approved wording note |

## CSV evidence schema

### market.csv
`keyword, search_volume, competition_count, trend_score, buyer_fit, thumbnail_click_fit, price_fit`

### ip.csv
`candidate, risk_level, matched_term, registered_name, source, notes`

### competitors.csv
`brand, store, product, platform, keyword, price, review_count, source`

## Blocking criteria

Block public use if:
- KIPRIS or platform search shows identical/confusingly similar brand in the same or adjacent category.
- Candidate name contains famous character/franchise/brand terms.
- Visual output resembles protected mascots or branded characters.
- Listing relies on guaranteed learning, therapy, or performance outcomes.

## Decision guidance

- No evidence: `needs_research`.
- Low-risk CSV/manual evidence: `recommend` or `conditional_pass`.
- High-risk match: `blocked`.
- Complete evidence plus operator approval: candidate may move to productization, but this still is not legal clearance.
