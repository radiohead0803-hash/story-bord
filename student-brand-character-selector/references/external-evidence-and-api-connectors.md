# External Evidence and API Connector Plan

This skill supports two evidence modes.

## Mode A: No API keys / manual evidence mode
Use this mode by default. Generate search tasks and URL-ready queries, then require the operator to paste findings into CSV evidence files.

Required evidence before public use:
- KIPRIS trademark exact and similar search for brand and character names.
- KIPRIS design-right/patent keyword search for any unique printable, sticker mechanism, or package shape.
- NAVER SmartStore product/store search for exact and confusingly similar names.
- Coupang search for exact and confusingly similar product names.
- Instagram, YouTube, TikTok, Naver Blog, and domain/social handle availability search.
- Competitor screenshot or URL notes for the closest 5 results.

## Mode B: API-assisted mode
Use this mode only when the user has explicit API keys, connector access, or provides exported data. Do not invent live results.

Supported connector contracts:

| Source | Purpose | Input expected | Output CSV |
|---|---|---|---|
| KIPRIS or manual export | trademark/design/patent conflict checks | brand/character/query | `ip.csv` |
| NAVER DataLab/SearchAd/manual export | search volume and trend proxy | keyword | `market.csv` |
| SmartStore/Coupang/manual scrape/export | competitor count, price, reviews | keyword/product | `competitors.csv` |
| Social/search manual export | handle/hashtag conflict | brand/character | `social.csv` |
| Claude Design output audit | visual proof evidence | image notes/scores | `visual_audit.csv` |

## Evidence grading

| Evidence | Minimum for label |
|---|---|
| no external data | `draft` or `needs_research` only |
| manual checklist completed but not independently verified | `recommend` only |
| CSV evidence plus visual proof templates generated | `conditional_pass` for prototype/design |
| CSV evidence, visual proof, print proof, operator approval | `launch-selectable` internally, never legal clearance |

## Do not overclaim
Never say a name is legally available or non-infringing. Say: "no high-risk conflict was found in the provided evidence" and list remaining checks.
