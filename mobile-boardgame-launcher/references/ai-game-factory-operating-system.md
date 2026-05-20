# AI Game Factory Operating System

Use this reference when the user asks to make the system more powerful than a single skill, asks for an AI Game Factory, or wants keyword-to-Google-Play game production with agents, connectors, MCP, Unity automation, CI, proof gates, and human approval.

## Purpose

AI Game Factory is an operating model that turns the skill into a repeatable production system:

```text
Keyword Intake
-> Scope Router
-> Market and IP Research
-> Concept Scorecard
-> Stack and Engine Decision
-> GitHub Project Factory
-> Unity/Godot Project Factory
-> Agent Swarm Development
-> SceneBaker / Project Doctor
-> Test Harness and CI Proof
-> Store Asset and Policy Preparation
-> Human Approval Gate
-> Google Play Release Prep
-> Post-launch Growth Loop
```

The skill remains the control plane. GitHub, Unity editor scripts, CI, MCP/connectors, test harnesses, and proof agents provide execution power.

## Factory Layers

| Layer | Role | Output |
|---|---|---|
| Control Plane | Choose workflow, packs, agents, gates | `Docs/FACTORY_CONTROL_PLANE.md` |
| Intake Plane | Convert keyword to scoped game request | `Docs/KEYWORD_INTAKE.md` |
| Research Plane | Trend, competitor, IP, license research | `Docs/TREND_MARKET_RESEARCH.md`, `Docs/RESEARCH_SOURCES.md` |
| Design Plane | Concept, rules, economy, UX, content plan | `Docs/GAME_DESIGN_BRIEF.md`, `Docs/CONCEPT_SCORECARD.md` |
| Build Plane | Repo, engine, scene, code, assets | GitHub repo, Unity/Godot project |
| Automation Plane | SceneBaker, Project Doctor, CI, scripts | Editor menu, workflows, validation logs |
| Proof Plane | Independent evidence and stage gates | `Docs/STAGE_GATE_REPORT.md`, `Docs/RELEASE_EVIDENCE.md` |
| Release Plane | Play Store prep, AAB, data safety draft | `Docs/PLAY_CONSOLE_AUTOMATION_PLAN.md` |
| Growth Plane | reviews, metrics, updates, hotfixes | `Docs/GROWTH_LOOP.md`, `Docs/HOTFIX_RUNBOOK.md` |

## Operating Modes

Always select one operating mode before building.

| Mode | When to use | Automation depth | Human gate |
|---|---|---:|---|
| Factory Lite | prototype, small game, solo builder | 1-3 | before release |
| Factory Standard | commercial MVP, 1-3 month launch | 2-4 | before SDK, signing, release |
| Factory Pro | higher-quality game, many systems | 3-5 | every major stage gate |
| Factory Studio | multi-game pipeline or large game | 4-5 | roadmap, budget, IP, launch |

Default to Factory Lite for early ideas. Upgrade only when the user explicitly needs scale, quality, or repeated production.

## Agent Swarm

Use a split between creation agents and proof agents. A creator agent cannot approve its own work.

| Agent | Owns | Must produce |
|---|---|---|
| Factory Orchestrator | scope, timeline, pack routing, gates | task board, ownership matrix, stage decisions |
| Trend Research Agent | market, competitor, review signals | research report with sources |
| IP and License Agent | title, theme, assets, SDK risk | risk table and go/no-go |
| Game Design Agent | core loop, rules, economy, UX | design brief and balancing assumptions |
| Technical Architect Agent | engine, repo, folders, data flow | stack decision and architecture map |
| Unity Automation Agent | SceneBaker, Project Doctor, settings | editor scripts and validation results |
| Gameplay Agent | movement, turns, events, economy | working feature slices with tests |
| UI/UX Agent | menu, HUD, tutorial, store screenshots | UI scenes and screenshot plan |
| Asset Agent | placeholder art, icons, audio, fonts | asset register and license proof |
| Test Harness Agent | deterministic tests, smoke tests | test runners and proof log |
| CI/Build Agent | GitHub Actions, Android build | build logs and artifacts |
| Release Agent | Play Console prep, notes, testing | release checklist and store drafts |
| Proof Agent | independent verification | pass/fail report and blockers |
| Security/Connector Agent | MCP, secrets, permissions | connector register and risk review |

## Connector and MCP Stack

Use connectors only when they reduce manual work or improve evidence quality.

| Connector/MCP | Use | Gate |
|---|---|---|
| GitHub | repo, issues, PRs, branch, code review | write allowed after repo confirmed |
| Web Search | trends, competitor, policy checks | cite important claims |
| File/Library | project docs, templates, uploaded files | read-only unless user asks edits |
| Unity Editor Script | scenes, settings, assets, inspector refs | local editor execution by user or trusted runner |
| Playwright/browser | visual checks, web forms, screenshots | no credential automation unless approved |
| Figma/design | UI mockups, icons, store art | asset license review required |
| Google Play Developer API | internal tracks, metadata prep | no production rollout without human approval |
| Railway/Firebase/Supabase | backend, remote config, leaderboard | only after backend decision gate |
| Analytics/Crash | quality monitoring | privacy/Data Safety update required |

## Security and Human Approval Rules

Never automate these without explicit human approval and proof review:

- Google Play production rollout.
- Signing key or keystore creation/rotation/transfer.
- Billing, ads account, payment profile, tax, identity verification.
- Final Data Safety and content rating declarations.
- Production backend secrets or credentials.
- Use of copyrighted brands, characters, music, or copied UI.

Use `Docs/MCP_CONNECTOR_REGISTER.md` for each connected tool:

```markdown
| Tool | Purpose | Permission | Secrets used? | Human approval needed? | Risk | Notes |
|---|---|---:|---:|---:|---:|---|
```

## Stage Gates

Each gate must produce a clear decision: Pass, Conditional Pass, Fail.

| Gate | Entry condition | Proof required |
|---|---|---|
| G0 Keyword Intake | user gives keyword or idea | scope, mode, target platform |
| G1 Market/IP | research complete | sources, risks, go/no-go |
| G2 Design | concept selected | design brief, scorecard, MVP cutline |
| G3 Architecture | engine and repo chosen | stack decision, folder plan, package policy |
| G4 Scene Automation | project scaffold ready | SceneBaker proof, Project Doctor proof |
| G5 Feature Slice | core loop playable | deterministic tests, screenshots/logs |
| G6 Build | Android build candidate | AAB/APK proof, device smoke test |
| G7 Store Prep | release materials ready | metadata, screenshots, policy draft |
| G8 Human Approval | all blockers closed | final review checklist |
| G9 Launch/Growth | test track/live release done | release notes, feedback loop |

## Factory Artifacts

When running AI Game Factory, create or update these documents as appropriate:

```text
Docs/FACTORY_CONTROL_PLANE.md
Docs/KEYWORD_INTAKE.md
Docs/GAME_SCOPE_DECISION.md
Docs/SCOPE_PACK_ROUTING.md
Docs/TREND_MARKET_RESEARCH.md
Docs/RESEARCH_SOURCES.md
Docs/CONCEPT_SCORECARD.md
Docs/IP_LICENSE_RISK_REVIEW.md
Docs/STACK_DECISION.md
Docs/AI_AGENT_PLAN.md
Docs/AGENT_OWNERSHIP_MATRIX.md
Docs/MCP_CONNECTOR_REGISTER.md
Docs/UNITY_AUTOMATION_PROFILE.md
Docs/SCENEBAKER_RECIPE.md
Docs/SCENE_BAKER_PROOF.md
Docs/PROJECT_DOCTOR_REPORT.md
Docs/TEST_HARNESS_PLAN.md
Docs/VERIFICATION_PROOF_MATRIX.md
Docs/STAGE_GATE_REPORT.md
Docs/BUILD_PROOF.md
Docs/PLAY_CONSOLE_AUTOMATION_PLAN.md
Docs/RELEASE_EVIDENCE.md
Docs/GROWTH_LOOP.md
```

## Repository Blueprint

Use this repo layout for a Unity-focused factory project:

```text
/
  Docs/
  UnityProject/
    Assets/
      Editor/AIProjectFactory/
      Scripts/Core/
      Scripts/Gameplay/
      Scripts/Tests/
      ScriptableObjects/
      Scenes/
      Art/Generated/
      Audio/Generated/
    ProjectSettings/
    Packages/
  .github/
    workflows/
    ISSUE_TEMPLATE/
    pull_request_template.md
  tools/
    proof/
    release/
  README.md
```

For Godot or another engine, keep the same `Docs/`, `.github/`, and `tools/` structure but replace `UnityProject/` with the engine-specific project.

## Factory Prompts

### Factory Orchestrator Prompt

```text
You are the AI Game Factory Orchestrator.
Input: [keyword or game idea]
Goal: route the idea from keyword intake to a verified Google Play release candidate.

Decide:
1. Game scope: prototype / small / mid-size / big / commercial launch.
2. Factory mode: Lite / Standard / Pro / Studio.
3. Engine and stack decision gate.
4. Required agents and file ownership.
5. Stage gates and proof requirements.
6. Human approval gates.

Output:
- Docs/FACTORY_CONTROL_PLANE.md
- Docs/KEYWORD_INTAKE.md
- Docs/SCOPE_PACK_ROUTING.md
- Docs/AI_AGENT_PLAN.md
- Docs/STAGE_GATE_REPORT.md
```

### Proof Agent Prompt

```text
You are the independent Proof Agent.
Do not accept claims without evidence.

Review:
- Changed files
- Build logs
- Unity Console status
- SceneBaker proof
- Project Doctor result
- Test harness output
- Android build proof
- License/IP register
- Store/Play Console checklist

Return only:
Pass / Conditional Pass / Fail
Blockers:
Evidence accepted:
Evidence missing:
Next required fix:
```

## Upgrade Rules

Upgrade from Skill-only to AI Game Factory when any of these are true:

- The user wants keyword-to-launch automation.
- Multiple agents or tools must coordinate.
- Unity Editor state must be generated or verified.
- GitHub, CI, assets, and Play Store prep must be connected.
- The game is commercial, mid-size, big, or repeated across multiple games.

Stay skill-only when the user only wants ideas, a plan, or a one-off document.
