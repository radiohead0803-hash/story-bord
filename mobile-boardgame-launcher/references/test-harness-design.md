# Test Harness Auto-Design Guide

Use this guide whenever the user asks to reduce bugs, improve completeness, add verification, or prepare a game for internal testing/launch.

## Purpose

A test harness is a small set of debug scenes, deterministic modes, test runners, and proof logs that make game behavior repeatable and verifiable. It should be designed before major implementation so coding agents know how their work will be tested.

## Required Harness Layers

1. Deterministic simulation
   - Replace random dice/card/chance results with seeded values.
   - Allow repeatable full-session playthroughs.

2. Rule validation
   - Check board movement, finish condition, skip-turn logic, chance events, and tile effects.

3. Economy validation
   - Check coin floors, reward values, shop purchases, equipped skins, and ad reward placeholders.

4. Persistence validation
   - Check save/load, reset, corrupt data fallback, and version migration.

5. Scene-flow validation
   - Check MainMenu -> Game -> Result -> Shop -> MainMenu without soft locks.

6. Device smoke validation
   - Check UI scaling, pause/resume, offline mode, audio/settings, Android install and launch.

7. Evidence logging
   - Record test date, build version, device/editor version, commit, result, and unresolved issues.

## Suggested Unity Files

- Assets/Scenes/TestHarnessScene.unity
- Assets/Scripts/Tests/DeterministicDiceProvider.cs
- Assets/Scripts/Tests/BoardEventTestRunner.cs
- Assets/Scripts/Tests/EconomyTestRunner.cs
- Assets/Scripts/Tests/SaveLoadTestRunner.cs
- Assets/Scripts/Tests/SceneFlowSmokeTest.cs
- Assets/Scripts/Tests/ProofLogWriter.cs
- Assets/Scripts/Tests/TestHarnessUI.cs
- Docs/PROOF_LOG.md
- Docs/LICENSE_INVENTORY.md

## Harness Acceptance Criteria

- The harness can run without external network access.
- It does not require production ads, login, or cloud services.
- It can test the same board path repeatedly using a fixed seed.
- It reports pass/fail in a way a non-developer can understand.
- It records enough evidence for the Verification/Proof Agent to make a Pass/Fail decision.

## Bug Report Template

```markdown
# Bug Report

## Summary

## Build / Commit

## Reproduction Steps
1.
2.
3.

## Expected Result

## Actual Result

## Severity
Blocker / High / Medium / Low

## Suspected Owner

## Evidence
- Screenshot/log:
- Harness result:

## Fix Verification Steps
```
