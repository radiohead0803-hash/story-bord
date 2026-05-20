# Keyword-to-Google-Play AI Stack

Use this reference when the user wants a higher-quality game that can move from a short keyword to automated development, verification, and Google Play release preparation.

## Goal

Convert a keyword such as `cozy dice board game`, `puzzle board game`, or `idle board adventure` into a controlled AI production pipeline:

1. Trend-aware research
2. Original concept generation
3. IP/license gate
4. Game design and monetization plan
5. Engine and automation profile selection
6. Unity project/repo scaffolding
7. SceneBaker generation
8. Agent-based implementation
9. Test harness and proof collection
10. Build, store asset, and Google Play release preparation
11. Post-launch iteration and live-ops decisions

Do not promise fully unattended publishing. Google Play Console account verification, payments profile, identity checks, signing credentials, content rating, policy declarations, and final submit-to-review actions often require a human owner. Automate preparation and evidence; keep final publication gate human-approved unless the user explicitly provides an approved publishing integration and wants that action.

## Recommended Connectors and Tools

### Must-have for production workflow

| Connector / tool | Purpose | Required guardrail |
|---|---|---|
| GitHub connector | Create/read repo, issues, PRs, commits, release tags, code review | Never commit secrets, keystore, service account JSON, or Play signing credentials |
| Web search | Trend research, competitor research, current Google Play policy, SDK policy, pricing | Cite sources and record search date in `Docs/RESEARCH_SOURCES.md` |
| File/library access | Read uploaded concepts, art briefs, legal notes, previous skill zips | Avoid assuming missing file contents |
| Unity Editor scripts | SceneBaker, Project Doctor, build settings, test harness, screenshot capture | Idempotent and safe to rerun |
| GitHub Actions or CI substitute | Docs validation, secret scan, tests, optional Unity build | Keep Unity license/secrets out of repo |
| Google Play Console / Developer API integration | Internal-track upload, release metadata, testing track automation | Human approval gate before production rollout |

### Strongly recommended for higher-quality games

| Connector / MCP / service | Use case | Notes |
|---|---|---|
| Figma MCP or design connector | UI layout, icon/screenshot design handoff | Prefer official/trusted MCP only; third-party MCP must pass security review |
| Playwright/browser automation MCP | Store listing preview, policy page capture, web QA, landing page tests | Use read-only mode by default for external sites |
| Asset/source registry | Track art, audio, fonts, prompts, licenses, attributions | Required before using generated or third-party content |
| Crash/analytics source | Play Console Android Vitals, Firebase Crashlytics, or privacy-light equivalent | Add only after SDK/privacy review |
| Translation/localization source | Korean/English strings, store copy variants, review replies | Keep app strings separate from code |
| Backend connector | Railway/Firebase/Supabase only when leaderboard, remote config, receipt validation, or live ops are needed | Default no backend for offline MVP |

### Optional only when justified

| Option | Use only when | Reason to defer |
|---|---|---|
| Remote config backend | Frequent balancing/events are required | Adds privacy, network, QA, and backend risk |
| Leaderboard | Competitive loop is central | Requires anti-cheat and account/privacy review |
| IAP receipt validation | Paid products are in v1 | Adds server and Google Play Billing compliance complexity |
| Addressables/CDN | Large downloadable content exists | Overkill for small board-game MVP |

## MCP Security Gate

MCP can connect AI agents to design tools, repos, browsers, docs, and build systems, but it also increases attack surface. Apply this gate before recommending an MCP:

1. Prefer official, maintained, read-only-capable MCP servers.
2. Check last update, maintainer trust, install source, and required permissions.
3. Avoid MCPs that execute shell commands from untrusted input.
4. Run least-privilege: read-only for research/design; write access only for repo automation or controlled internal tools.
5. Do not pass secrets through prompts or MCP context.
6. Record approved MCPs in `Docs/MCP_CONNECTOR_REGISTER.md`.
7. Require human approval before enabling publishing, billing, credentials, or production rollout actions.

## Keyword-to-Launch Routing

When the user provides only a keyword, route through this sequence:

1. **Keyword intake**
   - Extract genre, theme, audience, monetization, difficulty, and platform assumptions.
   - If unclear, choose a conservative MVP and state assumptions.

2. **Trend and competitor search**
   - Use web search for current trend signals, comparable games, monetization patterns, review complaints, and policy risks.
   - Use GitHub/open-source search for implementation examples and automation patterns.
   - Record sources in `Docs/RESEARCH_SOURCES.md`.

3. **Concept generation and scoring**
   - Generate 3-5 original concepts.
   - Score by market fit, build difficulty, novelty, monetization fit, IP risk, and testability.
   - Select one MVP; defer the rest.

4. **Production stack selection**
   - Decide Unity/Godot/other engine.
   - If Unity: choose game-type profile and SceneBaker recipe.
   - Decide if backend is needed; default no.

5. **Automation scaffold**
   - Create/recommend GitHub repo, branch model, issue set, docs, PR template, proof log, license inventory, SDK/privacy register.
   - Generate Unity project structure and Editor scripts.

6. **Parallel agent build lanes**
   - Run design, Unity core, SceneBaker, UI, data/save, test harness, store asset, and verification agents in parallel with file ownership rules.
   - Verification agents do not write production feature code.

7. **Proof and release gates**
   - Each milestone must produce proof: compile logs, harness output, screenshot, device smoke result, privacy review, release evidence.
   - No Google Play internal test readiness unless Stage Gate says Pass or approved Conditional Pass.

## Recommended New Packs to Add

Add these packs when the user wants stronger automation beyond the current skill:

- **Keyword-to-Launch Orchestrator Pack**: converts one keyword into the full research/design/build/release plan and active pack set.
- **Connector and MCP Governance Pack**: recommends, approves, records, and restricts connectors/MCPs.
- **Play Console Automation Pack**: prepares internal testing upload, listing metadata, release notes, data safety draft, and tester instructions; keeps production submission human-approved.
- **Creative Asset Generation Governance Pack**: manages generated art/audio/UI assets with prompt logs, style rules, license inventory, and no imitation of living artists, copyrighted characters, or franchise styles.
- **Quality Upgrade Pack**: adds polish loops: feel tuning, animation, sound, UX onboarding, retention, screenshot appeal, accessibility, and device performance.
- **Experiment and LiveOps Pack**: post-launch experiments, remote config decision, review mining, update roadmap, and balance changes.

## Required Documents

Generate or update these when running keyword-to-launch automation:

- `Docs/KEYWORD_INTAKE.md`
- `Docs/TREND_MARKET_RESEARCH.md`
- `Docs/RESEARCH_SOURCES.md`
- `Docs/CONCEPT_SCORECARD.md`
- `Docs/STACK_DECISION.md`
- `Docs/MCP_CONNECTOR_REGISTER.md`
- `Docs/AI_AGENT_PLAN.md`
- `Docs/ASSET_GENERATION_REGISTER.md`
- `Docs/PLAY_CONSOLE_AUTOMATION_PLAN.md`
- `Docs/STAGE_GATE_REPORT.md`
- `Docs/RELEASE_EVIDENCE.md`

## Play Console Automation Boundary

Automate preparation as much as possible:

- AAB artifact record
- package/version checklist
- internal testing checklist
- tester instructions
- store listing text
- screenshot plan
- privacy policy draft
- data safety draft
- content rating inputs
- release notes

Keep these as human-approved gates:

- Google Play developer identity and payments setup
- app signing key ownership
- service account creation and permissions
- final Data Safety declaration
- content rating submission
- production rollout submission
- any paid product/IAP setup

## Higher-Quality Game Checklist

A higher-quality keyword-generated game must pass these before Play testing:

- Original concept selected through research and IP gate
- Game feel checklist completed: feedback, timing, animation, sound, reward clarity
- Onboarding teaches the first turn in under 30 seconds
- Test harness covers core loop, economy, save/load, scene flow, and device smoke
- Store screenshots are generated from real scenes or clearly marked mockups
- SDK/privacy register matches actual project dependencies
- License inventory covers every external/generated asset
- Low-end Android performance target is defined and tested
- Verification agent independently approves evidence

## Output Template

```markdown
# Keyword-to-Launch Automation Recommendation

## Keyword

## Assumptions

## Active Packs
| Pack | Why active | Proof required |
|---|---|---|

## Recommended Connectors / MCPs
| Connector/MCP | Use | Permission level | Risk | Gate |
|---|---|---:|---:|---|

## Deferred Integrations
| Item | Why deferred | When to revisit |
|---|---|---|

## Automation Roadmap
1. Research
2. Concept
3. Stack decision
4. Repo/project scaffold
5. SceneBaker
6. Implementation agents
7. Verification agents
8. Build/release prep
9. Play Console human approval

## Required Documents

## Stage Gate Criteria
```
