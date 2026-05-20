# Unity Operations and New Development Automation

Use this reference when the user is unsure whether to use Unity, asks about Unity operations, or wants new Unity game development automation. Keep Unity optional until the engine decision gate passes.

## Engine Decision Gate

Before committing to Unity, compare Unity, Godot, Flutter, and React Native for the current game concept.

Recommend Unity when:
- The game is 2D/3D with animation, physics, board movement, effects, ads, IAP, or Google Play release needs.
- The user wants broad mobile game tutorials, asset store support, or many SDK integrations.
- The project may later need rewarded ads, IAP, analytics, localization, Android AAB, or console-like game loops.

Recommend Godot when:
- The game is simple 2D, the user wants a lighter open-source engine, and third-party mobile monetization SDK needs are minimal.

Recommend Flutter or React Native when:
- The product is mostly app UI, quiz/card content, dashboards, or collection screens with very light game mechanics.

Output an Engine Decision Matrix with: engine, fit, risk, reason, MVP impact, and final recommendation.

## Unity Operations Pack

When Unity is selected, generate a Unity operations plan before coding.

Required decisions:
- Unity version: use an LTS version unless the user has a specific installed version.
- Template: 2D Core for lightweight board games.
- Target platform: Android first, Google Play AAB.
- Orientation: portrait by default.
- Versioning: semantic version plus Android version code.
- Project folders: keep runtime, editor, tests, docs, and assets separate.
- Package policy: avoid unnecessary packages; record every package in the SDK/privacy register.
- Asset policy: placeholders first; licensed assets only after license inventory is ready.

## Recommended Unity Project Structure

```text
Assets/
  Art/
    Placeholder/
    UI/
    Tokens/
  Audio/
  Prefabs/
    Board/
    UI/
    Tests/
  Scenes/
    BootScene.unity
    MainMenuScene.unity
    GameScene.unity
    ResultScene.unity
    ShopScene.unity
    TestHarnessScene.unity
  Scripts/
    Core/
    Board/
    Economy/
    Save/
    UI/
    Config/
    Tests/
  ScriptableObjects/
    TileConfig.asset
    RewardConfig.asset
    SkinConfig.asset
  Settings/
Docs/
  UNITY_OPERATIONS.md
  UNITY_PROJECT_SETUP.md
  UNITY_BUILD_RUNBOOK.md
  PROOF_LOG.md
  LICENSE_INVENTORY.md
ProjectSettings/
Packages/
```

## Unity New Development Automation Workflow

1. Create or confirm the GitHub repo.
2. Add Unity `.gitignore` and repo docs before large Unity files.
3. Create the Unity project locally using the chosen LTS version.
4. Commit only stable setup files first.
5. Add scenes and placeholder UI.
6. Add core gameplay scripts in small vertical slices.
7. Add test harness scripts alongside gameplay scripts.
8. Run editor/play-mode checks before each commit.
9. Build Android only after scene flow and save/load pass.
10. Record proof in `Docs/PROOF_LOG.md` before PR/release decisions.

## Unity Version and Package Policy

- Prefer one Unity LTS version per project and document it in `Docs/UNITY_OPERATIONS.md`.
- Do not upgrade Unity mid-MVP unless there is a blocking bug or SDK requirement.
- Do not add packages without a reason, owner, version, license, and privacy impact.
- Keep Ads, Analytics, IAP, Firebase, Addressables, and localization packages optional until needed.
- When adding SDKs, update `Docs/SDK_PRIVACY_REGISTER.md` and Google Play Data Safety notes.

## Unity Git and Commit Rules

Recommended initial commits:

```text
docs: add unity engine decision and operations plan
chore: add unity gitignore and project documentation
chore: create unity 2d project scaffold
feat: add scene flow skeleton
feat: add board and deterministic dice foundation
test: add unity test harness scene and runners
feat: add tile events and economy system
feat: add save load and shop foundation
chore: prepare android build settings
release: prepare internal test build
```

Do not commit:
- Unity `Library/`, `Temp/`, `Obj/`, `Build/`, `Builds/`, `Logs/`, or local user settings.
- Android keystore files unless the user explicitly requires an encrypted enterprise storage process.
- Secrets, API keys, ad unit secrets, service account JSON, or Railway/Firebase credentials.

## Unity Build Runbook

For every Android build candidate, require:
- Unity version and commit SHA.
- Android target and minimum API level.
- Package name.
- Version code and version name.
- AAB generated path.
- Device/emulator test result.
- Five complete gameplay sessions.
- Save/load check.
- Pause/resume check.
- Offline mode check.
- Console errors/warnings summary.
- Proof log update.

## Unity Automation Agent Prompt

```text
너는 Unity Operations and New Development Agent다.
목표는 모바일 보드게임 프로젝트에서 Unity 사용 여부를 먼저 판단하고, Unity가 적합할 때만 Unity 프로젝트 운영/신규 개발 자동화를 설계하는 것이다.

해야 할 일:
1. Unity, Godot, Flutter, React Native를 비교해 엔진 선택표를 만든다.
2. Unity가 선택되면 Unity LTS 버전, Android 빌드 목표, 폴더 구조, 패키지 정책, Git 규칙을 정한다.
3. 신규 Unity 프로젝트 scaffold, 씬 구성, 스크립트 구조, 테스트 하네스, Android 빌드 runbook을 만든다.
4. GitHub 신규 repo/branch/commit 흐름과 연결한다.
5. SDK/Privacy/Register 및 License Inventory 갱신 항목을 정의한다.

제약:
- Unity를 기본 확정하지 말고 엔진 선택 게이트를 먼저 통과시킨다.
- MVP에서는 불필요한 SDK와 패키지를 추가하지 않는다.
- generated code만 보고 완료 판정하지 말고 proof log와 테스트 증거를 요구한다.
- secrets, keystore, ad unit, API key를 커밋하지 않는다.

산출물:
- Engine Decision Matrix
- Unity Operations Plan
- Unity Project Structure
- Git commit sequence
- Test harness checkpoints
- Android build runbook
- Windsurf implementation prompts
```

## Unity Proof Requirements

Before saying Unity work is complete, require proof:
- Screenshot or log of Unity Console with no compile errors.
- Scene flow test result.
- Deterministic dice/movement test result.
- Save/load result.
- Android build result or a documented reason if not yet ready.
- Updated `Docs/PROOF_LOG.md`.
