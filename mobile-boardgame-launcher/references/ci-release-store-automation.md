# CI, Release Evidence, Store Asset, and SDK Automation

Use this reference to strengthen the end-to-end launch pipeline after the concept, GitHub repo, and test harness are defined.

## Recommended Add-On Packs

Add these packs when the user asks for a more automated or production-like workflow:

1. CI Build Pack
2. Release Evidence Pack
3. Store Asset Production Pack
4. SDK and Privacy Register Pack
5. Crash/Analytics Decision Pack
6. Backup and Recovery Pack
7. Localization Pack
8. Accessibility and Device Compatibility Pack

## CI Build Pack

For Unity projects, recommend GitHub Actions only after the repository exists and Unity license/activation handling is understood. If CI cannot build Unity due to licensing or runner limits, use CI for static checks, docs validation, and release checklist validation instead.

Suggested files:

```text
.github/workflows/docs-check.yml
.github/workflows/unity-build-android.yml
.github/workflows/release-evidence.yml
Docs/CI_SETUP.md
Docs/BUILD_RUNBOOK.md
```

Minimum checks:

- Required docs exist.
- License inventory is not empty.
- Proof log exists.
- No obvious secrets in committed files.
- Unity build workflow is documented even if manual build remains the primary release path.

## Release Evidence Pack

Every internal test and release candidate should produce evidence:

```text
Docs/RELEASE_EVIDENCE.md
Docs/BUILD_RUNBOOK.md
Docs/INTERNAL_TEST_REPORT.md
Docs/KNOWN_ISSUES.md
```

Evidence must include:

- version code/name
- branch and commit
- Unity version
- Android device/emulator
- AAB/APK path or artifact name
- harness results
- manual smoke test results
- unresolved launch blockers
- release decision: Pass / Conditional Pass / Fail

## Store Asset Production Pack

Prepare a store-asset brief before screenshots are generated.

Suggested files:

```text
Docs/STORE_LISTING_COPY.md
Docs/SCREENSHOT_SHOTLIST.md
Docs/APP_ICON_BRIEF.md
Docs/FEATURE_GRAPHIC_BRIEF.md
```

Rules:

- Store copy must match actual implemented features.
- Do not claim multiplayer, cash prizes, real rewards, cloud save, or live events unless implemented and policy-reviewed.
- Screenshots should show real gameplay UI or clearly marked concept art.
- App icon and feature graphic must avoid trademark-confusing characters or copyrighted styles.

## SDK and Privacy Register Pack

Add a single source of truth for every SDK/plugin.

Suggested file:

```text
Docs/SDK_AND_DATA_SAFETY_REGISTER.md
```

Required fields:

```markdown
| SDK/Plugin | Purpose | Data collected | Shared with third party? | Consent/setting | Privacy policy impact | Data Safety impact | Status |
|---|---|---|---|---|---|---|---|
```

Default MVP guidance:

- Start with no analytics SDK and no ad SDK until the core game is stable.
- If adding ads, update privacy policy, Data Safety, store declarations, QA plan, and test cases.
- If adding crash reporting, document collected diagnostics and retention assumptions.

## Crash/Analytics Decision Pack

For v1.0, prefer minimum instrumentation:

- local proof logs during development
- Google Play Console vitals after release
- optional crash reporting only if the developer can keep Data Safety accurate

Decision output:

```markdown
# Crash and Analytics Decision
- MVP choice:
- SDKs included:
- Data Safety impact:
- Privacy policy update required:
- Go/No-Go:
```

## Backup and Recovery Pack

For solo/beginner projects, prevent catastrophic loss:

- Push to GitHub daily.
- Tag release candidates.
- Export final AAB and key release documents into a backup folder.
- Keep signing key/keystore outside Git, backed up securely.
- Document who owns Play Console and signing credentials.

Suggested file:

```text
Docs/BACKUP_AND_RECOVERY.md
```

## Localization Pack

Default: Korean and English store listing, English in-game strings only if the user wants a global launch.

Suggested files:

```text
Assets/Localization/strings_ko.json
Assets/Localization/strings_en.json
Docs/LOCALIZATION_PLAN.md
```

Avoid localization in v1.0 if it delays the MVP, but prepare string keys so localization can be added later.

## Accessibility and Device Compatibility Pack

Required checks:

- Buttons large enough for touch.
- Important text readable on small screens.
- No essential information conveyed by color only.
- Safe area support for notches.
- 16:9, 19.5:9, 20:9 aspect ratio checks.
- Offline mode behavior clear.

Suggested file:

```text
Docs/DEVICE_AND_ACCESSIBILITY_CHECKLIST.md
```

## Automation Recommendation Agent Prompt

```text
너는 Mobile Game Automation Architect다.
목표는 현재 모바일 보드게임 프로젝트에 추가하면 좋은 자동화 구성을 추천하고, MVP 범위를 해치지 않는 항목만 반영하는 것이다.

검토할 항목:
1. GitHub Actions CI
2. Release Evidence 문서화
3. Store asset 제작 브리프
4. SDK/Data Safety register
5. Crash/analytics decision
6. Backup/recovery plan
7. Localization plan
8. Accessibility/device compatibility checklist
9. Railway backend 필요 여부

원칙:
- MVP를 무겁게 만들지 말 것.
- 기본 gameplay보다 출시 차단 리스크를 줄이는 자동화를 우선할 것.
- SDK, backend, analytics는 기본 제외하고 필요 조건을 충족할 때만 추가할 것.
- 모든 자동화에는 acceptance criteria와 proof artifacts를 포함할 것.

산출물:
- recommended add-ons
- add / defer / reject decision table
- files to create
- commits to make
- risks reduced
- next 3 Windsurf prompts
```
