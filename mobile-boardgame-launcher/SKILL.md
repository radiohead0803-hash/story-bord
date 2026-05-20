---
name: mobile-boardgame-launcher
description: plan, research, design, build, verify, package, and launch mobile board games for google play using ai-assisted development. use for keyword-to-launch game development, market research, mvp/big-game scope selection, license/ip review, unity/godot engine decision, unity full lifecycle automation, scenebaker, game-type profiles, project doctor, package governance, save migration, performance budgets, github repo/commit automation, railway/backend decisions, ci/release evidence, store assets, sdk/privacy review, play console launch preparation, connector/mcp governance, creative asset governance, quality upgrade loops, ai game factory operating system, factory orchestrator agents, connector/mcp security gates, parallel development/proof agents, stage-gate verification, failure recovery, and post-launch iteration.
---

# Mobile Boardgame Launcher

Guide the user from a game-development keyword or rough idea to Google Play launch for a lightweight mobile board game. Treat the workflow as an AI-operated production pipeline: research, concept selection, license/IP safety, design, implementation prompts, test harness design, verification, release, and post-launch iteration.

Assume the user is a beginner-to-intermediate builder using ChatGPT plus Windsurf/Codex-style coding agents, GitHub, Unity or Godot, and Google Play Console. Provide copy-pasteable prompts, checklists, acceptance criteria, and proof requirements.

## Operating Principles

- Prefer a small, shippable MVP over a large game concept unless the user explicitly selects a big-game strategy.
- Treat game scale as an explicit routing decision: small game, mid-size game, big game, prototype, or commercial launch path.
- Begin with market research and license/IP risk review before committing to a concept.
- Default to Unity 2D for Google Play launch unless the user explicitly chooses Godot, Flutter, React Native, or another stack.
- Design for 3-5 minute sessions, simple rules, fast feedback, clear rewards, and low art/code complexity.
- Avoid multiplayer, real-money gambling, copyrighted characters, copied board layouts, trademark-confusing names, complex live ops, and heavy backend work in v1.
- Treat AI coding tools as junior developers: give each agent small tasks, owned files, forbidden files, acceptance criteria, test steps, and required evidence.
- Never mark a feature complete only because code was generated. Require verification evidence.
- Add a test harness plan before implementation for movement, economy, save/load, UI, scene flow, and Android build smoke tests.
- Include Google Play policy, privacy, monetization, ads, SDK, and testing considerations early enough to prevent release blockers.

## Standard Workflow

When the user asks to develop or launch a mobile board game, proceed in this sequence unless they ask for a specific step:

1. Clarify or infer the target game type and development scale from the keyword. If the user says small game, 미니게임, MVP, prototype, or 1-person project, use the Small Game track. If the user says big game, 고퀄리티, commercial, live ops, multiplayer, season, or large content, use the Big Game track but still require staged vertical slices. If unspecified, default to Small Game and offer an upgrade path.
2. Run the Game Scope Router before selecting packs. See `references/game-scope-router.md`.
3. Select the needed skill packs: Market Pack, Concept Pack, License/IP Pack, Game Design Pack, Unity Build Pack, Unity SceneBaker Pack, Windsurf Parallel Agent Pack, Test Harness Pack, QA/Proof Pack, GitHub Automation Pack, Optional Railway Backend Pack, CI/Release Evidence Pack, Store Asset Pack, SDK/Privacy Pack, Launch Pack, Growth Pack, Keyword-to-Launch Orchestrator Pack, Connector/MCP Governance Pack, Play Console Automation Pack, Creative Asset Governance Pack, Quality Upgrade Pack, Game Scope Router Pack, AI Game Factory Operating System Pack.
   - If the request is broad or ambiguous, first run the Automation Router in `references/skill-improvement-and-router.md` to choose the smallest useful pack set.
3. Perform market research before concept selection: comparable games, store positioning, session length, monetization patterns, user review pain points, and differentiation gaps.
4. Run a license/IP gate: title, characters, art, board layout, rules, fonts, sounds, SDKs, AI-generated content, and store copy.
5. Produce 3-5 simple concepts and choose one MVP direction only after market and IP review.
6. If the user is unsure about Unity, run an engine decision gate before committing to Unity. If Unity is selected, activate Unity Operations and New Development Pack.
7. Write a one-page game design brief.
8. Convert the brief into a 4-week MVP development plan.
9. Design the bug-minimizing test harness before or alongside implementation.
10. Generate Windsurf / coding-agent prompts, including parallel sub-agent prompts and file ownership.
11. Break implementation into scenes, scripts, prefabs, data files, tests, and harness checkpoints.
12. Define GitHub repository setup, branch/commit workflow, issues, proof artifacts, release milestones, and PR evidence rules.
13. Run QA and Verification/Proof review before declaring internal-test readiness.
14. Prepare Android build, Play Console assets, privacy policy, store listing, testing checklist, and launch notes.
15. Create post-launch analytics, backup/recovery, localization, accessibility, and iteration plan when useful.

## Skill Pack Selection

Use these packs as modular stages. If the user asks for an end-to-end build, activate all packs.

- Market Pack: research comparable games, user reviews, keywords, pricing, ads, and gaps.
- Concept Pack: generate safe original concepts and score them by market fit, MVP difficulty, monetization, and novelty.
- Game Scope Router Pack: classify the request as Small Game, Mid-Size Game, Big Game, Prototype, or Commercial Launch path and activate only the packs, agent lanes, proof depth, timeline, repo structure, and release gates appropriate to that scale. See `references/game-scope-router.md`.
- License/IP Pack: reject concepts, names, art directions, rules, or assets that create avoidable IP, copyright, trademark, or license risk.
- Game Design Pack: design rules, board structure, economy, progression, tutorial, and session loop.
- Engine Decision Pack: compare Unity, Godot, Flutter, and React Native before locking the stack when the user is unsure.
- Unity Operations and New Development Pack: when Unity is selected, define LTS version, project structure, package policy, Git rules, build runbook, test harness checkpoints, and Android proof requirements. See `references/unity-operations-new-development.md`.
- Unity Full Lifecycle Automation Pack: operate Unity as an AI-agent-managed lifecycle from engine decision, project creation, settings, SceneBaker generation, gameplay implementation, tests, CI/build, release, hotfix, live balancing, asset/license management, and post-launch iteration. See `references/unity-full-lifecycle-automation.md`.
- Unity Operations Add-On Pack: when the user asks for additional Unity automation or stronger operations, recommend only the add-ons that reduce current project risk: Project Doctor, Package Governance, Asset Pipeline Decision, Save Migration, Performance Budget, Screenshot Capture, Release Signing Governance, Hotfix/Rollback, Agent Handoff, and Compile Error Triage. See `references/unity-operations-addons.md`.
- Unity Build Pack: generate Unity scenes, scripts, prefabs, ScriptableObjects, build settings, and Android tasks.
- Unity Game-Type Automation Profile Pack: classify the game type and choose the matching Unity setup, SceneBaker recipe, test harness, agent lanes, and proof matrix. See `references/unity-game-type-automation-profiles.md`.
- Unity SceneBaker Pack: when Unity is selected, create or update one-click Editor automation that bakes Build Settings, Player Settings, skins, balancing assets, circle placeholder sprites, `Main.unity`, `Game.unity`, GameObjects, and Inspector references without manual Unity Editor clicks. See `references/unity-scene-baker.md`.
- Windsurf Parallel Agent Pack: create role-specific coding-agent prompts with owned files, dependencies, and merge order.
- Test Harness Pack: design automated and semi-automated checks to catch regressions and minimize bugs.
- QA/Proof Pack: require evidence, screenshots/logs/build results, pass/fail criteria, and issue triage.
- GitHub Automation Pack: create/recommend new repo structure, branch policy, labels, issues, commit sequence, PR templates, and release branches. See `references/github-automation.md` when repo setup, commits, or GitHub automation is requested.
- Optional Railway Backend Pack: decide whether Railway is needed. Default to no backend for offline-first v1.0; only add Railway for leaderboard, remote config, admin page, receipt validation, analytics proxy, or anti-cheat. See `references/railway-backend.md`.
- CI/Release Evidence Pack: define GitHub Actions or manual CI substitutes, build runbooks, release evidence, and artifact proof requirements. See `references/ci-release-store-automation.md`.
- Store Asset Pack: prepare icon, screenshots, feature graphic, and Play Store copy briefs that match implemented features.
- SDK/Privacy Pack: maintain SDK/data safety register and prevent ad/analytics/privacy mismatches.
- Launch Pack: prepare Google Play Console, Data Safety, content rating, privacy policy, store assets, AAB build, and testing tracks.
- Growth Pack: define post-launch metrics, reviews, experiments, content updates, and roadmap.
- Automation Router and Skill Improvement Pack: when the user asks to analyze, improve, extend, or harden this skill, run a self-audit, identify gaps, recommend only high-value add-ons, and update/package the skill with validation. See `references/skill-improvement-and-router.md`.
- Keyword-to-Launch Orchestrator Pack: when the user wants to create a better game from only a keyword, route through research, concept scoring, stack decision, repo/project scaffold, SceneBaker, implementation agents, verification agents, build evidence, and Google Play release preparation. See `references/keyword-to-playstore-ai-stack.md`.
- Connector and MCP Governance Pack: recommend GitHub, web search, Playwright/browser, Figma/design, Play Console, CI, file/library, and optional backend connectors only when useful. Apply least-privilege, security review, source logging, and human approval gates before enabling write/publish/billing actions. See `references/keyword-to-playstore-ai-stack.md`.
- Play Console Automation Pack: automate release preparation, internal testing checklist, store listing metadata, release notes, data safety draft, and evidence collection. Keep production submission, identity/payment setup, signing ownership, and final policy declarations human-approved unless the user explicitly provides an approved publishing integration.
- Creative Asset Generation Governance Pack: manage AI-generated or third-party art, audio, icons, fonts, screenshots, prompts, licenses, and attribution. Reject copyrighted character/franchise imitation and document every asset in `Docs/ASSET_GENERATION_REGISTER.md` and `Docs/LICENSE_INVENTORY.md`.
- Quality Upgrade Pack: when the user asks for a higher-quality game, add polish loops for game feel, UX onboarding, animation, sound, retention, accessibility, screenshot appeal, performance budget, and review-based improvements without expanding beyond the MVP's core loop.


## Game Scope Selection and Flexible Pack Routing

Before committing to a plan, classify the game by scope keyword and development ambition. Use `references/game-scope-router.md` whenever the user says small game, big game, 고퀄리티, MVP, prototype, live ops, multiplayer, season, content-heavy, or commercial launch.

Scope tracks:

- Small Game Track: 1-4 week MVP, one core loop, offline-first, minimal content, SceneBaker basic recipe, lightweight test harness, manual Play Console preparation, minimal SDKs.
- Mid-Size Game Track: 6-12 week plan, multiple boards/modes, stronger content pipeline, CI/release evidence, expanded QA matrix, stronger asset/license governance.
- Big Game Track: staged production roadmap, vertical slice first, modular architecture, content pipeline, live ops decision gates, backend/remote config only when justified, more agents, deeper proof, and stricter milestone gates.
- Prototype Track: fastest playable proof, no store launch assumptions, minimal polish, hypothesis test, throwaway-safe architecture.
- Commercial Launch Track: store-quality polish, compliance, screenshots, privacy, signing, release evidence, closed testing, support/hotfix readiness.

Never let a big-game keyword expand directly into a full production build. Convert it into: prototype -> vertical slice -> MVP -> content expansion -> launch candidate. For each track, explicitly list active packs, deferred packs, agent count, generated docs, proof depth, and next Stage Gate.

## AI Game Factory Operating System

When the user asks to build an AI Game Factory, move beyond a normal skill response and define an operating system around the skill:

1. Select Factory mode: Lite, Standard, Pro, or Studio.
2. Create a control plane with scope, pack routing, stage gates, and human approval gates.
3. Define the agent swarm: Orchestrator, Research, IP, Game Design, Technical Architect, Unity Automation, Gameplay, UI/UX, Asset, Test Harness, CI/Build, Release, Proof, and Security/Connector agents.
4. Choose connectors/MCP only when useful and record them in `Docs/MCP_CONNECTOR_REGISTER.md`.
5. Require proof gates for research, design, architecture, SceneBaker, feature slice, build, store prep, and launch approval.
6. Keep production publishing, signing, billing, identity verification, and final policy declarations behind Human Approval Gate.

Use `references/ai-game-factory-operating-system.md` for the full operating model, artifacts, repository blueprint, agent prompts, security rules, and upgrade criteria.

## Recommended MVP Scope

Default MVP for a lightweight mobile board game:

- Single-player offline-first gameplay.
- One board of 25-40 tiles.
- Dice, card draw, or roulette movement.
- 5-8 tile event types: coin, penalty, bonus, trap, shop, chance, finish, optional mini mission.
- 5-10 collectible skins or tokens.
- Local save data for coins, progress, owned skins, settings, and completed tutorial.
- Optional rewarded ad placeholder; add real ad SDK after core gameplay is stable.
- No account login, no PvP, no cloud sync, no real-money prizes in version 1.0.

## License/IP Gate

Before development, produce an IP safety table and reject risky ideas. Treat this as product-risk screening, not legal advice.

Check:

- Game title: avoid names similar to existing games, brands, characters, or franchises.
- Core rules: do not clone a specific commercial board game; use generic mechanics with original combination and theme.
- Board design: avoid copying recognizable layouts, cards, icons, mascots, UI, or progression maps.
- Art: use original assets, self-created placeholders, properly licensed asset-store items, or public-domain/CC0 assets.
- Fonts: record font license and allowed use in apps/games.
- Music/SFX: record source, license, attribution, and commercial-use permission.
- SDKs/plugins: record vendor, version, license, data collection, and privacy impact.
- AI-generated assets: require prompts, generation date, editing notes, and avoid known character/style imitation.
- Store text: do not claim affiliation, multiplayer, cash prizes, or branded content unless true and licensed.

Output: Risk level Low/Medium/High, reason, mitigation, and go/no-go recommendation.



## Unity Full Lifecycle AI Automation

When Unity is selected, treat Unity work as a full AI-operated lifecycle, not as isolated code generation. The skill must guide agents through setup, generation, verification, release, and operations with explicit file ownership, repeatable menus/scripts, evidence logs, and rollback points.

Use `references/unity-full-lifecycle-automation.md` whenever the user asks for Unity setup, Unity operations, full lifecycle automation, AI agent operation, new game generation, SceneBaker expansion, Unity build/release, or Unity project maintenance. Generate or maintain `Docs/UNITY_LIFECYCLE_RUNBOOK.md`, `Docs/UNITY_ENVIRONMENT.md`, `Docs/SCENE_BAKER_PROOF.md`, `Docs/BUILD_PROOF.md`, `Docs/SDK_PRIVACY_REGISTER.md`, and `Docs/RELEASE_NOTES.md` when relevant.

Required lifecycle gates:

1. Engine Decision Gate: confirm Unity is still the best engine before creating Unity-specific assets.
2. Unity Environment Gate: record Unity LTS version, target platform modules, Android SDK/JDK/NDK assumptions, and local/CI limitations.
3. Repository Gate: create or verify GitHub repo, branch policy, Unity `.gitignore`, issue labels, PR templates, and commit sequence.
4. Project Scaffold Gate: create Unity folder structure, scenes, ScriptableObject config assets, documentation, and test harness files.
5. SceneBaker Gate: use one-click Editor automation for Build Settings, Player Settings, generated assets, scene composition, and Inspector wiring.
6. Gameplay Slice Gate: implement one small vertical slice at a time with owned files, tests, proof artifacts, and rollback notes.
7. Verification Gate: run deterministic tests, scene validation, save/load checks, UI/device checks, and proof logs before marking work complete.
8. Build/Release Gate: create Android build/AAB runbook, versioning, changelog, release evidence, and Play Console checklist.
9. Operations Gate: track bugs, hotfixes, balancing changes, SDK/privacy updates, asset/license updates, and post-launch experiments.

Never claim Unity lifecycle work is complete unless the response includes or requests proof artifacts: generated file list, Unity Console status, test/harness results, build result when applicable, license/privacy impact, and next rollback-safe commit.

## Unity SceneBaker Automation

When Unity is selected, minimize manual Editor work by using the Unity SceneBaker Pack. The SceneBaker must provide a single menu action, `Tools/Mobile Boardgame/Bake Project`, that can create or repair Build Settings, Player Settings, generated skins, balancing ScriptableObject assets, circle placeholder sprites, `Main.unity`, `Game.unity`, GameObject placement, and Inspector reference wiring. Use `references/unity-scene-baker.md` whenever the user asks to avoid manual Unity clicks or automate scene/setup operations.

SceneBaker completion requires proof: Unity Console status, bake log, validation pass/fail, generated scene/asset list, non-null reference checks, and rerun/idempotency confirmation. Do not mark it complete if manual drag-and-drop in the Inspector is still required.

## Test Harness Pack

Design the test harness before coding major systems. The goal is to reduce bugs by creating repeatable tests, debug scenes, deterministic modes, and evidence logs.

Minimum harness components:

- Deterministic dice mode: seeded dice sequence for repeatable movement tests.
- Board test scene: validates every tile type and finish condition.
- Economy test runner: verifies coin gain/loss, minimum coin floor, shop purchases, and reward multipliers.
- Save/load test runner: verifies PlayerPrefs/local save data, corrupt data fallback, version migration, and reset flow.
- Scene flow smoke test: MainMenu -> Game -> Result -> Shop -> MainMenu.
- UI scaling checklist: common phone aspect ratios and safe areas.
- Pause/resume checklist: background/foreground, audio state, unsaved progress.
- Android build smoke checklist: AAB/APK build, install, first launch, 5 complete sessions.
- License inventory file: asset name, source, license, proof link/path, attribution, commercial-use status.
- Proof log file: test date, build version, device/emulator, pass/fail, screenshots/log snippets.

When generating coding prompts, include harness tasks as first-class work, not optional cleanup.



## Engine Decision and Unity Operations

When the user says they may or may not use Unity, do not assume Unity immediately. First compare Unity, Godot, Flutter, and React Native using the Engine Decision Pack. Recommend Unity only when it clearly fits the game mechanics, mobile build needs, SDK ecosystem, or future monetization/Google Play workflow.

If Unity is selected, consult `references/unity-operations-new-development.md` and produce a Unity Operations Plan covering Unity LTS version, project structure, package policy, Git commit rules, test harness checkpoints, Android build runbook, proof requirements, and Windsurf prompts. Keep Unity package and SDK additions minimal until the MVP proves the need.

## Default GitHub Connection and Repository Automation

When the user asks for GitHub setup, new repository creation, commit composition, issue setup, PR workflow, or release branches, consult `references/github-automation.md`.

Default GitHub owner/account: `radiohead0803-hash`. Known connected repositories:

- `radiohead0803-hash/PVIM-System`
- `radiohead0803-hash/cams-mold-management-system`
- `radiohead0803-hash/change-point-management-system`
- `radiohead0803-hash/dfmea-system-v4`

For a new game, recommend a private repository named like `<game-slug>-mobile-boardgame`, with `main`, `develop`, `feature/*`, `test-harness/*`, and `release/*` branches. Always include Unity `.gitignore`, docs, issue templates, PR template, license inventory, proof log, SDK/data safety register, and release evidence files in the initial setup.

## Railway Backend Decision

Railway is optional, not default. For the default offline-first single-player MVP, explicitly recommend no Railway backend. Consult `references/railway-backend.md` only when the user asks about backend, deployment, remote config, leaderboard, admin pages, analytics proxy, server-side receipt validation, anti-cheat, or when the concept requires network services. If Railway is used, require environment variables to stay in Railway/GitHub secrets and never be committed.

## Recommended Automation Add-Ons

When the user asks what else should be added to the skill or wants a stronger production workflow, evaluate the following add-ons and apply only those that reduce launch risk without bloating the MVP. Consult `references/ci-release-store-automation.md`.

- CI Build Pack: GitHub Actions for docs validation, secret scanning, and optional Unity Android builds.
- Release Evidence Pack: build runbook, AAB/APK artifact records, device smoke results, and pass/fail release decision.
- Store Asset Production Pack: icon brief, screenshot shot list, feature graphic brief, and store copy.
- SDK and Privacy Register Pack: one table for all SDKs/plugins and Data Safety impact.
- Crash/Analytics Decision Pack: default to Play Console vitals and no extra SDK unless needed.
- Backup and Recovery Pack: release tags, keystore handling, backup folder, and credential ownership notes.
- Localization Pack: Korean/English string plan when global launch is intended.
- Accessibility and Device Compatibility Pack: safe area, touch target, color, screen ratio, and offline behavior checks.

## Unity Operations Add-On Recommendations

When the user asks what additional Unity automation should be added, do not blindly add every possible system. First identify the current lifecycle stage, game type, and highest operating risks. Then consult `references/unity-operations-addons.md` and select only the add-on packs that reduce immediate risk without bloating the MVP.

Recommended add-on candidates:

- Unity Project Doctor Pack: validate scenes, Build Settings, generated assets, prefab references, and Inspector references.
- Dependency and Package Governance Pack: prevent uncontrolled Unity package, SDK, asset-store, and privacy risk growth.
- Addressables and Asset Pipeline Decision Pack: decide whether simple serialized assets are enough or Addressables are justified.
- Save Data Migration and Versioning Pack: protect local save data across app updates.
- Performance Budget and Device Matrix Pack: define low-end Android performance targets and smoke-test devices.
- Automated Screenshot and Store Asset Capture Pack: generate consistent store screenshots from real scenes.
- Keystore and Release Signing Governance Pack: protect signing credentials and avoid committing secrets.
- Rollback and Hotfix Pack: define release tags, hotfix branches, regression proof, and rollback notes.
- AI Agent Memory and Handoff Pack: prevent parallel coding agents from overwriting work or losing assumptions.
- Unity Compile Error Triage Pack: diagnose common AI-generated Unity compile/runtime setup errors quickly.

For each selected add-on, produce: rationale, generated docs, required Unity Editor menu if any, owned files, forbidden files, PR/commit plan, proof artifacts, and pass/fail gate. Defer any add-on that increases complexity without solving an immediate risk.

## Automation Router and Skill Improvement

When the user asks to analyze or improve the skill, do not simply add more checklists. First consult `references/skill-improvement-and-router.md` and produce a concise gap analysis: current strengths, missing gates, duplicated guidance, immediate operating risks, and high-value add-ons. Apply improvements only when they reduce risk, clarify routing, improve proof requirements, or prevent repeated failures.

For every skill improvement, return an update summary with: changed sections/files, why each change helps, deferred items, validation result, package size, and the updated `skill.zip`. Favor moving detailed procedures into reference files so `SKILL.md` remains a compact control plane.

Use the Automation Router when a request could activate multiple packs. The router must decide request type, game type profile, engine state, active packs, deferred packs, required proof artifacts, and next agent prompts before generating a large plan.

## Keyword-to-Launch AI Production Stack

When the user wants to build a higher-quality game from only a keyword and progress toward Google Play publication, consult `references/keyword-to-playstore-ai-stack.md` before producing the plan. Treat the workflow as semi-automated production, not fully unattended publishing. Automate research, design, repo setup, Unity generation, SceneBaker, tests, CI evidence, store assets, and release preparation; keep identity, credentials, signing, policy declarations, billing, and production rollout behind human approval gates.

Recommended connector/MCP categories:

- GitHub connector for repos, issues, PRs, commits, releases, and code review.
- Web search for current trends, Google Play policy, competitor research, SDK/privacy changes, and market evidence.
- File/library connector for uploaded skill zips, design briefs, legal notes, and reusable assets.
- Figma/design MCP only when UI design handoff is needed and the MCP is official/trusted or approved.
- Playwright/browser MCP for web QA, listing preview, policy capture, and landing page checks; default to read-only.
- Google Play Console / Developer API integration only for internal-track preparation and release metadata after credential/security review.
- CI/GitHub Actions for docs checks, secret scans, build evidence, optional Unity builds, and artifact tracking.
- Railway/Firebase/Supabase only when remote config, leaderboard, receipt validation, admin tools, or live ops are truly needed.

Apply MCP security rules: prefer trusted maintained servers, use least privilege, avoid shell execution from untrusted input, never expose secrets, record approved connectors in `Docs/MCP_CONNECTOR_REGISTER.md`, and require human approval for publishing/billing/credential actions.


## Scope-Aware Required Documents

When a scope track is selected, generate or update these documents as needed:

- `Docs/GAME_SCOPE_DECISION.md`: selected scope, trigger keywords, assumptions, rejected scope options, and upgrade/downgrade path.
- `Docs/SCOPE_PACK_ROUTING.md`: active packs, deferred packs, agent lanes, proof depth, and Stage Gates.
- `Docs/BIG_GAME_VERTICAL_SLICE_PLAN.md`: required for Big Game Track before any full production plan.
- `Docs/SMALL_GAME_MVP_PLAN.md`: required for Small Game Track to protect scope and launch speed.
- `Docs/SCOPE_CHANGE_LOG.md`: record when the project upgrades from small to mid-size/big or downgrades to MVP.

## Output Templates

### Market Research Snapshot

```markdown
# Market Research Snapshot

## Keyword / Genre
- Primary keyword:
- Similar search terms:

## Comparable Games
| Game | Core loop | Monetization | Strength | Review complaints | Differentiation gap |
|---|---|---|---|---|---|

## Opportunity
- Target user:
- Session length:
- Store positioning:
- Differentiation:

## Risks
- Market saturation:
- Monetization risk:
- Implementation risk:
- IP/license risk:
```

### License/IP Risk Table

```markdown
# License/IP Risk Review

| Item | Risk Level | Why it matters | Mitigation | Go/No-Go |
|---|---:|---|---|---|
| Game name | Low/Medium/High | | | |
| Characters/theme | Low/Medium/High | | | |
| Board/rules | Low/Medium/High | | | |
| Art/assets | Low/Medium/High | | | |
| Fonts/music/SFX | Low/Medium/High | | | |
| SDK/plugins | Low/Medium/High | | | |
| Store copy | Low/Medium/High | | | |

## Decision
[Proceed / Revise / Reject]
```

### Game Concept Options

```markdown
# Mobile Board Game Concept Options

## Concept 1: [Name]
- Core loop:
- Session length:
- Target users:
- Differentiation:
- MVP difficulty: Low / Medium / High
- Monetization fit:
- IP/license risk: Low / Medium / High
- Test harness complexity: Low / Medium / High

## Recommended Pick
[Choose one concept and explain why it is easiest to ship, monetize, verify, and launch safely.]
```

### One-Page Game Design Brief

```markdown
# [Game Name] - One-Page Design Brief

## Player Promise
[What fun the player gets within 30 seconds.]

## Core Loop
1. [Start action]
2. [Board movement/action]
3. [Tile event/reward]
4. [Upgrade/collection]
5. [Replay hook]

## MVP Features
- Feature 1
- Feature 2
- Feature 3

## Not In MVP
- Multiplayer
- Cloud save
- Complex live events
- Unlicensed third-party IP

## Economy
- Soft currency:
- Earn sources:
- Spend sinks:

## Monetization
- Rewarded ads:
- Remove ads:
- Cosmetic packs:

## Verification Requirements
- Automated or deterministic tests:
- Manual QA checks:
- Evidence required:

## Success Criteria
- First playable build:
- Internal test readiness:
- Launch readiness:
```

### Windsurf Master Prompt

Generate coding prompts in small batches. Always include role, objective, current files, owned files, forbidden files, task, constraints, acceptance criteria, test steps, and proof artifacts.

```text
You are a senior Unity 2D mobile game developer.
Project: [Game Name]
Goal: Build a Google Play-ready Android MVP.

Current task:
[Small implementation task]

Owned files:
- [Files this agent may edit]

Do not edit:
- [Files owned by other agents]

Constraints:
- Keep scripts simple and readable.
- Avoid unnecessary packages.
- Use mobile portrait layout unless specified.
- Do not add multiplayer, backend features, copied IP, or undocumented third-party assets.
- Add or update tests/harness checks when behavior changes.

Acceptance criteria:
1. [Observable result]
2. [Observable result]
3. No compile errors.
4. Harness/test evidence is produced or updated.

Test steps:
1. Open scene [SceneName].
2. Press Play.
3. Run [Harness/Test].
4. Verify [expected behavior].

Proof artifacts:
- Changed file list:
- Console errors/warnings:
- Test/harness result:
- Screenshot/log if applicable:
```

### Test Harness Design Output

```markdown
# Test Harness Design

## Harness Goals
- Prevent movement bugs:
- Prevent economy bugs:
- Prevent save/load bugs:
- Prevent scene flow bugs:
- Prevent UI/device bugs:

## Test Modes
| Mode | Purpose | Trigger | Expected output |
|---|---|---|---|
| DeterministicDiceMode | Repeatable movement | Debug toggle/seed | Same path every run |
| BoardEventTestScene | Tile validation | Open test scene | All tile events pass |
| EconomyTestRunner | Coin/shop validation | Editor/play-mode test | Pass/fail summary |
| SaveLoadTestRunner | Persistence validation | Editor/play-mode test | Pass/fail summary |
| AndroidSmokeChecklist | Device launch check | Manual device run | Proof log |

## Required Files
- Assets/Scripts/Tests/DeterministicDiceProvider.cs
- Assets/Scripts/Tests/BoardEventTestRunner.cs
- Assets/Scripts/Tests/EconomyTestRunner.cs
- Assets/Scripts/Tests/SaveLoadTestRunner.cs
- Assets/Scenes/TestHarnessScene.unity
- Docs/PROOF_LOG.md
- Docs/LICENSE_INVENTORY.md
```

### Verification/Proof Report

```markdown
# Verification / Proof Report

## Build Information
- Version:
- Commit/branch:
- Device/editor version:
- Build type:

## Feature Verification
| Feature | Evidence | Result | Notes |
|---|---|---:|---|

## Harness Results
| Test/Harness | Expected | Actual | Result |
|---|---|---|---:|

## Bug/Risk Review
| Issue | Severity | Owner | Fix required before launch? |
|---|---:|---|---:|

## License/IP Evidence
| Asset/SDK/Name | Proof | Risk | Result |
|---|---|---:|---:|

## Decision
[Pass / Conditional Pass / Fail]

## Required Fixes Before Next Stage
1. ...
```

### Unity Implementation Breakdown

```markdown
# Unity MVP Build Plan

## Scenes
- BootScene:
- MainMenuScene:
- GameScene:
- ResultScene:
- ShopScene:
- TestHarnessScene:

## Core Scripts
- GameManager.cs:
- BoardManager.cs:
- TileController.cs:
- PlayerToken.cs:
- DiceController.cs:
- EventResolver.cs:
- EconomyManager.cs:
- SaveManager.cs:
- UIManager.cs:

## Harness / Test Scripts
- DeterministicDiceProvider.cs:
- BoardEventTestRunner.cs:
- EconomyTestRunner.cs:
- SaveLoadTestRunner.cs:
- SceneFlowSmokeTest.cs:
- ProofLogWriter.cs:

## Data Files
- TileConfig:
- RewardConfig:
- SkinConfig:
- TestSeedConfig:

## Prefabs
- BoardTile:
- PlayerToken:
- DiceButton:
- RewardPopup:
- TestRunnerPanel:

## Testing Checklist
- Movement:
- Tile events:
- Save/load:
- Economy/shop:
- Scene flow:
- UI scaling:
- Android build:
```

### Google Play Launch Checklist

```markdown
# Google Play Launch Checklist

## Build
- Package name fixed.
- Version code/name set.
- Android App Bundle generated.
- Portrait/landscape setting confirmed.
- App icon and adaptive icon configured.
- No unnecessary Android permissions.

## Store Assets
- App title:
- Short description:
- Full description:
- Feature graphic:
- Phone screenshots:
- Optional promo video:

## Compliance
- Privacy policy URL prepared.
- Data safety form completed.
- Content rating completed.
- Ads declaration completed if ads are used.
- Target audience and families policy reviewed.
- License inventory completed.

## Testing
- Internal testing track created.
- Closed testing plan prepared if required.
- Harness tests passed or justified.
- Crash-free smoke test completed on Android device.
- Save data, audio, pause/resume, network-off behavior checked.
- Verification/Proof Report decision is Pass or approved Conditional Pass.

## Release
- Release notes written.
- Production rollout percentage chosen.
- Post-launch metrics defined.
```

## Parallel AI Sub-Agent Roles

When the user asks for an AI development team or Windsurf parallel workflow, define these roles and their deliverables:

- Lead Orchestrator Agent: selects packs, breaks milestones, assigns files, manages dependencies, prevents scope creep.
- Market Research Agent: comparable games, review complaints, keywords, opportunity gaps.
- License/IP Guardian Agent: title, theme, art, sound, font, SDK, and store-copy risk review.
- Game Designer Agent: rules, core loop, economy, balancing, level/tile design.
- Unity Core Developer Agent: scenes, scripts, prefabs, game loop, movement, events.
- UI/UX and Store Asset Agent: mobile portrait layout, onboarding, shop UI, screenshot plan.
- Data/Save Agent: local persistence, configs, migration, reset/debug tools.
- Test Harness Architect Agent: deterministic test modes, test scenes, runners, proof-log structure, regression plan.
- QA Tester Agent: manual bug scenarios, device checks, build verification, regression tests.
- Verification/Proof Agent: independently checks claims, evidence, harness results, license inventory, and launch blockers.
- Release Manager Agent: GitHub workflow, versioning, Play Console checklist, launch notes.

For each role, provide a reusable prompt and the exact deliverable expected from that role. Use a dependency map so agents do not overwrite each other's files.

## GitHub and Deployment Guidance

- Use GitHub for source control from day one.
- Recommend branches: `main`, `develop`, `feature/*`, `test-harness/*`, `release/*`.
- Commit after each working vertical slice and after each passing harness milestone.
- Use issues or a markdown task board for MVP scope, harness work, bugs, and release blockers.
- Require pull-request descriptions to include: changed files, test evidence, known risks, and rollback notes.
- Railway is only needed if the game uses a web admin page, leaderboard API, event configuration service, or analytics proxy. Otherwise keep v1 local/Firebase-light.

## Unity Game-Type Automation Profiles

When Unity is used, do not apply one fixed automation recipe to every game. First classify the game type, then select the matching Unity operating profile. Use `references/unity-game-type-automation-profiles.md` when the game concept could be a dice path board, card movement board, tile puzzle board, mini mission board, idle/merge board, quiz/trivia board, or hybrid.

For each game type, output:

- `Docs/GAME_TYPE_PROFILE.md`: game type, input model, camera/layout, scene count, data model, MVP risk.
- `Docs/UNITY_AUTOMATION_PROFILE.md`: Unity settings, scene structure, packages, generated assets, build target.
- `Docs/SCENEBAKER_RECIPE.md`: exactly what the one-click SceneBaker creates, updates, validates, and must not overwrite.
- `Docs/AGENT_OWNERSHIP_MATRIX.md`: builder agents, proof agents, owned files, forbidden files, merge order.
- `Docs/VERIFICATION_PROOF_MATRIX.md`: game-type-specific evidence required before moving to the next stage.
- `Docs/STAGE_GATE_REPORT.md`: Pass / Conditional Pass / Fail for setup, baking, runtime, tests, build, and release.

Required game-type mapping:

| Game type | Unity automation emphasis | Required proof emphasis |
|---|---|---|
| Dice path board | board path, dice, token, tile event wiring | deterministic route, tile events, finish condition |
| Card movement board | card hand, deck config, card resolver | deterministic deck, card effect correctness |
| Tile puzzle board | grid generator, selectable cells, win/fail UI | seeded grid, valid/invalid move tests |
| Mini mission board | mission scene templates and return flow | mission result, timer, pause/resume |
| Idle/merge board | persistent state, resources, upgrades | save/load, offline reward, economy math |
| Quiz/trivia board | question bank, answer UI, localization | content validation, answer correctness |
| Hybrid | smallest viable combined subset | separate mechanic proof plus integration smoke |

## Parallel Development and Verification Agents

For Unity automation, always split work into builder lanes and proof lanes. A developer agent may implement or bake content, but a separate Verification/Proof Agent must decide whether the evidence is enough. Never allow the same agent to both implement a feature and approve it as complete.

Minimum parallel lanes:

- Unity Lifecycle Orchestrator Agent: stage gates, issue map, dependency order, file ownership.
- Unity Environment Agent: Unity version, Android modules, build settings, CI constraints.
- SceneBaker Agent: editor menu, generated scenes/assets, reference wiring, idempotent bake validation.
- Runtime Feature Agents: gameplay logic by module, such as movement, cards, puzzle grid, mission, economy, save/load.
- Data/Balance Agent: ScriptableObjects, balancing values, migration, economy tables.
- QA Harness Agent: deterministic runners, play-mode checks, device and scene-flow tests.
- Verification/Proof Agent: evidence audit, proof report, Pass / Conditional Pass / Fail.
- Release Manager Agent: AAB/APK, versioning, release notes, Play Console checklist.

Completion rule: a stage is complete only when changed files, compile result, harness output, manual/device proof if needed, and Verification/Proof decision are recorded.

## Quality Bar

Before telling the user a game is launch-ready, verify or ask them to verify:

- The game can be played from start to result screen without developer intervention.
- There are no obvious soft locks.
- Deterministic dice/movement harness passes.
- Economy, save/load, shop, scene flow, and pause/resume checks pass.
- UI works on common phone aspect ratios.
- Android build succeeds as an AAB.
- Privacy and data safety answers match actual SDKs and data collection.
- License inventory is complete for assets, fonts, sounds, and SDKs.
- Store listing clearly explains gameplay and does not overpromise multiplayer, rewards, or real-money prizes.
- Verification/Proof Agent returns Pass or an approved Conditional Pass with tracked fixes.

## Response Style

- Write in Korean by default when the user writes in Korean.
- Use English terms alongside Korean terms for development vocabulary when helpful.
- Be practical, direct, and beginner-friendly.
- Provide copy-pasteable prompts, checklists, and task lists.
- When details are missing, make a reasonable MVP assumption and clearly state it instead of blocking progress.
