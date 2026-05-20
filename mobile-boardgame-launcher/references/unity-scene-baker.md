# Unity SceneBaker Automation Pack

Use this reference when Unity is selected and the project would otherwise require manual Unity Editor clicks for Build Settings, Player Settings, scene creation, GameObject placement, Inspector reference wiring, sprites, skins, balancing assets, or Android build setup.

## Purpose

SceneBaker is a Unity Editor automation layer that turns fragile manual Editor work into a repeatable one-click menu action. It should create or repair scenes, project settings, ScriptableObject assets, placeholder sprites, prefab references, and build configuration so a beginner does not need to manually wire Inspector references.

## When to Use SceneBaker

Use SceneBaker when any of these are true:

- The user wants one-click Unity setup.
- The project needs Build Settings or Player Settings configured.
- The project needs `Main.unity` or `Game.unity` generated.
- The project needs GameObjects placed and connected in the Inspector.
- The project needs placeholder circle sprites, token skins, balancing assets, or ScriptableObjects created.
- Windsurf or another coding agent can generate C# but cannot reliably perform Unity Editor clicks.

Do not use SceneBaker for non-Unity engines. If the engine is undecided, run the Engine Decision Pack first.

## Required Menu

Create one Unity Editor menu item:

```text
Tools/Mobile Boardgame/Bake Project
```

Optional secondary menus:

```text
Tools/Mobile Boardgame/Bake Build Settings Only
Tools/Mobile Boardgame/Bake Main Scene Only
Tools/Mobile Boardgame/Bake Game Scene Only
Tools/Mobile Boardgame/Bake Data Assets Only
Tools/Mobile Boardgame/Validate Bake
```

The primary menu must be safe to run repeatedly. Re-running it should update or repair the setup without duplicating objects.

## Required Editor Files

```text
Assets/Editor/SceneBaker/MobileBoardgameSceneBaker.cs
Assets/Editor/SceneBaker/BuildSettingsBaker.cs
Assets/Editor/SceneBaker/PlayerSettingsBaker.cs
Assets/Editor/SceneBaker/DataAssetBaker.cs
Assets/Editor/SceneBaker/SpriteBaker.cs
Assets/Editor/SceneBaker/MainSceneBaker.cs
Assets/Editor/SceneBaker/GameSceneBaker.cs
Assets/Editor/SceneBaker/BakeValidator.cs
```

Keep runtime code outside `Assets/Editor`. Editor scripts must not be included in Android builds.

## Required Runtime/Data Folders

```text
Assets/Scenes/Main.unity
Assets/Scenes/Game.unity
Assets/ScriptableObjects/Balancing/GameBalance.asset
Assets/ScriptableObjects/Skins/SkinCatalog.asset
Assets/Sprites/Generated/CircleWhite.png
Assets/Sprites/Generated/CircleToken_*.png
Assets/Prefabs/Generated/
Docs/SCENE_BAKER_RUNBOOK.md
Docs/SCENE_BAKER_PROOF.md
```

## One-Click Bake Scope

The single bake command must configure all of the following when Unity is the selected engine:

### Build Settings

- Add `Assets/Scenes/Main.unity` and `Assets/Scenes/Game.unity` to Editor Build Settings.
- Ensure `Main.unity` is the first scene.
- Set Android as the target build group when appropriate, but do not silently overwrite a user-selected non-Android platform unless the task is specifically Android/Google Play.
- Record the configured scenes in `Docs/SCENE_BAKER_PROOF.md`.

### Player Settings

Configure safe MVP defaults:

- Company name placeholder or user-provided studio name.
- Product name from the selected game concept.
- Package name format: `com.<studio>.<gamename>`.
- Portrait orientation.
- Android minimum/target SDK defaults appropriate to the installed Unity version.
- Version name and version code placeholders.
- No unnecessary permissions.
- Do not write keystore passwords, API keys, ad IDs, or secrets into source files.

### Skins

Create a simple `SkinCatalog.asset` ScriptableObject with 5-10 token skins:

- Default token
- Forest token
- River token
- Sun token
- Moon token
- Gem token

Each skin should reference generated circle sprite placeholders until final art exists.

### Balancing Assets

Create `GameBalance.asset` with editable MVP values:

- Board tile count: 32
- Dice min/max: 1/6
- Coin tile reward: 10
- Bonus tile reward: 25
- Trap penalty: 10
- Finish reward: 50
- Starting coins: 0
- Skin prices: 100-300
- Rewarded ad placeholder reward: 40

Balance values must be editable in the Inspector and consumed by runtime systems instead of hardcoded whenever possible.

### Circle Sprites

Generate or import simple placeholder circle sprites for tokens and UI markers:

- White base circle
- 5-10 colored token circles
- Ensure import settings work for 2D sprites.
- Record that these are placeholders in the license inventory as self-generated placeholders.

### `Main.unity` Full Composition

Create or repair `Main.unity` with:

- Main Camera
- Canvas
- EventSystem
- MainMenuRoot
- Title text
- Start button
- Shop button
- Settings/Privacy button placeholder
- SceneNavigator or equivalent component
- Safe-area aware UI anchors

Wire button references automatically. No Inspector drag-and-drop should be required.

### `Game.unity` Full Composition

Create or repair `Game.unity` with:

- Main Camera
- Canvas
- EventSystem
- GameRoot
- BoardRoot
- PlayerToken
- DiceButton
- HUD coin text
- Turn/result popup placeholder
- GameManager
- BoardManager
- DiceController
- EventResolver
- EconomyManager
- References wired through serialized fields or runtime discovery with validation

Create a 25-40 tile placeholder board, default 32 tiles. Prefer deterministic grid/circle/path placement that is easy to test.

## Idempotency Rules

SceneBaker must be idempotent:

- Find existing objects by stable names before creating new ones.
- Avoid duplicate EventSystems, Cameras, Managers, Canvases, and generated assets.
- Preserve user edits when possible.
- Only overwrite generated placeholder assets when they are marked as generated.
- Log all created, updated, skipped, and failed items.

## Validation Requirements

After baking, run `Validate Bake` or equivalent checks:

- Build Settings include Main and Game scenes.
- Main scene can navigate to Game scene.
- Game scene has required managers.
- Required serialized references are non-null.
- SkinCatalog exists and has at least 5 skins.
- GameBalance exists and contains valid non-negative values.
- Circle sprites exist and import as sprites.
- No duplicate EventSystem or Main Camera in a scene unless intentional.
- `Docs/SCENE_BAKER_PROOF.md` is updated with timestamp, Unity version, scene list, created assets, validation result, and known issues.

## SceneBaker Implementation Prompt

Use this prompt for Windsurf or another coding agent:

```text
너는 Unity Editor 자동화 전문 개발자다.
프로젝트는 Google Play 출시용 모바일 보드게임 MVP다.
목표는 수동 Unity Editor 클릭 작업을 Tools/Mobile Boardgame/Bake Project 메뉴 한 번으로 자동화하는 SceneBaker를 구현하는 것이다.

반드시 구현할 것:
1. Build Settings 자동 구성
2. Player Settings 자동 구성
3. SkinCatalog ScriptableObject 생성
4. GameBalance ScriptableObject 생성
5. Circle placeholder sprite 생성 및 Sprite import setting 적용
6. Main.unity 전체 구성
7. Game.unity 전체 구성
8. GameObject/Component/Inspector 참조 자동 연결
9. BakeValidator 검증 메뉴
10. Docs/SCENE_BAKER_PROOF.md 증거 로그 생성

수정 가능 파일:
- Assets/Editor/SceneBaker/*
- Assets/Scripts/Data/*
- Assets/Scripts/Core/* 중 필요한 public/serialized field 보강
- Assets/Scenes/Main.unity
- Assets/Scenes/Game.unity
- Assets/ScriptableObjects/*
- Assets/Sprites/Generated/*
- Docs/SCENE_BAKER_RUNBOOK.md
- Docs/SCENE_BAKER_PROOF.md

수정 금지:
- 외부 SDK 추가 금지
- 광고 SDK 추가 금지
- keystore, API key, password, token 커밋 금지
- 기존 수동 제작 아트 덮어쓰기 금지

제약:
- Bake Project 메뉴는 여러 번 실행해도 중복 오브젝트를 만들면 안 된다.
- 생성/수정/스킵/실패 항목을 콘솔과 proof 문서에 남겨라.
- Main.unity와 Game.unity는 Play 버튼으로 최소 씬 흐름이 확인되어야 한다.
- Inspector 참조는 자동 연결되어야 하며 수동 drag-and-drop이 필요하면 실패로 간주한다.

완료 기준:
1. Tools/Mobile Boardgame/Bake Project 메뉴가 존재한다.
2. Build Settings에 Main.unity와 Game.unity가 순서대로 등록된다.
3. Player Settings가 Android portrait MVP 기본값으로 설정된다.
4. SkinCatalog.asset과 GameBalance.asset이 생성된다.
5. Circle placeholder sprites가 생성되고 Sprite로 import된다.
6. Main.unity와 Game.unity가 완성된다.
7. Validate Bake가 Pass를 반환한다.
8. Docs/SCENE_BAKER_PROOF.md가 생성/업데이트된다.

증거물:
- 변경 파일 목록
- Unity Console 오류/경고
- Bake 실행 로그
- Validate Bake 결과
- 생성된 씬/에셋 목록
- SCENE_BAKER_PROOF.md 내용
```

## Commit Sequence

Use these commits for SceneBaker work:

```text
docs: add scenebaker automation runbook
chore: add unity editor scenebaker scaffold
feat: automate build and player settings bake
feat: generate skin catalog and balancing assets
feat: generate circle placeholder sprites
feat: bake main and game scenes with wired references
test: add scenebaker validation and proof logging
fix: make scenebaker idempotent and safe to rerun
```

## Proof Standard

Never claim SceneBaker is complete until there is evidence for:

- One-click menu exists.
- Running the menu produces or repairs all expected assets.
- Unity Console has no compile errors.
- Bake validation passes.
- Manual Inspector wiring is not required.
- Re-running the bake does not duplicate objects.
