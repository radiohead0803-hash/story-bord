# Visual, Print, and Sales Proof

## Visual audit input
Use `visual_audit.csv` when Claude Design output exists.

Required columns:
- `pair`: brand + character pair name.
- `mobile_readability`: 0-100 score after viewing thumbnail at mobile size.
- `small_sticker_readability`: 0-100 score at 15-20 mm icon size.
- `cutline_safe_area`: 0-100 score.
- `monochrome_identifiability`: 0-100 score.
- `ip_visual_similarity_risk`: low / medium / high.
- `notes`: evidence, screenshot path, or issue summary.

Hard blockers:
- `ip_visual_similarity_risk=high`
- mobile readability below 60
- small sticker readability below 60
- cutline safe area below 60

## Sales evidence input
Use `sales_proxy.csv` to avoid guessing demand.

Required columns:
- `keyword`
- `avg_price`
- `review_count_top5`
- `ad_competition`: 0-100
- `seasonality_fit`: 0-100
- `giftability`: 0-100
- `repeat_purchase_fit`: 0-100
- `bundle_fit`: 0-100

Interpretation:
- High search volume with extremely high competition is not automatically good.
- For a first product, prefer moderate competition, strong buyer fit, and easy bundle expansion.
- Treat sales prediction as a prioritization signal, not a guarantee.
