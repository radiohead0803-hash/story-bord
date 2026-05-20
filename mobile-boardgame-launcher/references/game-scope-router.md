# Game Scope Router

Use this reference when the user wants to choose between a small game and a bigger, higher-quality game, or when the keyword implies scope uncertainty.

## Scope Classification

| Track | Trigger keywords | Default goal | Default timeline | Risk posture |
|---|---|---|---|---|
| Prototype | idea test, 실험, 빠르게, proof, sample | playable proof of concept | 1-7 days | disposable, learning first |
| Small Game | 작은 게임, 미니게임, MVP, casual, simple, 1인 개발 | shippable small game | 1-4 weeks | strict scope control |
| Mid-Size Game | 고퀄리티, multiple modes, several boards, collection, season-lite | polished MVP plus content | 6-12 weeks | staged expansion |
| Big Game | 큰 게임, live ops, multiplayer, long-term, many levels, commercial studio | vertical slice first, not full build first | 3-6+ months | milestone-gated |
| Commercial Launch | Google Play 출시, revenue, ads, store ready, closed test | launch candidate | depends on build maturity | compliance-first |

If the user only provides a keyword, default to Small Game Track and include an upgrade path. If the keyword contains big-game ambition, select Big Game Track but force a vertical-slice gate before production scaling.

## Pack Routing by Scope

### Prototype Track
Activate: Market Pack lite, Concept Pack, License/IP lite, Game Design lite, Engine Decision, minimal Unity/Godot scaffold, one smoke test.
Defer: monetization SDKs, backend, Play Console, complex CI, full asset pipeline.
Proof depth: playable loop proof, screenshot/video note, known limitations.

### Small Game Track
Activate: Market Pack, Concept Pack, License/IP Pack, Game Design Pack, Unity Game-Type Profile, SceneBaker basic, Test Harness basic, GitHub basic, Launch Pack lite.
Defer: backend, live ops, multiplayer, Addressables, heavy analytics, advanced CI unless launch-ready.
Proof depth: deterministic tests, scene flow, save/load, Android smoke, license inventory.

### Mid-Size Game Track
Activate: Small Game Track plus content pipeline, Project Doctor, Package Governance, screenshot capture, performance budget, expanded QA, CI/release evidence.
Conditional: remote config, analytics, Addressables, localization.
Proof depth: feature tests, content validation, device matrix, release evidence, regression log.

### Big Game Track
Activate: Scope Gate, Market Research deep, Concept Scorecard, Architecture Agent, Vertical Slice Plan, modular Unity automation, content pipeline decision, CI, QA matrix, Project Doctor, Release Evidence.
Conditional only after gate: backend, live ops, multiplayer, IAP, remote config, Play Console automation.
Proof depth: vertical slice pass, architecture review, performance budget, risk burndown, milestone reports.
Rule: never generate a full big-game production plan before the vertical slice plan and milestone gates are accepted.

### Commercial Launch Track
Activate: Launch Pack, Store Asset Pack, SDK/Privacy Pack, License/IP final, Play Console Automation boundaries, Release Signing Governance, Closed Test Plan, Hotfix/Rollback, Support Plan.
Proof depth: AAB build, store listing evidence, privacy/data safety draft, signing runbook, closed testing readiness, release notes.
Human approval required: final Google Play submission, identity/payment, keystore ownership, production rollout, policy declarations.

## Agent Sizing by Scope

| Track | Minimum agents | Optional agents |
|---|---|---|
| Prototype | Orchestrator, Core Developer, Proof Agent | Market Agent |
| Small Game | Orchestrator, Game Designer, Unity Core, SceneBaker, Test Harness, Proof, Release | UI/UX, Asset Agent |
| Mid-Size Game | Small Game agents plus Architecture, Content Pipeline, Performance, Package Governance | Localization, Analytics |
| Big Game | Mid-Size agents plus Technical Director, Backend/LiveOps Decision, QA Lead, Risk Manager | Economy/Retention, Community/Ops |
| Commercial Launch | Release Manager, Privacy/SDK, Store Asset, QA, Proof, Hotfix/Rollback | Support/CRM |

## Scope Change Rules

- Upgrade small -> mid-size only after the core loop is playable and tested.
- Upgrade mid-size -> big only after a vertical slice proves fun, performance, and production feasibility.
- Downgrade big -> small when timeline, budget, asset burden, backend complexity, or QA risk is too high.
- Record every scope change in `Docs/SCOPE_CHANGE_LOG.md`.

## Required Output Template

```markdown
# Game Scope Decision

## Input keyword

## Selected track
Prototype / Small Game / Mid-Size Game / Big Game / Commercial Launch

## Why this track

## Active packs

## Deferred packs

## Agent lanes

## Proof depth

## Stage Gates
1.
2.
3.

## Upgrade / downgrade path

## Generated documents
```
