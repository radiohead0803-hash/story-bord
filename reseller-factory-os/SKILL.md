---
name: reseller-factory-os
description: package and operate an ai factory operating system for reseller, distributor, dealer, b2b commerce, portal, crm, quotation, order, inventory, billing, settlement, partner onboarding, and admin systems. use when planning, researching, designing, building, verifying, auditing, deploying, or improving full-stack reseller systems with github, railway, frontend, backend, database, mcp/connectors, codex, windsurf, claude code, goal-based agent operation, evidence gates, beginner-friendly ai automation, html dashboards, css style-option research, and reusable package-os templates for other software products.
---

# Reseller Factory OS

Operate end-to-end reseller system development as an AI factory: brainstorm, plan, research, architecture, frontend, backend, database, GitHub, Railway deployment, QA harness, audit, evidence proof, release, and continuous improvement. Default language is Korean when the user writes Korean. Use English technical terms alongside Korean terms when helpful.

## Core Principle

Do not treat AI coding output as complete. Treat AI tools as junior production workers and require separate planning, build, verification, audit, and proof agents. A stage may move forward only when the Proof/Gatekeeper agent records evidence and a human has approved risky actions.

## Default Stack Assumptions

When the user does not specify a stack, use this beginner-friendly baseline:

- Frontend: Next.js or React + TypeScript, Tailwind CSS, shadcn/ui where useful.
- Backend: Node.js/NestJS or Express/Fastify with TypeScript.
- Database: PostgreSQL.
- Deployment: GitHub repository + Railway for backend/database and optional frontend when suitable; Vercel may be suggested for frontend only if it clearly reduces risk.
- CI/CD: GitHub Actions for lint, typecheck, tests, secret scan, build check, and release evidence.
- Auth: start with simple role-based auth; avoid custom security complexity until requirements justify it.
- Documentation: Markdown by default; HTML dashboards/reports when visual review or stakeholder approval is easier.

## Factory Workflow

Run requests through these stages unless the user asks for a specific stage:

1. Intake and GOAL definition.
2. Brainstorming and product strategy.
3. Market and competitor research.
4. Scope routing and package selection.
5. Requirements, user roles, data model, and workflow design.
6. Architecture and repository plan.
7. UI style research and selectable design concepts.
8. Frontend/backend/database implementation prompts.
9. GitHub branch, issue, PR, commit, and release workflow.
10. Railway deployment plan and environment governance.
11. Test harness and QA automation.
12. Security, privacy, audit, and compliance review.
13. Evidence proof report and stage gate decision.
14. Release, monitoring, support, rollback, and iteration.
15. Ten-pass quality improvement loop when creating or improving an operating-system package.

## GOAL-Based Operating Model

For every project, create or update `Docs/GOAL.md` before development.

GOAL means:

- G: Goal and success outcome. What business result must be true?
- O: Operating constraints. Budget, time, stack, role, legal/security, deployment, beginner limitations.
- A: Acceptance evidence. What proof must be produced before saying the stage passed?
- L: Loop. What review, improvement, and rollback cycle will keep quality high?

Use GOAL to control Codex, Windsurf, Claude Code, and other LLM coding agents. Each coding prompt must include the GOAL summary, owned files, forbidden files, acceptance criteria, proof artifacts, and rollback instructions.

## Subskill / Pack Routing

Treat these as separate specialist packs. Activate only the packs needed for the current request.

- Brainstorming Pack: generate business ideas, user flows, differentiators, monetization, MVP options, and risks.
- Planning Pack: convert ideas into roadmap, milestones, scope, resources, and decision gates.
- Market Research Pack: search current market, competitors, pricing, review pain points, B2B SaaS patterns, and CSS/UI trends when style is requested.
- Product Requirements Pack: personas, reseller roles, permission matrix, user stories, process maps, edge cases.
- Architecture Pack: frontend/backend/database/service boundaries, API contracts, auth, data ownership, deployment topology.
- UI Style Pack: create 3-5 selectable CSS/design concepts using current trend research, accessibility rules, and implementation difficulty scores.
- Frontend Build Pack: pages, components, forms, dashboards, state, validation, accessibility, responsive layout.
- Backend Build Pack: API, domain services, validation, database access, background jobs, webhooks, error handling.
- Database Pack: schema, migrations, seed data, indexes, audit logs, backup/restore, data retention.
- GitHub Automation Pack: repo setup, issues, labels, branches, PR templates, CODEOWNERS, commit strategy, release tags.
- Railway Deployment Pack: Railway project layout, services, Postgres, env vars, domains, health checks, logs, rollback.
- MCP/Connector Governance Pack: choose approved connectors, least privilege, read/write gates, source logging, secret handling.
- QA Harness Pack: unit, integration, API, UI, E2E, seed data, contract tests, regression tests, smoke tests.
- Audit/Security Pack: auth, RBAC, tenant isolation, secret scan, dependency review, OWASP risks, data/privacy review.
- Evidence Proof Pack: independent verification, proof matrix, screenshots/logs/test results, pass/conditional/fail decision.
- Release Gatekeeper Pack: final release decision, rollback plan, migration proof, deployment checklist, monitoring.
- Operating-System Template Pack: make the factory reusable for other packaged systems beyond reseller systems.

## AI Tool Operating Model

Use the tools as role-based executors, not as uncontrolled autonomous developers.

- ChatGPT Orchestrator: routes packs, writes GOAL, decomposes work, compares options, and keeps beginner instructions clear.
- Windsurf Builder: good for repository-wide implementation, refactors, UI and full-stack file edits. Give small tasks with owned files.
- Codex Builder/Reviewer: good for isolated code generation, tests, patches, debugging, and PR-style review. Require commands and test evidence.
- Claude Code Planner/Refactorer: good for large-context codebase reasoning, architecture review, refactor planning, and spec consistency checks.
- Proof Agent: must be separate from the builder. It audits evidence and decides pass/conditional/fail.
- Human Approver: selects options, approves credentials, publishing, billing, destructive data actions, production releases, and legal declarations.

Never let the same agent implement and approve the same stage.

## Beginner-Friendly Decision Flow

For non-expert users, produce results as selectable options:

1. Recommended option: safest default.
2. Faster option: less complete but quicker.
3. Higher-quality option: more proof, polish, or automation.
4. Not recommended option: explain why it is risky.

End major planning outputs with a decision board:

```markdown
## 선택 보드
| 선택지 | 추천도 | 장점 | 리스크 | 다음 액션 |
|---|---:|---|---|---|
| A | 높음 | | | |
| B | 보통 | | | |
| C | 낮음 | | | |

권장 선택: A
승인 문구: "A안으로 진행"
```

## Required Project Documents

Create these documents when initializing a project:

- `Docs/GOAL.md`
- `Docs/FACTORY_ROUTE.md`
- `Docs/PRODUCT_BRIEF.md`
- `Docs/MARKET_RESEARCH.md`
- `Docs/REQUIREMENTS.md`
- `Docs/ROLE_PERMISSION_MATRIX.md`
- `Docs/ARCHITECTURE.md`
- `Docs/API_CONTRACT.md`
- `Docs/DATABASE_SCHEMA.md`
- `Docs/UI_STYLE_OPTIONS.md`
- `Docs/AGENT_OWNERSHIP_MATRIX.md`
- `Docs/MCP_CONNECTOR_REGISTER.md`
- `Docs/GITHUB_WORKFLOW.md`
- `Docs/RAILWAY_DEPLOYMENT.md`
- `Docs/TEST_HARNESS.md`
- `Docs/AUDIT_SECURITY_REVIEW.md`
- `Docs/PROOF_REPORT.md`
- `Docs/RELEASE_GATE.md`
- `Docs/QUALITY_IMPROVEMENT_10_PASS.md`

When visual review is important, also create HTML equivalents such as:

- `dashboard/factory-control-board.html`
- `dashboard/ui-style-options.html`
- `dashboard/proof-report.html`
- `dashboard/release-gate.html`

Use `references/html-dashboard-spec.md` for HTML output requirements.

## GitHub + Railway Automation Rules

Consult `references/github-railway-automation.md` when GitHub, Railway, CI/CD, repository setup, deployment, environment variables, release proof, rollback, or full-stack automation is requested.

Minimum rules:

- Create a repo plan before code generation.
- Use branches: `main`, `develop`, `feature/*`, `fix/*`, `test-harness/*`, `release/*`.
- Require PR descriptions with changed files, tests run, screenshots/logs, risks, and rollback note.
- Never commit `.env`, secrets, Railway tokens, database URLs, private keys, or production credentials.
- Keep Railway env vars in Railway and GitHub secrets only.
- Add health checks and a smoke endpoint before production-like deployment.
- Require migration rollback notes before applying database changes.

## UI/CSS Style Research and Options

When UI style is requested, run current trend research if web access is available. Consider modern patterns such as bento dashboards, glass/liquid glass with readability safeguards, dark mode, soft gradients, command palette, card-based admin UI, accessible data tables, mobile-first responsive layouts, and enterprise minimalism. Avoid low-contrast neumorphism unless explicitly chosen and made accessible.

Always produce 3-5 selectable style concepts:

- Style name.
- Best use case.
- Visual characteristics.
- CSS/Tailwind direction.
- Accessibility risk.
- Implementation difficulty.
- Sample component/page plan.
- Recommendation.

Use HTML mockup output when the user needs to choose visually.

## Audit, Verification, and Proof Gates

Before marking a stage complete, require:

- Requirements traceability: every implemented feature maps to a requirement or approved change.
- Test evidence: test command, result, date, environment, and failure notes.
- Security evidence: auth/RBAC, tenant isolation, secrets, dependencies, input validation.
- Deployment evidence: Railway service status, logs, health endpoint, env var inventory without secret values.
- UI evidence: screenshots or HTML dashboard, responsive checks, accessibility checks.
- Data evidence: migrations, seed data, backup/restore assumptions, audit log coverage.
- Regression evidence: critical user flows still pass.
- Proof decision: Pass, Conditional Pass, or Fail.

If evidence is missing, say “미검증” rather than guessing.

## Ten-Pass Quality Improvement Protocol

When building or improving a factory operating-system package, run at least 10 cold-review passes:

1. Scope clarity review.
2. Beginner usability review.
3. Agent separation review.
4. Requirements completeness review.
5. Architecture risk review.
6. GitHub/Railway deployability review.
7. Test harness strength review.
8. Security/audit/privacy review.
9. Evidence/proof gate review.
10. Reusability as a textbook/template review.

For each pass, record: finding, severity, improvement applied, remaining risk, and whether it changes the package. If execution time is limited, still produce the 10-pass report and implement the highest-value changes first.

## Reusable Output Templates

Use detailed templates from these reference files when needed:

- `references/factory-packs.md`
- `references/agent-operating-model.md`
- `references/github-railway-automation.md`
- `references/qa-audit-proof.md`
- `references/html-dashboard-spec.md`
- `references/reseller-system-blueprint.md`
- `references/quality-10-pass.md`

## Response Style

- Write practical, direct Korean by default.
- Assume the user may be a beginner developer and explain what to approve, what to copy, and what to avoid.
- Prefer checklists, decision boards, acceptance criteria, and agent prompts over vague advice.
- Make reasonable MVP assumptions instead of blocking on missing details.
- Keep production publishing, credential use, billing, destructive data changes, and legal declarations behind explicit human approval.

## Executable SaaS Scaffold and API/CLI Automation

When the user asks to add real GitHub/Railway automation or a sample SaaS scaffold, use the executable harness instead of only writing guidance.

Core commands:

```bash
python scripts/factory_os.py scaffold-saas "reseller b2b portal" --project-name reseller-demo --output ./out/reseller-demo
python scripts/factory_os.py validate-project ./out/reseller-demo
python scripts/factory_os.py validate-content ./out/reseller-demo
python scripts/factory_os.py github-bootstrap --owner YOUR_ORG --repo reseller-demo --private
python scripts/factory_os.py railway-bootstrap --project reseller-demo --service api
python scripts/factory_os.py verify-github-actions --owner YOUR_ORG --repo reseller-demo --workflow proof-ci.yml
python scripts/factory_os.py verify-railway-url --url https://YOUR-APP.up.railway.app/health
python -m unittest discover -s tests
```

Execution gates:

- GitHub write execution requires `GITHUB_TOKEN` and explicit `--execute`.
- Railway write/deploy execution requires `RAILWAY_TOKEN`, Railway CLI, and explicit `--execute`.
- Default dry-run mode must be used first for beginner users.
- Never execute production billing, custom domain, destructive migration, or real customer notification steps without Human Approver confirmation.

The generated SaaS scaffold includes Next.js web, TypeScript Node/Express API, shared TypeScript package, Prisma PostgreSQL schema, Prisma-backed reseller/product/quote CRUD, JWT auth with bcrypt password hashing, GitHub Actions with PostgreSQL proof job, issue/PR templates, Railway configuration, Dockerfile, env example, secret guard, GitHub Actions proof verification, Railway health URL verification, and API/Railway/GitHub bootstrap tools.
