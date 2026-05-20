# Skill Improvement and Automation Router

Use this reference when the user asks to analyze, improve, extend, or harden the mobile-boardgame-launcher workflow itself, or when the project has grown enough that the correct automation path is no longer obvious.

## Purpose

The skill should behave like an automation router, not a pile of unrelated checklists. Before adding work, decide which stage, game type, engine, risk level, and proof requirement applies. Add only the smallest set of packs that reduce risk or unblock the next milestone.

## Self-Audit Checklist

| Area | What to check | Improve if |
|---|---|---|
| Trigger clarity | Does the skill know when to invoke web, GitHub, Unity, Railway, or Play Console guidance? | The response chooses tools without an explicit gate |
| Scope control | Does the plan still fit a small MVP? | The project adds backend, live ops, SDKs, or multiplayer too early |
| Engine routing | Is Unity actually the right engine? | The user is unsure or the game is UI-only/simple web-like |
| Game-type profile | Does the automation match dice, card, puzzle, idle, quiz, or hybrid mechanics? | SceneBaker/test harness is generic and misses mechanics |
| Proof model | Is every completion claim tied to evidence? | The response says complete without logs/screenshots/test results |
| Agent boundaries | Are owned files and forbidden files defined? | Multiple agents can edit the same scene/script without coordination |
| Failure recovery | Is there a rollback/hotfix path? | Compile errors, broken scenes, or bad builds have no triage path |
| Privacy/IP | Are SDKs/assets/store claims recorded? | Ads, analytics, AI art, fonts, or sounds are added without records |
| Release readiness | Is launch state separated from development state? | The project jumps to Play Store assets before test evidence |

## Automation Router

Use this routing order before producing a plan:

1. **Request type**
   - Idea/brainstorming -> Trend Research + Concept + IP Gate
   - Build/new project -> Engine Decision + GitHub + Unity/Godot setup
   - Unity setup/scene work -> Unity Profile + SceneBaker + Project Doctor
   - Bug/failure -> Compile Error Triage + Project Doctor + rollback plan
   - Release -> CI/Release Evidence + Play Console + SDK/Privacy
   - Skill improvement -> Self-Audit + Pack Recommendation + package update

2. **Game type**
   - Dice Path: board positions, dice provider, tile resolver, economy tests
   - Card Movement: deck state, draw/discard, deterministic card sequence
   - Tile Puzzle: board grid, tile state, hint/turn economy, puzzle validation
   - Mini Mission: mission launcher, timeout, scoring, fail/retry tests
   - Idle/Merge: timers, offline rewards, economy exploit checks
   - Quiz/Trivia: question bank, answer validation, localization and content review
   - Hybrid: pick one primary profile and add one secondary profile only

3. **Automation depth**
   - Level 0: Plan only
   - Level 1: Docs + prompts
   - Level 2: Repo/branch/issues/templates
   - Level 3: Unity Editor scripts/SceneBaker/test harness
   - Level 4: CI/build/release evidence
   - Level 5: Backend/live ops/remote config if explicitly justified

4. **Proof depth**
   - Planning proof: completed docs and decision tables
   - Code proof: changed files, compile status, unit/play-mode tests
   - Scene proof: SceneBaker log, non-null reference validation, screenshot
   - Build proof: AAB/APK result, device smoke test, version/commit
   - Release proof: Play Console checklist, privacy/IP/license register, tester results

## Pack Recommendation Rules

Recommend add-ons only when they solve an immediate risk.

| Risk | Add-on Pack |
|---|---|
| Manual Unity setup errors | SceneBaker + Project Doctor |
| Agent overwrites | Agent Ownership + Handoff Log |
| Generic automation mismatches game mechanics | Game-Type Automation Profile |
| Code compiles locally but CI/build fails | CI/Release Evidence Pack |
| Too many packages/SDKs | Package Governance + SDK/Privacy Register |
| Save breaks after update | Save Migration Pack |
| Store screenshots inconsistent | Screenshot Capture Pack |
| Low-end phones lag/crash | Performance Budget + Device Matrix |
| Release signing risk | Keystore/Signing Governance |
| Post-release emergency fixes | Hotfix/Rollback Pack |

## Output Template: Skill Improvement Report

```markdown
# Skill Improvement Report

## Current Strengths
- ...

## Gaps / Risks
| Gap | Impact | Recommended improvement | Priority |
|---|---:|---|---:|

## Improvements Applied
| Change | Where added | Why it helps |
|---|---|---|

## Deferred Improvements
| Item | Why deferred | Trigger to add later |
|---|---|---|

## Validation
- Skill validation:
- Package size:
- Updated files:
```

## Output Template: Automation Router Decision

```markdown
# Automation Router Decision

## User request type

## Game type profile

## Engine decision

## Active packs

## Deferred packs

## Required proof artifacts

## Next agent prompts
```

## Failure Recovery Rules

When automation fails, do not continue adding features. Stop and route to recovery:

1. Capture the exact failure: compile error, scene missing reference, failed test, failed build, policy issue.
2. Assign owner: Core Developer, SceneBaker, Test Harness, Release, Privacy/IP, Backend.
3. Create a minimal reproduction or deterministic test.
4. Fix in the smallest possible commit.
5. Re-run only the relevant validation first, then the full stage gate.
6. Update `Docs/KNOWN_ERRORS.md` and `Docs/AGENT_HANDOFF_LOG.md`.

## Skill Maintenance Cadence

After every 3-5 real project uses, audit:

- Which sections were actually used?
- Which outputs were too long or too generic?
- Which errors repeated?
- Which manual Unity operations still remained?
- Which agent prompts caused overlapping file edits?
- Which proof artifacts were missing?

Move long or rarely used details into references rather than expanding `SKILL.md` further.
