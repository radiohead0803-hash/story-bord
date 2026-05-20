# Unity Full Lifecycle AI Automation

Use this reference when Unity is selected and the user wants AI automation for setup, development, operation, build, release, and post-launch maintenance.

## Purpose

Turn Unity from a manually operated editor workflow into a repeatable AI-agent-managed production pipeline. Prefer scripts, Editor menu commands, SceneBaker actions, CI checks, proof logs, and GitHub commits over manual clicking.

## Lifecycle Stages

| Stage | Goal | Required output |
|---|---|---|
| Engine Decision | Confirm Unity is appropriate | Engine decision note and risks |
| Environment Setup | Define Unity and Android requirements | `Docs/UNITY_ENVIRONMENT.md` |
| Repo Setup | Create/verify repo operations | branches, labels, PR/issue templates |
| Project Scaffold | Generate baseline Unity structure | folders, scenes, docs, test placeholders |
| SceneBaker | Remove manual Editor clicking | one-click bake and validation menu |
| Gameplay Slices | Add small verified features | feature branch, tests, proof log |
| Test Harness | Prevent regressions | deterministic runners and smoke checks |
| Build Pipeline | Produce Android build evidence | build runbook, AAB/APK proof |
| Release Prep | Prepare Google Play assets | store checklist and compliance docs |
| Operations | Maintain and improve after launch | bug triage, hotfixes, balancing, analytics review |

## AI Agent Operating Model

Use these agents when running Unity lifecycle automation:

- Unity Lifecycle Orchestrator: owns roadmap, gates, dependencies, and file ownership.
- Unity Environment Agent: documents Unity version, modules, Android SDK/JDK/NDK, and local/CI assumptions.
- Repository Operations Agent: creates/updates GitHub repo, labels, issues, branch strategy, PR templates, and commit plan.
- Unity Scaffold Agent: creates folder layout, placeholder scripts, docs, and baseline scenes.
- SceneBaker Agent: creates `Assets/Editor/MobileBoardgameSceneBaker.cs` and one-click bake/validate menus.
- Gameplay Feature Agent: implements one vertical slice at a time.
- Test Harness Agent: owns deterministic tests, scene validation, save/load, economy, UI, and Android smoke checks.
- Build and Release Agent: owns Android build settings, versioning, AAB/APK runbook, and release evidence.
- Privacy and SDK Agent: tracks SDKs, data collection, permissions, ads, analytics, and Data Safety impact.
- Live Ops and Maintenance Agent: owns bugs, hotfixes, balancing updates, version notes, and post-launch experiments.
- Verification/Proof Agent: independently checks evidence before any phase is marked complete.

## Default Unity Project Structure

```text
Assets/
  Editor/
    MobileBoardgameSceneBaker.cs
  Scenes/
    Main.unity
    Game.unity
    Result.unity
    Shop.unity
    TestHarness.unity
  Scripts/
    Core/
    Board/
    Economy/
    Save/
    UI/
    Tests/
  Data/
    GameBalance.asset
    SkinCatalog.asset
  Art/
    Generated/
      circle_token.png
  Prefabs/
  Plugins/
Docs/
  UNITY_ENVIRONMENT.md
  UNITY_LIFECYCLE_RUNBOOK.md
  SCENE_BAKER_PROOF.md
  BUILD_PROOF.md
  RELEASE_NOTES.md
  SDK_PRIVACY_REGISTER.md
  LICENSE_INVENTORY.md
```

## One-Click Unity Automation Requirements

The SceneBaker must provide these menu actions:

```text
Tools/Mobile Boardgame/Bake Project
Tools/Mobile Boardgame/Validate Bake
Tools/Mobile Boardgame/Generate Data Assets
Tools/Mobile Boardgame/Generate Main Scene
Tools/Mobile Boardgame/Generate Game Scene
Tools/Mobile Boardgame/Apply Android Build Settings
Tools/Mobile Boardgame/Write Proof Log
```

`Bake Project` should call the lower-level steps in order and be safe to run repeatedly.

## Mandatory Automation Targets

- Build Settings scenes are registered in the correct order.
- Player Settings set company/product/package/version/orientation/platform defaults.
- Android settings are documented; signing/keystore secrets are never committed.
- `GameBalance.asset` is generated or repaired.
- `SkinCatalog.asset` is generated or repaired.
- Circle placeholder sprites are generated or imported.
- `Main.unity` is created with camera, canvas, event system, buttons, and scene navigation references.
- `Game.unity` is created with camera, canvas, game manager, board root, dice UI, HUD, player token, and data references.
- Inspector references are wired by script, not manually dragged.
- Validation detects missing scenes, null references, missing data assets, missing event system, missing canvas, missing build scenes, and bad player settings.
- Proof logs are written to `Docs/SCENE_BAKER_PROOF.md`.

## GitHub Commit Sequence

Use small, rollback-safe commits:

```text
docs: add unity lifecycle automation runbook
chore: add unity environment and repo operation docs
chore: add unity project scaffold and folder layout
feat: add scenebaker editor automation menus
feat: bake build settings and player settings
feat: bake data assets and generated sprites
feat: bake main and game scenes with references
test: add bake validation and proof logging
feat: add first gameplay vertical slice
test: add deterministic movement and economy harness
chore: prepare android build runbook
release: prepare internal test candidate
```

## Windsurf Prompt: Unity Lifecycle Orchestrator

```text
너는 Unity Lifecycle Orchestrator Agent다.
목표는 모바일 보드게임 Unity 프로젝트의 전체 라이프사이클을 AI 자동화로 운영하는 것이다.

해야 할 일:
1. Unity 사용 여부를 엔진 선택 기준으로 먼저 확인한다.
2. Unity가 선택되면 환경, GitHub repo, 프로젝트 scaffold, SceneBaker, 테스트 하네스, 빌드, 출시, 운영 단계를 게이트로 나눈다.
3. 각 게이트별 담당 에이전트, 소유 파일, 금지 파일, 산출물, 완료 증거를 정의한다.
4. 수동 Unity Editor 클릭이 필요한 작업은 SceneBaker 또는 Editor script로 대체한다.
5. 각 기능은 작은 vertical slice 단위로 구현하고, 테스트와 proof log 없이는 완료 처리하지 않는다.

산출물:
- Unity lifecycle gate table
- Agent ownership map
- GitHub branch/commit plan
- SceneBaker task list
- Test harness plan
- Build/release proof checklist
- 다음에 Windsurf에 넣을 프롬프트 5개
```

## Windsurf Prompt: SceneBaker and Operations Agent

```text
너는 Unity SceneBaker and Operations Agent다.
목표는 Unity Editor에서 수동 클릭해야 하는 설정/씬/Inspector 참조 연결을 단일 메뉴로 자동화하는 것이다.

현재 작업:
Assets/Editor/MobileBoardgameSceneBaker.cs를 만들고 다음 메뉴를 구현한다.
- Tools/Mobile Boardgame/Bake Project
- Tools/Mobile Boardgame/Validate Bake
- Tools/Mobile Boardgame/Apply Android Build Settings
- Tools/Mobile Boardgame/Write Proof Log

자동화 범위:
1. Build Settings에 Main.unity와 Game.unity를 등록한다.
2. Player Settings의 company/product/package/version/orientation/platform 기본값을 설정한다.
3. GameBalance.asset과 SkinCatalog.asset을 생성 또는 복구한다.
4. Circle placeholder sprite를 생성 또는 복구한다.
5. Main.unity와 Game.unity를 생성하고 카메라, Canvas, EventSystem, Manager, BoardRoot, HUD, 버튼을 배치한다.
6. 모든 SerializedField와 Inspector 참조를 코드로 연결한다.
7. Validate Bake에서 누락된 참조와 설정 오류를 검출한다.
8. Docs/SCENE_BAKER_PROOF.md에 실행 결과를 기록한다.

제약:
- 수동 drag-and-drop을 요구하지 말 것.
- 비밀키, keystore, API key를 생성하거나 커밋하지 말 것.
- 외부 패키지를 임의로 추가하지 말 것.
- 재실행해도 중복 오브젝트가 계속 쌓이지 않도록 idempotent하게 작성할 것.

완료 기준:
1. Bake Project 메뉴가 한 번에 실행된다.
2. Validate Bake가 pass/fail을 출력한다.
3. Build Settings와 Player Settings가 기대값으로 설정된다.
4. Main.unity와 Game.unity가 생성되고 핵심 참조가 null이 아니다.
5. Proof log가 생성된다.
6. Unity Console compile error가 없다.

증거물:
- 변경 파일 목록
- Unity Console 오류/경고 상태
- Bake 실행 로그
- Validate Bake 결과
- 생성된 scene/asset 목록
- Docs/SCENE_BAKER_PROOF.md 내용
```

## Completion Standard

Do not say Unity automation is complete unless the following are available or explicitly requested from the user:

- Unity version and target platform assumptions
- Generated or updated file list
- SceneBaker menu list
- Build Settings and Player Settings proof
- Scene validation result
- Test harness result
- GitHub commit/PR evidence
- License and SDK/privacy impact review
- Rollback note
