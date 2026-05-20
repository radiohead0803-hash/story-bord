# Unity Game-Type Automation Profiles

Use this reference when the user asks for Unity automation that must adapt to the game type. The goal is to avoid one rigid SceneBaker or test plan. First classify the game, then choose a Unity operating profile, SceneBaker recipe, test harness, agent split, and proof requirements.

## Classification Gate

Before generating Unity tasks, identify:

1. Game type: dice path board, card movement board, tile puzzle board, mini mission board, idle/merge board, quiz/trivia board, or hybrid.
2. Core input: tap only, drag, swipe, card select, dice roll, timed reaction, or mixed.
3. Camera/layout: portrait fixed board, scrollable map, zoomable board, grid puzzle, or mini-game scene.
4. Runtime data: ScriptableObjects only, local JSON, remote config, or backend API.
5. MVP risk: low, medium, high based on art volume, scene count, rules complexity, and testability.

## Operating Profiles

| Profile | Best for | Unity setup | SceneBaker focus | Harness focus |
|---|---|---|---|---|
| Dice Path Board | simple roll-and-move boards | 2D URP or built-in, portrait, fixed camera | Main/Game scenes, board tiles, token, dice button, HUD | deterministic dice, movement clamp, tile event tests |
| Card Movement Board | tactical path games | 2D portrait, hand/card UI area | card hand, board path, discard/selection UI | deterministic card deck, turn resolution, card effect tests |
| Tile Puzzle Board | match/connect/flip puzzle boards | grid layout, puzzle board root, optional timer | grid generator, selectable tiles, result UI | deterministic board seed, move validation, fail/win conditions |
| Mini Mission Board | board plus small challenges | GameScene plus MissionScene templates | mission loader, timed UI, return-to-board flow | scene transition, timer, mission pass/fail, pause/resume |
| Idle/Merge Board | slower progression boards | persistent board, save-heavy UI | resource panels, merge cells, shop/upgrades | economy, save/load, offline reward validation |
| Quiz/Trivia Board | question-based board games | text-heavy UI, localization-ready | question panel, answer buttons, result feedback | answer validation, localization, content safety checks |
| Hybrid | multiple mechanics | smallest viable subset only | bake only core loop scenes first | test each mechanic independently before combining |

## SceneBaker Recipe by Profile

- Dice Path Board: bake `Main.unity`, `Game.unity`, `BoardRoot`, 25-40 path tiles, `PlayerToken`, `DiceController`, `EventResolver`, HUD, `SkinCatalog`, `GameBalance`, and deterministic dice provider.
- Card Movement Board: bake `Main.unity`, `Game.unity`, `BoardRoot`, `CardHandPanel`, `DeckConfig`, `DiscardPile`, `CardEffectResolver`, and deterministic deck provider.
- Tile Puzzle Board: bake `Main.unity`, `Game.unity`, `PuzzleGridRoot`, `GridConfig`, selectable cell prefab, result popup, and deterministic board seed config.
- Mini Mission Board: bake `Main.unity`, `Game.unity`, `MissionScene.unity`, `MissionLoader`, mission result bridge, timer HUD, and return-to-board state.
- Idle/Merge Board: bake `Main.unity`, `Game.unity`, `BoardStateRoot`, resource counters, upgrade shop, merge cells, save debugger, and offline reward simulator.
- Quiz/Trivia Board: bake `Main.unity`, `Game.unity`, `QuestionPanel`, `AnswerButton` prefabs, `QuestionBank`, localization stub, and content proof document.

SceneBaker must be idempotent: rerunning the menu should update or recreate generated assets without duplicating GameObjects, corrupting manual files, or losing proof logs.

## Parallel Development and Proof Agents

Always separate builder agents from verification agents. Builders may implement features; proof agents must independently check evidence.

| Lane | Agent | Owns | Must not own | Required proof |
|---|---|---|---|---|
| Orchestration | Unity Lifecycle Orchestrator | roadmap, issue map, file ownership | feature code details | dependency map and milestone gates |
| Setup | Unity Environment Agent | Unity version, Android modules, build settings plan | game rules | environment proof checklist |
| Baking | SceneBaker Agent | Editor scripts, generated scenes/assets | core runtime rules except wiring hooks | bake log, generated object list, validation result |
| Runtime | Feature Developer Agents | gameplay scripts per feature | proof report decisions | compile result, play-mode test result |
| Data | Balance/Data Agent | ScriptableObjects, balancing, save keys | scene layout | config diff and migration notes |
| QA | QA Harness Agent | test scenes, deterministic runners | production feature ownership | pass/fail logs and bug reports |
| Proof | Verification/Proof Agent | proof report, launch blockers, evidence audit | implementation edits | Pass/Conditional Pass/Fail decision |
| Release | Release Manager Agent | versioning, AAB, release notes, Play checklist | gameplay changes | build artifact list and release proof |

## Cross-Verification Rule

A stage cannot be marked complete unless:

1. The builder agent lists changed files.
2. Unity compile result is captured.
3. Relevant automated or deterministic harness passes, or failed tests are logged as issues.
4. Proof agent reviews the evidence and gives Pass, Conditional Pass, or Fail.
5. The next stage receives only Pass or approved Conditional Pass.

## Game-Type Specific Proof Matrix

| Profile | Must-have proof |
|---|---|
| Dice Path Board | deterministic dice route, all tile event results, finish condition, economy floor |
| Card Movement Board | deterministic deck order, card effect resolution, invalid move handling |
| Tile Puzzle Board | seeded grid reproduction, valid/invalid move tests, win/fail detection |
| Mini Mission Board | mission load/return, timer, pause/resume, board state restore |
| Idle/Merge Board | save/load, offline reward math, merge validation, economy inflation check |
| Quiz/Trivia Board | answer correctness, content file validation, localization display, no unsafe claims |
| Hybrid | proof matrix for each included mechanic plus integration smoke test |

## Documents to Generate

- `Docs/GAME_TYPE_PROFILE.md`
- `Docs/UNITY_AUTOMATION_PROFILE.md`
- `Docs/SCENEBAKER_RECIPE.md`
- `Docs/AGENT_OWNERSHIP_MATRIX.md`
- `Docs/VERIFICATION_PROOF_MATRIX.md`
- `Docs/STAGE_GATE_REPORT.md`

## Windsurf Prompt: Game-Type Automation Profiler

```text
너는 Unity Game-Type Automation Profiler Agent다.
목표는 게임 아이디어를 분석해 Unity 운영 프로파일, SceneBaker 레시피, 테스트 하네스, 병렬 에이전트 구성을 결정하는 것이다.

입력:
- 게임 아이디어:
- 목표 플랫폼:
- 예상 조작 방식:
- MVP 범위:

해야 할 일:
1. 게임 타입을 Dice Path, Card Movement, Tile Puzzle, Mini Mission, Idle/Merge, Quiz/Trivia, Hybrid 중 하나로 분류하라.
2. 카메라/씬/입력/UI/데이터 구조를 결정하라.
3. 해당 타입에 맞는 SceneBaker 레시피를 작성하라.
4. 개발 에이전트와 검증/증명 에이전트를 분리해 소유 파일과 금지 파일을 지정하라.
5. 게임 타입별 필수 증거와 stage gate를 정의하라.

산출물:
- GAME_TYPE_PROFILE.md
- UNITY_AUTOMATION_PROFILE.md
- SCENEBAKER_RECIPE.md
- AGENT_OWNERSHIP_MATRIX.md
- VERIFICATION_PROOF_MATRIX.md
```
