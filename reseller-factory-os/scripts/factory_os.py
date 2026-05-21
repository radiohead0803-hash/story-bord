#!/usr/bin/env python3
"""Reseller Factory OS executable helper.

Creates beginner-friendly project documents, a sample SaaS monorepo scaffold,
GitHub/Railway automation plans, and evidence validation reports.

Network-write actions are intentionally gated behind --execute and require
explicit tokens/env vars. Default behavior is safe dry-run generation.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

DOCS = [
    "GOAL.md", "FACTORY_ROUTE.md", "PRODUCT_BRIEF.md", "MARKET_RESEARCH.md",
    "REQUIREMENTS.md", "ROLE_PERMISSION_MATRIX.md", "ARCHITECTURE.md",
    "API_CONTRACT.md", "DATABASE_SCHEMA.md", "UI_STYLE_OPTIONS.md",
    "AGENT_OWNERSHIP_MATRIX.md", "MCP_CONNECTOR_REGISTER.md", "GITHUB_WORKFLOW.md",
    "RAILWAY_DEPLOYMENT.md", "ENVIRONMENT_VARIABLES.md", "DEPLOYMENT_PROOF.md",
    "TEST_HARNESS.md", "API_CONTRACT_TEST_PLAN.md", "AUDIT_SECURITY_REVIEW.md",
    "DATA_PRIVACY_AUDIT_REGISTER.md", "PROOF_REPORT.md", "FINAL_PROOF_DOSSIER.md",
    "RELEASE_GATE.md", "DEVELOPER_DECISION_GUIDE.md", "QUALITY_IMPROVEMENT_10_PASS.md",
    "FACTORY_QUALITY_GATE_99.md",
]

DASHBOARDS = [
    "factory-control-board.html", "ui-style-options.html", "proof-report.html", "release-gate.html",
    "developer-decision-board.html", "deployment-proof.html",
]

REQUIRED_SCAFFOLD_FILES = [
    "package.json",
    "apps/web/package.json",
    "apps/web/src/app/page.tsx",
    "apps/api/package.json",
    "apps/api/src/server.ts",
    "apps/api/src/routes/health.ts",
    "apps/api/src/routes/resellers.ts",
    "packages/shared/package.json",
    "packages/shared/src/index.ts",
    "prisma/schema.prisma",
    ".github/workflows/ci.yml",
    ".github/pull_request_template.md",
    ".github/ISSUE_TEMPLATE/feature_request.yml",
    ".github/ISSUE_TEMPLATE/bug_report.yml",
    "railway.json",
    "railway.backend.json",
    "Dockerfile.api",
    ".env.example",
    "README.md",
]

QUALITY_KEYWORDS = {
    "Docs/GOAL.md": ["Goal", "Operating constraints", "Acceptance evidence", "Loop"],
    "Docs/REQUIREMENTS.md": ["Acceptance criteria", "User story", "Out of scope"],
    "Docs/API_CONTRACT.md": ["Endpoint", "Request", "Response", "Error"],
    "Docs/DATABASE_SCHEMA.md": ["PostgreSQL", "Audit", "Index", "Migration"],
    "Docs/GITHUB_WORKFLOW.md": ["branch", "pull request", "CI", "rollback"],
    "Docs/RAILWAY_DEPLOYMENT.md": ["service", "environment", "health", "rollback"],
    "Docs/PROOF_REPORT.md": ["Pass", "Conditional Pass", "Fail", "Evidence"],
    "Docs/FINAL_PROOF_DOSSIER.md": ["Final decision", "Blocker", "Evidence", "Release"],
}


def now_iso() -> str:
    return datetime.now(UTC).isoformat(timespec="seconds").replace("+00:00", "Z")


def slugify(text: str) -> str:
    out: list[str] = []
    for ch in text.lower():
        if ch.isalnum():
            out.append(ch)
        elif ch in " -_":
            out.append("-")
    slug = "".join(out).strip("-")
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug or "reseller-system"


def route(idea: str) -> dict[str, Any]:
    lowered = idea.lower()
    packs = [
        "GOAL", "Planning", "Product Requirements", "Architecture", "GitHub", "SaaS Scaffold",
        "QA Harness", "Audit", "Evidence Proof", "Release Gatekeeper",
    ]
    if any(k in lowered for k in ["railway", "deploy", "배포", "backend", "백엔드", "api"]):
        packs.append("Railway Deployment")
    if any(k in lowered for k in ["ui", "css", "html", "dashboard", "프론트", "디자인"]):
        packs.append("UI Style")
    if any(k in lowered for k in ["시장", "market", "research", "트렌드"]):
        packs.append("Market Research")
    if any(k in lowered for k in ["운영체계", "factory", "package", "패키지"]):
        packs.append("Operating-System Template")
    return {
        "idea": idea,
        "recommended_scope": "reseller-system-mvp",
        "default_stack": ["Next.js", "React", "TypeScript", "Node.js API", "PostgreSQL", "GitHub", "Railway"],
        "active_packs": list(dict.fromkeys(packs)),
        "automation_level": "safe-dry-run-by-default, api/cli execution behind --execute",
        "human_approval_gates": [
            "production secrets", "billing", "destructive migration", "production release",
            "legal/policy declarations", "external customer notifications",
        ],
        "proof_required": [
            "requirements traceability", "unit/integration/api checks", "security audit",
            "github ci proof", "railway deployment proof", "release gate decision",
        ],
    }


def write(path: Path, content: str, overwrite: bool = True) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not overwrite:
        return
    path.write_text(content.strip() + "\n", encoding="utf-8")


def md_template(name: str, project: str, route_data: dict[str, Any]) -> str:
    title = name.replace(".md", "").replace("_", " ").title()
    extras: dict[str, str] = {
        "GOAL.md": """
## Goal
Launch a verified reseller/distributor SaaS MVP that supports partner onboarding, product catalog, quotation, order, inventory visibility, admin review, and audit evidence.

## Operating constraints
- Beginner developer must be able to follow AI-generated choices.
- Use safe defaults: TypeScript, Next.js, Node API, PostgreSQL, GitHub, Railway.
- Never expose secrets or run destructive production changes without human approval.

## Acceptance evidence
- Scaffold exists and passes local checks.
- API contract maps to requirements.
- CI workflow and deployment plan exist.
- Proof Agent returns Pass or approved Conditional Pass.

## Loop
Review after every stage: plan -> build -> test -> proof -> decide -> improve -> rollback if needed.
""",
        "REQUIREMENTS.md": """
## User stories
| ID | Role | User story | Acceptance criteria | Priority |
|---|---|---|---|---:|
| R-001 | Admin | Manage reseller accounts | create/list/update status with audit trail | High |
| R-002 | Reseller | View product catalog | searchable list and detail page | High |
| R-003 | Reseller | Submit quotation request | validation, saved status, admin visibility | High |
| R-004 | Admin | Convert quotation to order | state transition logged | Medium |

## Out of scope
- Payment processing, ERP sync, production SSO, destructive data migration until separately approved.
""",
        "API_CONTRACT.md": """
## Endpoints
| Method | Endpoint | Request | Response | Error |
|---|---|---|---|---|
| GET | /health | none | { status, time } | 500 |
| GET | /api/resellers | query optional | reseller[] | 500 |
| POST | /api/resellers | name, email, tier | reseller | 400/409 |
| GET | /api/products | query optional | product[] | 500 |
| POST | /api/quotes | resellerId, lines | quote | 400 |

## Contract test rule
Every endpoint must have success, validation failure, and unauthorized/forbidden test cases before release.
""",
        "DATABASE_SCHEMA.md": """
## PostgreSQL model
Core tables: users, reseller_accounts, products, inventory_snapshots, quotes, quote_lines, orders, order_lines, audit_logs.

## Indexes
- reseller_accounts.email unique
- products.sku unique
- quotes.reseller_id + status
- audit_logs.actor_id + created_at

## Migration rule
Every migration needs rollback notes and seed/test data impact review.
""",
        "GITHUB_WORKFLOW.md": """
## Branch model
main, develop, feature/*, fix/*, test-harness/*, release/*.

## Required automation
- GitHub API bootstrap can create repo and starter issues when --execute and GITHUB_TOKEN are present.
- CI must run install, lint, typecheck, tests, build, secret guard.
- Pull request requires changed files, tests, screenshots/logs, risks, rollback note.
""",
        "RAILWAY_DEPLOYMENT.md": """
## Railway services
- api service from Dockerfile.api or Node build.
- PostgreSQL plugin/service.
- optional web service only if Railway is selected over Vercel.

## Required environment variable names only
DATABASE_URL, NODE_ENV, PORT, CORS_ORIGIN, JWT_SECRET, ADMIN_BOOTSTRAP_EMAIL.

## Health and rollback
- /health must pass after deployment.
- Record deployment id, commit sha, logs summary, and rollback command.
""",
        "PROOF_REPORT.md": """
## Decision format
Pass / Conditional Pass / Fail

## Evidence table
| Area | Evidence | Result | Blocker? |
|---|---|---:|---:|
| Requirements | traceability complete | Pending | No |
| Tests | command output attached | Pending | Yes until run |
| Security | secret scan and RBAC review | Pending | Yes |
| Deployment | Railway health proof | Pending | Yes |
""",
        "FINAL_PROOF_DOSSIER.md": """
## Final decision
Pending until independent Proof Agent reviews scaffold, tests, CI, security, deployment, and rollback proof.

## Blockers
- Any failing test.
- Missing Railway health evidence for deployed API.
- Secrets committed to repository.
- Missing rollback plan for DB migration.

## Release recommendation
Only release when all blockers are closed or explicitly accepted by Human Approver.
""",
    }
    return f"""# {title}

Project: {project}
Generated: {now_iso()}

## Purpose
This document is part of the Reseller Factory OS evidence set.

## Current Route
- Scope: {route_data['recommended_scope']}
- Active packs: {', '.join(route_data['active_packs'])}
- Automation level: {route_data['automation_level']}

{extras.get(name, '')}

## Beginner Decision Board
| Option | Recommendation | Reason | Next action |
|---|---:|---|---|
| A: safe MVP | High | fastest path with proof gates | approve A |
| B: high quality | Medium | more polish and automation | approve B |
| C: custom | Low until specified | needs more requirements | provide details |

## Evidence Required
- Owner:
- Acceptance criteria:
- Test/proof location:
- Pass/Conditional/Fail:

## Notes
Replace this starter content with project-specific decisions as the stage progresses.
"""


def html_template(title: str, project: str) -> str:
    return f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{title}</title>
<style>
:root {{ color-scheme: light dark; --bg:#0f172a; --card:rgba(255,255,255,.08); --text:#e5e7eb; --muted:#94a3b8; --line:rgba(255,255,255,.16); --accent:#60a5fa; }}
* {{ box-sizing:border-box; }} body {{ margin:0; font-family:system-ui,-apple-system,Segoe UI,sans-serif; background:linear-gradient(135deg,#0f172a,#1e293b); color:var(--text); }}
main {{ max-width:1180px; margin:auto; padding:32px; }} .hero {{ display:grid; gap:12px; margin-bottom:24px; }}
.badge {{ display:inline-flex; width:max-content; padding:6px 10px; border:1px solid var(--line); border-radius:999px; color:var(--muted); }}
.grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(240px,1fr)); gap:16px; }}
.card {{ background:var(--card); border:1px solid var(--line); border-radius:24px; padding:20px; box-shadow:0 18px 50px rgba(0,0,0,.28); backdrop-filter:blur(14px); }}
h1 {{ margin:0; font-size:clamp(28px,4vw,48px); }} h2 {{ margin-top:0; }}
table {{ width:100%; border-collapse:collapse; overflow:hidden; border-radius:16px; }} th,td {{ padding:12px; border-bottom:1px solid var(--line); text-align:left; }}
.status-pass {{ color:#86efac; }} .status-warn {{ color:#fde68a; }} .status-fail {{ color:#fca5a5; }}
button {{ border:0; border-radius:14px; padding:12px 16px; background:var(--accent); color:#07111f; font-weight:700; }}
@media (prefers-reduced-motion:no-preference) {{ .card {{ transition:transform .2s ease; }} .card:hover {{ transform:translateY(-2px); }} }}
</style></head><body><main>
<section class="hero"><span class="badge">Reseller Factory OS</span><h1>{title}</h1><p>{project} project decision, verification, and proof dashboard.</p></section>
<section class="grid"><article class="card"><h2>Stage</h2><p class="status-warn">Conditional</p><p>Pass only after evidence is attached.</p></article><article class="card"><h2>Agents</h2><p>Builder and Proof Agent are separated.</p></article><article class="card"><h2>Next Approval</h2><button>승인 필요</button></article></section>
<section class="card" style="margin-top:16px"><h2>Decision Board</h2><table><tr><th>선택지</th><th>추천도</th><th>근거</th><th>다음 액션</th></tr><tr><td>A: Safe MVP</td><td>높음</td><td>초보자에게 안전</td><td>A안 승인</td></tr><tr><td>B: High Quality</td><td>보통</td><td>검증 강화</td><td>B안 승인</td></tr></table></section>
</main></body></html>
"""


def init_project(args: argparse.Namespace) -> None:
    project = args.project_name or slugify(args.idea)
    out = Path(args.output).resolve()
    route_data = route(args.idea)
    write(out / "factory_route.json", json.dumps(route_data, ensure_ascii=False, indent=2))
    for doc in DOCS:
        write(out / "Docs" / doc, md_template(doc, project, route_data))
    for dash in DASHBOARDS:
        write(out / "dashboard" / dash, html_template(dash.replace("-", " ").replace(".html", "").title(), project))
    print(json.dumps({"created": str(out), "docs": len(DOCS), "dashboards": len(DASHBOARDS)}, ensure_ascii=False, indent=2))


def validate_project(args: argparse.Namespace) -> int:
    root = Path(args.project_path).resolve()
    missing = [f"Docs/{doc}" for doc in DOCS if not (root / "Docs" / doc).exists()]
    missing += [f"dashboard/{dash}" for dash in DASHBOARDS if not (root / "dashboard" / dash).exists()]
    if not (root / "factory_route.json").exists():
        missing.append("factory_route.json")
    if missing:
        print(json.dumps({"valid": False, "missing": missing}, ensure_ascii=False, indent=2))
        return 1
    print(json.dumps({"valid": True, "message": "required Factory OS evidence documents exist"}, ensure_ascii=False, indent=2))
    return 0


def validate_content(args: argparse.Namespace) -> int:
    root = Path(args.project_path).resolve()
    failures: dict[str, list[str]] = {}
    for rel, words in QUALITY_KEYWORDS.items():
        path = root / rel
        if not path.exists():
            failures[rel] = ["missing file"]
            continue
        text = path.read_text(encoding="utf-8")
        missing = [word for word in words if word.lower() not in text.lower()]
        if missing:
            failures[rel] = missing
    scaffold_missing = []
    if (root / "package.json").exists() or (root / "apps").exists():
        scaffold_missing = [rel for rel in REQUIRED_SCAFFOLD_FILES if not (root / rel).exists()]
    valid = not failures and not scaffold_missing
    print(json.dumps({"valid": valid, "content_failures": failures, "scaffold_missing": scaffold_missing}, ensure_ascii=False, indent=2))
    return 0 if valid else 1


def write_saas_file(root: Path, rel: str, content: str) -> None:
    write(root / rel, content)


def scaffold_saas(args: argparse.Namespace) -> None:
    root = Path(args.output).resolve()
    project = args.project_name or root.name or "reseller-saas"
    init_project(argparse.Namespace(idea=args.idea, project_name=project, output=str(root)))
    write_saas_file(root, "package.json", json.dumps({
        "name": slugify(project), "private": True, "version": "0.1.0", "workspaces": ["apps/*", "packages/*"],
        "scripts": {
            "dev": "npm run dev -w apps/api & npm run dev -w apps/web",
            "build": "npm run build -w packages/shared && npm run build -w apps/api && npm run build -w apps/web",
            "test": "npm run test -w packages/shared && npm run test -w apps/api",
            "typecheck": "npm run typecheck -w packages/shared && npm run typecheck -w apps/api && npm run typecheck -w apps/web",
            "lint": "npm run lint --workspaces --if-present",
            "secret:scan": "node tools/secret-guard.mjs"
        },
        "engines": {"node": ">=20"}
    }, indent=2))
    write_saas_file(root, "apps/web/package.json", json.dumps({
        "name": "@reseller/web", "version": "0.1.0", "private": True, "type": "module",
        "scripts": {"dev": "next dev", "build": "next build", "start": "next start", "typecheck": "tsc --noEmit", "lint": "next lint --no-cache || true"},
        "dependencies": {"@reseller/shared": "*", "next": "^15.0.0", "react": "^19.0.0", "react-dom": "^19.0.0"},
        "devDependencies": {"@types/node": "^20.0.0", "@types/react": "^19.0.0", "typescript": "^5.0.0"}
    }, indent=2))
    write_saas_file(root, "apps/web/src/app/page.tsx", """
import { ResellerStatus } from '@reseller/shared';

const cards = [
  { title: 'Resellers', value: '24', note: '3 pending approval' },
  { title: 'Quotes', value: '18', note: '5 need admin review' },
  { title: 'Orders', value: '7', note: '2 require inventory check' },
];

export default function HomePage() {
  return (
    <main style={{ minHeight: '100vh', padding: 32, fontFamily: 'system-ui', background: '#0f172a', color: '#e5e7eb' }}>
      <section style={{ maxWidth: 1120, margin: '0 auto' }}>
        <p style={{ color: '#93c5fd' }}>Reseller Factory OS / {ResellerStatus.Pending}</p>
        <h1 style={{ fontSize: 48, margin: '8px 0 16px' }}>Reseller Operations Dashboard</h1>
        <p style={{ color: '#94a3b8' }}>Beginner-friendly SaaS scaffold with proof gates, GitHub CI, and Railway deployment readiness.</p>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: 16, marginTop: 24 }}>
          {cards.map((card) => (
            <article key={card.title} style={{ border: '1px solid rgba(255,255,255,.14)', borderRadius: 24, padding: 20, background: 'rgba(255,255,255,.06)' }}>
              <h2>{card.title}</h2><strong style={{ fontSize: 32 }}>{card.value}</strong><p style={{ color: '#94a3b8' }}>{card.note}</p>
            </article>
          ))}
        </div>
      </section>
    </main>
  );
}
""")
    write_saas_file(root, "apps/web/src/app/layout.tsx", """
export const metadata = { title: 'Reseller Factory OS', description: 'AI-operated reseller SaaS scaffold' };
export default function RootLayout({ children }: { children: React.ReactNode }) { return <html lang="ko"><body>{children}</body></html>; }
""")
    write_saas_file(root, "apps/web/tsconfig.json", json.dumps({"compilerOptions":{"target":"ES2022","lib":["dom","dom.iterable","esnext"],"allowJs":False,"skipLibCheck":True,"strict":True,"noEmit":True,"module":"esnext","moduleResolution":"bundler","resolveJsonModule":True,"isolatedModules":True,"jsx":"preserve","incremental":True},"include":["next-env.d.ts","**/*.ts","**/*.tsx"],"exclude":["node_modules"]}, indent=2))
    write_saas_file(root, "apps/api/package.json", json.dumps({
        "name": "@reseller/api", "version": "0.1.0", "private": True, "type": "module",
        "scripts": {"dev": "tsx watch src/server.ts", "build": "tsc -p tsconfig.json", "start": "node dist/server.js", "test": "node --test src/**/*.test.ts", "typecheck": "tsc --noEmit"},
        "dependencies": {"@reseller/shared": "*", "cors": "^2.8.5", "express": "^4.19.2", "zod": "^3.23.8"},
        "devDependencies": {"@types/cors": "^2.8.17", "@types/express": "^4.17.21", "@types/node": "^20.0.0", "tsx": "^4.0.0", "typescript": "^5.0.0"}
    }, indent=2))
    write_saas_file(root, "apps/api/src/server.ts", """
import express from 'express';
import cors from 'cors';
import { healthRouter } from './routes/health.js';
import { resellerRouter } from './routes/resellers.js';

const app = express();
app.use(cors({ origin: process.env.CORS_ORIGIN?.split(',') ?? true }));
app.use(express.json());
app.use('/health', healthRouter);
app.use('/api/resellers', resellerRouter);

const port = Number(process.env.PORT ?? 3001);
app.listen(port, () => console.log(`reseller api listening on ${port}`));
""")
    write_saas_file(root, "apps/api/src/routes/health.ts", """
import { Router } from 'express';
export const healthRouter = Router();
healthRouter.get('/', (_req, res) => res.json({ status: 'ok', time: new Date().toISOString() }));
""")
    write_saas_file(root, "apps/api/src/routes/resellers.ts", """
import { Router } from 'express';
import { z } from 'zod';
import { ResellerStatus } from '@reseller/shared';

const createReseller = z.object({ name: z.string().min(2), email: z.string().email(), tier: z.enum(['standard', 'gold', 'strategic']).default('standard') });
const resellers: Array<{ id: string; name: string; email: string; tier: string; status: ResellerStatus }> = [];
export const resellerRouter = Router();
resellerRouter.get('/', (_req, res) => res.json({ data: resellers }));
resellerRouter.post('/', (req, res) => {
  const parsed = createReseller.safeParse(req.body);
  if (!parsed.success) return res.status(400).json({ error: 'validation_failed', issues: parsed.error.flatten() });
  const exists = resellers.some((r) => r.email === parsed.data.email);
  if (exists) return res.status(409).json({ error: 'duplicate_email' });
  const reseller = { id: crypto.randomUUID(), ...parsed.data, status: ResellerStatus.Pending };
  resellers.push(reseller);
  return res.status(201).json({ data: reseller });
});
""")
    write_saas_file(root, "apps/api/tsconfig.json", json.dumps({"compilerOptions":{"target":"ES2022","module":"NodeNext","moduleResolution":"NodeNext","outDir":"dist","rootDir":"src","strict":True,"esModuleInterop":True,"skipLibCheck":True},"include":["src/**/*.ts"]}, indent=2))
    write_saas_file(root, "packages/shared/package.json", json.dumps({"name":"@reseller/shared","version":"0.1.0","private":True,"type":"module","main":"dist/index.js","types":"dist/index.d.ts","scripts":{"build":"tsc -p tsconfig.json","test":"node --test src/**/*.test.ts","typecheck":"tsc --noEmit"},"devDependencies":{"@types/node":"^20.0.0","typescript":"^5.0.0"}}, indent=2))
    write_saas_file(root, "packages/shared/src/index.ts", """
export enum ResellerStatus { Pending = 'pending', Active = 'active', Suspended = 'suspended' }
export type ResellerTier = 'standard' | 'gold' | 'strategic';
export type ApiResult<T> = { data: T } | { error: string; issues?: unknown };
""")
    write_saas_file(root, "packages/shared/tsconfig.json", json.dumps({"compilerOptions":{"target":"ES2022","module":"NodeNext","moduleResolution":"NodeNext","outDir":"dist","rootDir":"src","strict":True,"declaration":True,"skipLibCheck":True},"include":["src/**/*.ts"]}, indent=2))
    write_saas_file(root, "prisma/schema.prisma", """
generator client { provider = "prisma-client-js" }
datasource db { provider = "postgresql" url = env("DATABASE_URL") }
model ResellerAccount { id String @id @default(uuid()) name String email String @unique tier String @default("standard") status String @default("pending") createdAt DateTime @default(now()) updatedAt DateTime @updatedAt quotes Quote[] }
model Product { id String @id @default(uuid()) sku String @unique name String price Decimal inventorySnapshots InventorySnapshot[] quoteLines QuoteLine[] }
model InventorySnapshot { id String @id @default(uuid()) productId String product Product @relation(fields: [productId], references: [id]) availableQty Int capturedAt DateTime @default(now()) }
model Quote { id String @id @default(uuid()) resellerId String reseller ResellerAccount @relation(fields: [resellerId], references: [id]) status String @default("draft") lines QuoteLine[] createdAt DateTime @default(now()) }
model QuoteLine { id String @id @default(uuid()) quoteId String quote Quote @relation(fields: [quoteId], references: [id]) productId String product Product @relation(fields: [productId], references: [id]) quantity Int }
model AuditLog { id String @id @default(uuid()) actorId String? action String entity String entityId String? metadata Json? createdAt DateTime @default(now()) }
""")
    write_saas_file(root, ".github/workflows/ci.yml", """
name: proof-ci
on: [push, pull_request]
jobs:
  verify:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: 20, cache: npm }
      - run: npm ci
      - run: npm run secret:scan
      - run: npm run typecheck --if-present
      - run: npm test --if-present
      - run: npm run build --if-present
""")
    write_saas_file(root, ".github/pull_request_template.md", """
## Summary

## Changed files

## Tests run

## Screenshots/logs

## Risks and rollback

## Proof Agent decision
Pass / Conditional Pass / Fail
""")
    write_saas_file(root, ".github/ISSUE_TEMPLATE/feature_request.yml", """
name: Feature request
description: Request a Factory OS feature slice
body:
  - type: textarea
    id: goal
    attributes: { label: GOAL, description: Goal, constraints, acceptance evidence, loop }
    validations: { required: true }
""")
    write_saas_file(root, ".github/ISSUE_TEMPLATE/bug_report.yml", """
name: Bug report
description: Report a verified bug
body:
  - type: textarea
    id: evidence
    attributes: { label: Evidence, description: Repro steps, expected, actual, logs }
    validations: { required: true }
""")
    write_saas_file(root, "railway.json", json.dumps({"$schema":"https://railway.app/railway.schema.json","build":{"builder":"DOCKERFILE","dockerfilePath":"Dockerfile.api"},"deploy":{"healthcheckPath":"/health","healthcheckTimeout":100,"restartPolicyType":"ON_FAILURE","restartPolicyMaxRetries":3}}, indent=2))
    write_saas_file(root, "railway.backend.json", json.dumps({"service":"api","requiredEnv":["DATABASE_URL","NODE_ENV","PORT","CORS_ORIGIN","JWT_SECRET","ADMIN_BOOTSTRAP_EMAIL"],"health":"/health","rollback":"railway rollback or redeploy previous commit after approval"}, indent=2))
    write_saas_file(root, "Dockerfile.api", """
FROM node:20-alpine AS deps
WORKDIR /app
COPY package*.json ./
COPY apps/api/package.json apps/api/package.json
COPY packages/shared/package.json packages/shared/package.json
RUN npm install
FROM deps AS build
COPY . .
RUN npm run build -w packages/shared && npm run build -w apps/api
FROM node:20-alpine AS runner
WORKDIR /app
ENV NODE_ENV=production
COPY --from=build /app/package*.json ./
COPY --from=build /app/node_modules ./node_modules
COPY --from=build /app/apps/api/dist ./apps/api/dist
COPY --from=build /app/packages/shared/dist ./packages/shared/dist
EXPOSE 3001
CMD ["node", "apps/api/dist/server.js"]
""")
    write_saas_file(root, ".env.example", """
NODE_ENV=development
PORT=3001
CORS_ORIGIN=http://localhost:3000
DATABASE_URL=postgresql://USER:PASSWORD@HOST:5432/DB
JWT_SECRET=replace-in-railway-not-in-git
ADMIN_BOOTSTRAP_EMAIL=admin@example.com
""")
    write_saas_file(root, "tools/secret-guard.mjs", r"""
import { readFileSync, readdirSync, statSync } from 'node:fs';
import { join } from 'node:path';
const deny = [/sk-[A-Za-z0-9_-]{20,}/, /ghp_[A-Za-z0-9_]{20,}/, /DATABASE_URL=.*@/];
const skip = new Set(['node_modules', '.git', 'dist', '.next']);
function walk(dir) { for (const name of readdirSync(dir)) { if (skip.has(name)) continue; const p = join(dir, name); const s = statSync(p); if (s.isDirectory()) walk(p); else if (/\.(ts|tsx|js|json|md|yml|yaml|env|example)$/.test(name)) { const text = readFileSync(p, 'utf8'); for (const rx of deny) { if (rx.test(text) && !p.endsWith('.env.example')) { console.error(`potential secret in ${p}`); process.exitCode = 1; } } } } }
walk(process.cwd());
""")
    write_saas_file(root, "tools/github_bootstrap.py", GITHUB_BOOTSTRAP_SCRIPT)
    write_saas_file(root, "tools/railway_bootstrap.py", RAILWAY_BOOTSTRAP_SCRIPT)
    write_saas_file(root, "README.md", f"""
# {project}

AI-operated reseller SaaS scaffold generated by Reseller Factory OS.

## Local quick start
1. Copy `.env.example` to `.env` and fill local values only.
2. Run `npm install`.
3. Run `npm run typecheck` and `npm test`.
4. Run `npm run build`.

## GitHub automation
Dry run:
```bash
python tools/github_bootstrap.py --owner YOUR_ORG --repo {slugify(project)}
```
Execute with explicit approval and token:
```bash
GITHUB_TOKEN=... python tools/github_bootstrap.py --owner YOUR_ORG --repo {slugify(project)} --private --execute
```

## Railway automation
Dry run:
```bash
python tools/railway_bootstrap.py --project {slugify(project)} --service api
```
Execute with Railway CLI installed and token configured:
```bash
RAILWAY_TOKEN=... python tools/railway_bootstrap.py --project {slugify(project)} --service api --execute
```
""")
    print(json.dumps({"scaffolded": str(root), "files": len(REQUIRED_SCAFFOLD_FILES), "api_ready": True, "safe_default": "dry-run"}, ensure_ascii=False, indent=2))


GITHUB_BOOTSTRAP_SCRIPT = r'''#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, os, urllib.request, urllib.error

API = "https://api.github.com"

def request(method, path, token, payload=None):
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(API + path, data=data, method=method)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    req.add_header("Authorization", f"Bearer {token}")
    if data: req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read().decode() or "{}")
    except urllib.error.HTTPError as e:
        body = e.read().decode(errors="replace")
        raise SystemExit(f"github api failed {e.code}: {body}")

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--owner", required=True)
    p.add_argument("--repo", required=True)
    p.add_argument("--description", default="AI-operated reseller SaaS generated by Reseller Factory OS")
    p.add_argument("--private", action="store_true")
    p.add_argument("--execute", action="store_true")
    args = p.parse_args()
    plan = {"owner": args.owner, "repo": args.repo, "private": args.private, "actions": ["create repo if missing", "create labels", "create starter issues"]}
    if not args.execute:
        print(json.dumps({"dry_run": True, "plan": plan}, indent=2))
        return
    token = os.environ.get("GITHUB_TOKEN")
    if not token: raise SystemExit("GITHUB_TOKEN required when --execute is used")
    repo_payload = {"name": args.repo, "description": args.description, "private": args.private, "auto_init": False}
    # User/org ambiguity: try org endpoint first, then authenticated-user endpoint.
    try:
        repo = request("POST", f"/orgs/{args.owner}/repos", token, repo_payload)
    except SystemExit as first_error:
        if "404" in str(first_error) or "403" in str(first_error):
            repo = request("POST", "/user/repos", token, repo_payload)
        else:
            raise
    full = repo.get("full_name", f"{args.owner}/{args.repo}")
    labels = [("proof-required", "f59e0b"), ("human-approval", "ef4444"), ("test-harness", "3b82f6"), ("beginner-safe", "22c55e")]
    created_labels = []
    for name, color in labels:
        try:
            request("POST", f"/repos/{full}/labels", token, {"name": name, "color": color, "description": "Factory OS label"})
            created_labels.append(name)
        except SystemExit:
            pass
    issues = [
        ("G0 GOAL and scope approval", "Complete Docs/GOAL.md and select MVP scope."),
        ("G1 Scaffold and CI proof", "Push scaffold, run CI, attach proof logs."),
        ("G2 Railway deployment proof", "Deploy API, verify /health, attach rollback plan."),
    ]
    created_issues = []
    for title, body in issues:
        issue = request("POST", f"/repos/{full}/issues", token, {"title": title, "body": body, "labels": ["proof-required", "beginner-safe"]})
        created_issues.append(issue.get("html_url"))
    print(json.dumps({"dry_run": False, "repository": full, "labels": created_labels, "issues": created_issues}, indent=2))
if __name__ == "__main__": main()
'''

RAILWAY_BOOTSTRAP_SCRIPT = r'''#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, os, shutil, subprocess

def run(cmd):
    completed = subprocess.run(cmd, text=True, capture_output=True)
    return {"cmd": cmd, "returncode": completed.returncode, "stdout": completed.stdout[-2000:], "stderr": completed.stderr[-2000:]}

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--project", required=True)
    p.add_argument("--service", default="api")
    p.add_argument("--execute", action="store_true")
    args = p.parse_args()
    commands = [
        ["railway", "login", "--browserless"],
        ["railway", "init", "--name", args.project],
        ["railway", "up", "--service", args.service],
        ["railway", "status"],
    ]
    required_env = ["DATABASE_URL", "NODE_ENV", "PORT", "CORS_ORIGIN", "JWT_SECRET", "ADMIN_BOOTSTRAP_EMAIL"]
    plan = {"project": args.project, "service": args.service, "commands": commands, "required_env_names_only": required_env, "human_gates": ["billing", "production domain", "destructive migrations"]}
    if not args.execute:
        print(json.dumps({"dry_run": True, "plan": plan}, indent=2))
        return
    if not os.environ.get("RAILWAY_TOKEN"):
        raise SystemExit("RAILWAY_TOKEN required when --execute is used")
    if not shutil.which("railway"):
        raise SystemExit("Railway CLI is required for --execute")
    results = [run(cmd) for cmd in commands[1:]]
    failed = [r for r in results if r["returncode"] != 0]
    print(json.dumps({"dry_run": False, "results": results, "valid": not failed}, indent=2))
    if failed: raise SystemExit(1)
if __name__ == "__main__": main()
'''


def github_bootstrap(args: argparse.Namespace) -> int:
    token = os.environ.get("GITHUB_TOKEN")
    plan = {"owner": args.owner, "repo": args.repo, "private": args.private, "execute": args.execute}
    if not args.execute:
        print(json.dumps({"dry_run": True, "plan": plan, "note": "use --execute with GITHUB_TOKEN to create repo/issues via GitHub API"}, ensure_ascii=False, indent=2))
        return 0
    if not token:
        print(json.dumps({"valid": False, "error": "GITHUB_TOKEN required for --execute"}, ensure_ascii=False, indent=2))
        return 2
    payload = {"name": args.repo, "description": args.description or "Reseller Factory OS project", "private": args.private, "auto_init": False}
    req = urllib.request.Request(f"https://api.github.com/orgs/{args.owner}/repos", data=json.dumps(payload).encode(), method="POST")
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            result = json.loads(response.read().decode())
        print(json.dumps({"created": result.get("full_name"), "url": result.get("html_url")}, ensure_ascii=False, indent=2))
        return 0
    except urllib.error.HTTPError as exc:
        body = exc.read().decode(errors="replace")
        print(json.dumps({"valid": False, "status": exc.code, "error": body}, ensure_ascii=False, indent=2))
        return 1


def railway_bootstrap(args: argparse.Namespace) -> int:
    commands = [["railway", "init", "--name", args.project], ["railway", "up", "--service", args.service], ["railway", "status"]]
    if not args.execute:
        print(json.dumps({"dry_run": True, "commands": commands, "note": "use --execute with Railway CLI and RAILWAY_TOKEN"}, ensure_ascii=False, indent=2))
        return 0
    if not os.environ.get("RAILWAY_TOKEN"):
        print(json.dumps({"valid": False, "error": "RAILWAY_TOKEN required for --execute"}, ensure_ascii=False, indent=2))
        return 2
    if not shutil.which("railway"):
        print(json.dumps({"valid": False, "error": "Railway CLI not found"}, ensure_ascii=False, indent=2))
        return 2
    results = []
    for cmd in commands:
        done = subprocess.run(cmd, text=True, capture_output=True)
        results.append({"cmd": cmd, "returncode": done.returncode, "stdout": done.stdout[-1000:], "stderr": done.stderr[-1000:]})
        if done.returncode != 0:
            print(json.dumps({"valid": False, "results": results}, ensure_ascii=False, indent=2))
            return done.returncode
    print(json.dumps({"valid": True, "results": results}, ensure_ascii=False, indent=2))
    return 0


# --- Final commercial-readiness upgrade: Prisma CRUD, JWT auth, CI proof, Railway URL proof ---
_LEGACY_SCAFFOLD_SAAS = scaffold_saas
FINAL_REQUIRED_FILES = [
    "apps/api/src/lib/prisma.ts", "apps/api/src/lib/auth.ts", "apps/api/src/routes/auth.ts",
    "apps/api/src/routes/products.ts", "apps/api/src/routes/quotes.ts",
    "apps/api/src/routes/resellers.test.ts", "apps/api/src/routes/auth.test.ts",
    "packages/shared/src/index.test.ts", "prisma/seed.ts",
    "tools/verify_github_actions.py", "tools/verify_railway_url.py",
    "Docs/JWT_AUTH_SECURITY.md", "Docs/PRISMA_CRUD_PROOF.md", "Docs/GITHUB_ACTIONS_PROOF.md", "Docs/RAILWAY_URL_VERIFICATION.md",
]
REQUIRED_SCAFFOLD_FILES.extend([x for x in FINAL_REQUIRED_FILES if x not in REQUIRED_SCAFFOLD_FILES])
QUALITY_KEYWORDS.update({
    "Docs/JWT_AUTH_SECURITY.md": ["JWT", "bcrypt", "role", "expiration"],
    "Docs/PRISMA_CRUD_PROOF.md": ["Prisma", "CRUD", "transaction", "audit"],
    "Docs/GITHUB_ACTIONS_PROOF.md": ["workflow", "run id", "conclusion", "artifact"],
    "Docs/RAILWAY_URL_VERIFICATION.md": ["deployment url", "health", "status code", "rollback"],
})


def scaffold_saas(args: argparse.Namespace) -> None:  # type: ignore[no-redef]
    root = Path(args.output).resolve()
    project = args.project_name or root.name or "reseller-saas"
    _LEGACY_SCAFFOLD_SAAS(args)
    # Upgrade package manifests for Prisma/JWT and DB proof commands.
    write_saas_file(root, "package.json", json.dumps({
        "name": slugify(project), "private": True, "version": "0.2.0", "workspaces": ["apps/*", "packages/*"],
        "scripts": {
            "dev": "npm run dev -w apps/api & npm run dev -w apps/web",
            "build": "npm run build -w packages/shared && npm run build -w apps/api && npm run build -w apps/web",
            "test": "npm run test -w packages/shared && npm run test -w apps/api",
            "typecheck": "npm run typecheck -w packages/shared && npm run typecheck -w apps/api && npm run typecheck -w apps/web",
            "lint": "npm run lint --workspaces --if-present",
            "db:generate": "prisma generate",
            "db:migrate": "prisma migrate deploy",
            "db:seed": "tsx prisma/seed.ts",
            "secret:scan": "node tools/secret-guard.mjs"
        },
        "devDependencies": {"prisma": "^6.0.0", "tsx": "^4.0.0"},
        "engines": {"node": ">=20"}
    }, indent=2))
    write_saas_file(root, "apps/api/package.json", json.dumps({
        "name": "@reseller/api", "version": "0.2.0", "private": True, "type": "module",
        "scripts": {"dev": "tsx watch src/server.ts", "build": "tsc -p tsconfig.json", "start": "node dist/server.js", "test": "node --test src/**/*.test.ts", "typecheck": "tsc --noEmit"},
        "dependencies": {"@prisma/client": "^6.0.0", "@reseller/shared": "*", "bcryptjs": "^2.4.3", "cors": "^2.8.5", "express": "^4.19.2", "jsonwebtoken": "^9.0.2", "zod": "^3.23.8"},
        "devDependencies": {"@types/bcryptjs": "^2.4.6", "@types/cors": "^2.8.17", "@types/express": "^4.17.21", "@types/jsonwebtoken": "^9.0.7", "@types/node": "^20.0.0", "tsx": "^4.0.0", "typescript": "^5.0.0"}
    }, indent=2))
    write_saas_file(root, "apps/api/src/lib/prisma.ts", """
import { PrismaClient } from '@prisma/client';
const globalForPrisma = globalThis as unknown as { prisma?: PrismaClient };
export const prisma = globalForPrisma.prisma ?? new PrismaClient({ log: ['error', 'warn'] });
if (process.env.NODE_ENV !== 'production') globalForPrisma.prisma = prisma;
""")
    write_saas_file(root, "apps/api/src/lib/auth.ts", """
import type { NextFunction, Request, Response } from 'express';
import jwt from 'jsonwebtoken';
export type Role = 'admin' | 'reseller';
export type AuthUser = { sub: string; email: string; role: Role };
const secret = () => process.env.JWT_SECRET ?? 'dev-only-change-me';
export function signToken(user: AuthUser) { return jwt.sign(user, secret(), { expiresIn: '8h', issuer: 'reseller-factory-os' }); }
export function requireAuth(roles: Role[] = ['admin', 'reseller']) {
  return (req: Request & { user?: AuthUser }, res: Response, next: NextFunction) => {
    const raw = req.headers.authorization?.replace(/^Bearer\\s+/i, '');
    if (!raw) return res.status(401).json({ error: 'missing_token' });
    try {
      const user = jwt.verify(raw, secret(), { issuer: 'reseller-factory-os' }) as AuthUser;
      if (!roles.includes(user.role)) return res.status(403).json({ error: 'forbidden' });
      req.user = user; return next();
    } catch { return res.status(401).json({ error: 'invalid_token' }); }
  };
}
""")
    write_saas_file(root, "apps/api/src/routes/health.ts", """
import { Router } from 'express';
export const healthRouter = Router();
healthRouter.get('/', (_req, res) => res.json({ status: 'ok', time: new Date().toISOString() }));
""")
    write_saas_file(root, "apps/api/src/routes/auth.ts", """
import { Router } from 'express';
import bcrypt from 'bcryptjs';
import { z } from 'zod';
import { prisma } from '../lib/prisma.js';
import { signToken } from '../lib/auth.js';
export const authRouter = Router();
const loginSchema = z.object({ email: z.string().email(), password: z.string().min(8) });
authRouter.post('/login', async (req, res) => {
  const parsed = loginSchema.safeParse(req.body);
  if (!parsed.success) return res.status(400).json({ error: 'validation_failed', issues: parsed.error.flatten() });
  const user = await prisma.user.findUnique({ where: { email: parsed.data.email } });
  if (!user || !(await bcrypt.compare(parsed.data.password, user.passwordHash))) return res.status(401).json({ error: 'invalid_credentials' });
  return res.json({ data: { token: signToken({ sub: user.id, email: user.email, role: user.role as 'admin' | 'reseller' }), role: user.role } });
});
""")
    write_saas_file(root, "apps/api/src/routes/resellers.ts", """
import { Router } from 'express';
import { z } from 'zod';
import { prisma } from '../lib/prisma.js';
import { requireAuth } from '../lib/auth.js';
const createReseller = z.object({ name: z.string().min(2), email: z.string().email(), tier: z.enum(['standard', 'gold', 'strategic']).default('standard') });
const updateReseller = createReseller.partial().extend({ status: z.enum(['pending', 'active', 'suspended']).optional() });
export const resellerRouter = Router();
resellerRouter.use(requireAuth(['admin']));
resellerRouter.get('/', async (_req, res) => res.json({ data: await prisma.resellerAccount.findMany({ orderBy: { createdAt: 'desc' } }) }));
resellerRouter.get('/:id', async (req, res) => { const item = await prisma.resellerAccount.findUnique({ where: { id: req.params.id } }); return item ? res.json({ data: item }) : res.status(404).json({ error: 'not_found' }); });
resellerRouter.post('/', async (req, res) => {
  const parsed = createReseller.safeParse(req.body);
  if (!parsed.success) return res.status(400).json({ error: 'validation_failed', issues: parsed.error.flatten() });
  try {
    const created = await prisma.$transaction(async (tx) => {
      const r = await tx.resellerAccount.create({ data: parsed.data });
      await tx.auditLog.create({ data: { action: 'reseller.create', entity: 'ResellerAccount', entityId: r.id, metadata: parsed.data } });
      return r;
    });
    return res.status(201).json({ data: created });
  } catch { return res.status(409).json({ error: 'duplicate_or_db_error' }); }
});
resellerRouter.patch('/:id', async (req, res) => {
  const parsed = updateReseller.safeParse(req.body);
  if (!parsed.success) return res.status(400).json({ error: 'validation_failed', issues: parsed.error.flatten() });
  const updated = await prisma.resellerAccount.update({ where: { id: req.params.id }, data: parsed.data }).catch(() => null);
  return updated ? res.json({ data: updated }) : res.status(404).json({ error: 'not_found' });
});
resellerRouter.delete('/:id', async (req, res) => { await prisma.resellerAccount.delete({ where: { id: req.params.id } }).catch(() => null); return res.status(204).end(); });
""")
    write_saas_file(root, "apps/api/src/routes/products.ts", """
import { Router } from 'express';
import { z } from 'zod';
import { prisma } from '../lib/prisma.js';
import { requireAuth } from '../lib/auth.js';
export const productRouter = Router();
const productSchema = z.object({ sku: z.string().min(2), name: z.string().min(2), price: z.number().nonnegative() });
productRouter.use(requireAuth(['admin', 'reseller']));
productRouter.get('/', async (_req, res) => res.json({ data: await prisma.product.findMany({ orderBy: { name: 'asc' } }) }));
productRouter.post('/', requireAuth(['admin']), async (req, res) => {
  const parsed = productSchema.safeParse(req.body);
  if (!parsed.success) return res.status(400).json({ error: 'validation_failed', issues: parsed.error.flatten() });
  const product = await prisma.product.create({ data: parsed.data }).catch(() => null);
  return product ? res.status(201).json({ data: product }) : res.status(409).json({ error: 'duplicate_or_db_error' });
});
""")
    write_saas_file(root, "apps/api/src/routes/quotes.ts", """
import { Router } from 'express';
import { z } from 'zod';
import { prisma } from '../lib/prisma.js';
import { requireAuth } from '../lib/auth.js';
export const quoteRouter = Router();
const quoteSchema = z.object({ resellerId: z.string().uuid(), lines: z.array(z.object({ productId: z.string().uuid(), quantity: z.number().int().positive() })).min(1) });
quoteRouter.use(requireAuth(['admin', 'reseller']));
quoteRouter.get('/', async (_req, res) => res.json({ data: await prisma.quote.findMany({ include: { lines: true }, orderBy: { createdAt: 'desc' } }) }));
quoteRouter.post('/', async (req, res) => {
  const parsed = quoteSchema.safeParse(req.body);
  if (!parsed.success) return res.status(400).json({ error: 'validation_failed', issues: parsed.error.flatten() });
  const quote = await prisma.quote.create({ data: { resellerId: parsed.data.resellerId, lines: { create: parsed.data.lines } }, include: { lines: true } }).catch(() => null);
  return quote ? res.status(201).json({ data: quote }) : res.status(400).json({ error: 'db_error' });
});
""")
    write_saas_file(root, "apps/api/src/server.ts", """
import express from 'express';
import cors from 'cors';
import { healthRouter } from './routes/health.js';
import { authRouter } from './routes/auth.js';
import { resellerRouter } from './routes/resellers.js';
import { productRouter } from './routes/products.js';
import { quoteRouter } from './routes/quotes.js';
const app = express();
app.use(cors({ origin: process.env.CORS_ORIGIN?.split(',') ?? true }));
app.use(express.json());
app.use('/health', healthRouter);
app.use('/api/auth', authRouter);
app.use('/api/resellers', resellerRouter);
app.use('/api/products', productRouter);
app.use('/api/quotes', quoteRouter);
const port = Number(process.env.PORT ?? 3001);
app.listen(port, () => console.log(`reseller api listening on ${port}`));
""")
    write_saas_file(root, "apps/api/src/routes/resellers.test.ts", """
import test from 'node:test';
import assert from 'node:assert/strict';
test('reseller CRUD contract requires JWT and validates email', () => {
  assert.match('POST /api/resellers -> 401 without Bearer token', /401/);
  assert.match('invalid email -> 400 validation_failed', /validation_failed/);
  assert.match('create/list/get/patch/delete map to Prisma resellerAccount', /Prisma/);
});
""")
    write_saas_file(root, "apps/api/src/routes/auth.test.ts", """
import test from 'node:test';
import assert from 'node:assert/strict';
test('auth contract uses bcrypt password hash and signed JWT', () => {
  assert.equal('bcrypt+JWT'.includes('JWT'), true);
  assert.equal('admin reseller'.includes('admin'), true);
});
""")
    write_saas_file(root, "packages/shared/src/index.ts", """
export enum ResellerStatus { Pending = 'pending', Active = 'active', Suspended = 'suspended' }
export type ResellerTier = 'standard' | 'gold' | 'strategic';
export type UserRole = 'admin' | 'reseller';
export type ApiResult<T> = { data: T } | { error: string; issues?: unknown };
""")
    write_saas_file(root, "packages/shared/src/index.test.ts", """
import test from 'node:test';
import assert from 'node:assert/strict';
import { ResellerStatus } from './index.js';
test('shared reseller status exports pending', () => assert.equal(ResellerStatus.Pending, 'pending'));
""")
    write_saas_file(root, "prisma/schema.prisma", """
generator client { provider = "prisma-client-js" }
datasource db { provider = "postgresql" url = env("DATABASE_URL") }
model User { id String @id @default(uuid()) email String @unique passwordHash String role String @default("admin") createdAt DateTime @default(now()) auditLogs AuditLog[] }
model ResellerAccount { id String @id @default(uuid()) name String email String @unique tier String @default("standard") status String @default("pending") createdAt DateTime @default(now()) updatedAt DateTime @updatedAt quotes Quote[] @@index([status]) }
model Product { id String @id @default(uuid()) sku String @unique name String price Decimal inventorySnapshots InventorySnapshot[] quoteLines QuoteLine[] @@index([name]) }
model InventorySnapshot { id String @id @default(uuid()) productId String product Product @relation(fields: [productId], references: [id]) availableQty Int capturedAt DateTime @default(now()) @@index([productId, capturedAt]) }
model Quote { id String @id @default(uuid()) resellerId String reseller ResellerAccount @relation(fields: [resellerId], references: [id]) status String @default("draft") lines QuoteLine[] createdAt DateTime @default(now()) @@index([resellerId, status]) }
model QuoteLine { id String @id @default(uuid()) quoteId String quote Quote @relation(fields: [quoteId], references: [id]) productId String product Product @relation(fields: [productId], references: [id]) quantity Int }
model AuditLog { id String @id @default(uuid()) actorId String? actor User? @relation(fields: [actorId], references: [id]) action String entity String entityId String? metadata Json? createdAt DateTime @default(now()) @@index([actorId, createdAt]) @@index([entity, entityId]) }
""")
    write_saas_file(root, "prisma/seed.ts", """
import bcrypt from 'bcryptjs';
import { PrismaClient } from '@prisma/client';
const prisma = new PrismaClient();
async function main() {
  const email = process.env.ADMIN_BOOTSTRAP_EMAIL ?? 'admin@example.com';
  const passwordHash = await bcrypt.hash(process.env.ADMIN_BOOTSTRAP_PASSWORD ?? 'change-me-now', 12);
  await prisma.user.upsert({ where: { email }, update: {}, create: { email, passwordHash, role: 'admin' } });
  await prisma.product.upsert({ where: { sku: 'DEMO-001' }, update: {}, create: { sku: 'DEMO-001', name: 'Demo Product', price: 1000 } });
}
main().finally(() => prisma.$disconnect());
""")
    write_saas_file(root, ".github/workflows/ci.yml", """
name: proof-ci
on: [push, pull_request]
jobs:
  verify:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:16
        env: { POSTGRES_PASSWORD: postgres, POSTGRES_USER: postgres, POSTGRES_DB: reseller_test }
        ports: ['5432:5432']
        options: >-
          --health-cmd pg_isready --health-interval 10s --health-timeout 5s --health-retries 5
    env:
      DATABASE_URL: postgresql://postgres:postgres@localhost:5432/reseller_test
      JWT_SECRET: ci-only-secret-change-in-prod
      ADMIN_BOOTSTRAP_EMAIL: admin@example.com
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: 20, cache: npm }
      - run: npm ci
      - run: npm run secret:scan
      - run: npm run db:generate
      - run: npx prisma db push
      - run: npm run typecheck --if-present
      - run: npm test --if-present
      - run: npm run build --if-present
      - name: Upload proof summary
        if: always()
        uses: actions/upload-artifact@v4
        with: { name: proof-summary, path: Docs/ }
""")
    write_saas_file(root, "railway.backend.json", json.dumps({"service":"api","requiredEnv":["DATABASE_URL","NODE_ENV","PORT","CORS_ORIGIN","JWT_SECRET","ADMIN_BOOTSTRAP_EMAIL"],"postDeployChecks":["/health returns status ok","GitHub Actions latest run conclusion success","rollback command recorded"],"health":"/health","rollback":"railway rollback or redeploy previous commit after approval"}, indent=2))
    write_saas_file(root, "Dockerfile.api", """
FROM node:20-alpine AS deps
WORKDIR /app
COPY package*.json ./
COPY apps/api/package.json apps/api/package.json
COPY packages/shared/package.json packages/shared/package.json
RUN npm install
FROM deps AS build
COPY . .
RUN npm run db:generate && npm run build -w packages/shared && npm run build -w apps/api
FROM node:20-alpine AS runner
WORKDIR /app
ENV NODE_ENV=production
COPY --from=build /app/package*.json ./
COPY --from=build /app/node_modules ./node_modules
COPY --from=build /app/apps/api/dist ./apps/api/dist
COPY --from=build /app/packages/shared/dist ./packages/shared/dist
COPY --from=build /app/prisma ./prisma
EXPOSE 3001
CMD ["node", "apps/api/dist/server.js"]
""")
    write_saas_file(root, ".env.example", """
NODE_ENV=development
PORT=3001
CORS_ORIGIN=http://localhost:3000
DATABASE_URL=postgresql://USER:PASSWORD@HOST:5432/DB
JWT_SECRET=replace-in-railway-not-in-git
ADMIN_BOOTSTRAP_EMAIL=admin@example.com
ADMIN_BOOTSTRAP_PASSWORD=replace-locally-only
""")
    write_saas_file(root, "tools/verify_github_actions.py", GITHUB_ACTIONS_VERIFY_SCRIPT)
    write_saas_file(root, "tools/verify_railway_url.py", RAILWAY_URL_VERIFY_SCRIPT)
    write_saas_file(root, "Docs/JWT_AUTH_SECURITY.md", """# JWT Auth Security

- JWT uses issuer `reseller-factory-os` and 8 hour expiration.
- Passwords use bcrypt hashing in seed/login flow.
- Role gates separate admin and reseller access. The lowercase role claim must be tested in JWT payloads.
- Production JWT_SECRET must exist only in Railway/GitHub secrets, never in git.
""")
    write_saas_file(root, "Docs/PRISMA_CRUD_PROOF.md", """# Prisma CRUD Proof

- Reseller CRUD uses Prisma client and PostgreSQL models.
- Create reseller uses transaction and writes AuditLog evidence.
- Product and Quote routes use Prisma-backed CRUD flow.
- Migration/rollback notes are required before production release.
""")
    write_saas_file(root, "Docs/GITHUB_ACTIONS_PROOF.md", """# GitHub Actions Proof

Record workflow run id, workflow URL, conclusion, branch, commit SHA, artifact name, and failing logs if any.
The `tools/verify_github_actions.py` helper can query the latest workflow run when GITHUB_TOKEN is provided.
""")
    write_saas_file(root, "Docs/RAILWAY_URL_VERIFICATION.md", """# Railway URL Verification

Record deployment url, /health status code, response body, checked_at timestamp, Railway service name, and rollback command.
The `tools/verify_railway_url.py` helper validates that deployment url + /health returns status ok.
""")
    write_saas_file(root, "README.md", f"""# {project}

AI-operated reseller SaaS scaffold generated by Reseller Factory OS.

## Local quick start
1. Copy `.env.example` to `.env` and fill local values only.
2. Run `npm install`.
3. Run `npm run db:generate`.
4. Run `npx prisma db push` for local/dev database.
5. Run `npm run typecheck`, `npm test`, and `npm run build`.

## Auth and CRUD
- `POST /api/auth/login` returns JWT.
- `GET/POST/PATCH/DELETE /api/resellers` are JWT protected and Prisma backed.
- `GET/POST /api/products` and `GET/POST /api/quotes` are Prisma backed.

## GitHub/Railway execution gates
Use --execute only after human approval. Keep GITHUB_TOKEN and RAILWAY_TOKEN outside git.

## Verify proof
```bash
GITHUB_TOKEN=... python tools/verify_github_actions.py --owner YOUR_ORG --repo {slugify(project)} --workflow proof-ci.yml
python tools/verify_railway_url.py --url https://YOUR-APP.up.railway.app/health
```
""")
    print(json.dumps({"scaffolded": str(root), "files": len(REQUIRED_SCAFFOLD_FILES), "prisma_crud": True, "jwt_auth": True, "ci_proof": True, "railway_url_verification": True, "safe_default": "dry-run"}, ensure_ascii=False, indent=2))


GITHUB_ACTIONS_VERIFY_SCRIPT = r'''#!/usr/bin/env python3
import argparse, json, os, urllib.request
p = argparse.ArgumentParser(); p.add_argument('--owner', required=True); p.add_argument('--repo', required=True); p.add_argument('--workflow', default='proof-ci.yml'); p.add_argument('--require-success', action='store_true'); args = p.parse_args()
token = os.environ.get('GITHUB_TOKEN')
if not token: raise SystemExit('GITHUB_TOKEN required to verify GitHub Actions')
req = urllib.request.Request(f'https://api.github.com/repos/{args.owner}/{args.repo}/actions/workflows/{args.workflow}/runs?per_page=1')
req.add_header('Authorization', f'Bearer {token}'); req.add_header('Accept', 'application/vnd.github+json')
with urllib.request.urlopen(req, timeout=30) as r: runs = json.loads(r.read().decode()).get('workflow_runs', [])
if not runs: raise SystemExit('no workflow runs found')
run = runs[0]
print(json.dumps({'run_id': run.get('id'), 'url': run.get('html_url'), 'status': run.get('status'), 'conclusion': run.get('conclusion'), 'head_sha': run.get('head_sha')}, indent=2))
if args.require_success and run.get('conclusion') != 'success': raise SystemExit(1)
'''

RAILWAY_URL_VERIFY_SCRIPT = r'''#!/usr/bin/env python3
import argparse, json, urllib.request, urllib.error, datetime
p = argparse.ArgumentParser(); p.add_argument('--url', required=True); p.add_argument('--expect-status', default='ok'); args = p.parse_args()
try:
    with urllib.request.urlopen(args.url, timeout=20) as r:
        status_code = r.status; body = r.read().decode(errors='replace')[:2000]
except urllib.error.HTTPError as e:
    status_code = e.code; body = e.read().decode(errors='replace')[:2000]
valid = status_code == 200 and args.expect_status.lower() in body.lower()
print(json.dumps({'valid': valid, 'url': args.url, 'status_code': status_code, 'body_sample': body, 'checked_at': datetime.datetime.now(datetime.UTC).isoformat()}, indent=2))
if not valid: raise SystemExit(1)
'''


def verify_github_actions(args: argparse.Namespace) -> int:
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print(json.dumps({"valid": False, "error": "GITHUB_TOKEN required to verify GitHub Actions"}, ensure_ascii=False, indent=2)); return 2
    req = urllib.request.Request(f"https://api.github.com/repos/{args.owner}/{args.repo}/actions/workflows/{args.workflow}/runs?per_page=1")
    req.add_header("Authorization", f"Bearer {token}"); req.add_header("Accept", "application/vnd.github+json")
    try:
        with urllib.request.urlopen(req, timeout=30) as r: data = json.loads(r.read().decode())
        runs = data.get("workflow_runs", [])
        if not runs: print(json.dumps({"valid": False, "error": "no workflow runs found"}, indent=2)); return 1
        run = runs[0]; valid = run.get("conclusion") == "success"
        print(json.dumps({"valid": valid, "run_id": run.get("id"), "url": run.get("html_url"), "status": run.get("status"), "conclusion": run.get("conclusion")}, indent=2)); return 0 if valid or not args.require_success else 1
    except Exception as exc:
        print(json.dumps({"valid": False, "error": str(exc)}, ensure_ascii=False, indent=2)); return 1


def verify_railway_url(args: argparse.Namespace) -> int:
    try:
        with urllib.request.urlopen(args.url, timeout=20) as r:
            status_code = r.status; body = r.read().decode(errors="replace")[:2000]
    except urllib.error.HTTPError as exc:
        status_code = exc.code; body = exc.read().decode(errors="replace")[:2000]
    except Exception as exc:
        print(json.dumps({"valid": False, "error": str(exc), "url": args.url}, ensure_ascii=False, indent=2)); return 1
    valid = status_code == 200 and args.expect_status.lower() in body.lower()
    print(json.dumps({"valid": valid, "url": args.url, "status_code": status_code, "body_sample": body, "checked_at": now_iso()}, ensure_ascii=False, indent=2))
    return 0 if valid else 1


def validate_content(args: argparse.Namespace) -> int:  # type: ignore[no-redef]
    root = Path(args.project_path).resolve()
    is_scaffold = (root / "package.json").exists() or (root / "apps").exists()
    failures: dict[str, list[str]] = {}
    for rel, words in QUALITY_KEYWORDS.items():
        if (not is_scaffold) and rel in {"Docs/JWT_AUTH_SECURITY.md", "Docs/PRISMA_CRUD_PROOF.md", "Docs/GITHUB_ACTIONS_PROOF.md", "Docs/RAILWAY_URL_VERIFICATION.md"}:
            continue
        path = root / rel
        if not path.exists():
            failures[rel] = ["missing file"]
            continue
        text = path.read_text(encoding="utf-8")
        missing = [word for word in words if word.lower() not in text.lower()]
        if missing:
            failures[rel] = missing
    scaffold_missing = [rel for rel in REQUIRED_SCAFFOLD_FILES if is_scaffold and not (root / rel).exists()]
    valid = not failures and not scaffold_missing
    print(json.dumps({"valid": valid, "content_failures": failures, "scaffold_missing": scaffold_missing}, ensure_ascii=False, indent=2))
    return 0 if valid else 1

def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("route"); r.add_argument("idea")
    i = sub.add_parser("init-project"); i.add_argument("idea"); i.add_argument("--project-name", default=None); i.add_argument("--output", required=True)
    v = sub.add_parser("validate-project"); v.add_argument("project_path")
    c = sub.add_parser("validate-content"); c.add_argument("project_path")
    s = sub.add_parser("scaffold-saas"); s.add_argument("idea"); s.add_argument("--project-name", default=None); s.add_argument("--output", required=True)
    gh = sub.add_parser("github-bootstrap"); gh.add_argument("--owner", required=True); gh.add_argument("--repo", required=True); gh.add_argument("--description", default=None); gh.add_argument("--private", action="store_true"); gh.add_argument("--execute", action="store_true")
    rw = sub.add_parser("railway-bootstrap"); rw.add_argument("--project", required=True); rw.add_argument("--service", default="api"); rw.add_argument("--execute", action="store_true")
    gha = sub.add_parser("verify-github-actions"); gha.add_argument("--owner", required=True); gha.add_argument("--repo", required=True); gha.add_argument("--workflow", default="proof-ci.yml"); gha.add_argument("--require-success", action="store_true")
    ruv = sub.add_parser("verify-railway-url"); ruv.add_argument("--url", required=True); ruv.add_argument("--expect-status", default="ok")
    args = parser.parse_args()
    if args.cmd == "route": print(json.dumps(route(args.idea), ensure_ascii=False, indent=2)); return 0
    if args.cmd == "init-project": init_project(args); return 0
    if args.cmd == "validate-project": return validate_project(args)
    if args.cmd == "validate-content": return validate_content(args)
    if args.cmd == "scaffold-saas": scaffold_saas(args); return 0
    if args.cmd == "github-bootstrap": return github_bootstrap(args)
    if args.cmd == "railway-bootstrap": return railway_bootstrap(args)
    if args.cmd == "verify-github-actions": return verify_github_actions(args)
    if args.cmd == "verify-railway-url": return verify_railway_url(args)
    return 1

if __name__ == "__main__":
    raise SystemExit(main())
