# GitHub + Railway Automation

## Repository Blueprint

```text
repo/
  apps/web/              # frontend
  apps/api/              # backend
  packages/shared/       # types, schemas, utilities
  docs/                  # project evidence docs
  .github/workflows/     # CI checks
  .github/ISSUE_TEMPLATE/
  .github/PULL_REQUEST_TEMPLATE.md
  railway.json           # only if needed and safe
```

## Beginner Defaults

- One repository, monorepo structure.
- `main` = protected release branch.
- `develop` = integration branch.
- Feature branches per task.
- PR required for merge.
- CI must run lint, typecheck, tests, build.

## Railway Deployment Plan

Use Railway for:

- Backend API service.
- PostgreSQL database.
- Background workers if required.
- Optional frontend only when deployment simplicity beats using Vercel.

Required Railway artifacts:

- `Docs/RAILWAY_DEPLOYMENT.md`: services, env vars by name only, domains, health checks.
- `Docs/ENVIRONMENT_VARIABLES.md`: variable name, owner, environment, purpose, secret yes/no; never include values.
- `Docs/DEPLOYMENT_PROOF.md`: build logs summary, service status, health endpoint result, rollback point.

## CI/CD Minimum Checks

```yaml
name: ci
on: [push, pull_request]
jobs:
  verify:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
      - run: npm ci
      - run: npm run lint --if-present
      - run: npm run typecheck --if-present
      - run: npm test --if-present
      - run: npm run build --if-present
```

## Human Approval Gates

Require explicit human approval before:

- Creating or using production secrets.
- Publishing production deployment.
- Running destructive database migrations.
- Enabling billing, paid services, or external integrations.
- Sending real customer email/SMS/payment events.

## Executable GitHub/Railway API and CLI Automation Add-On

The skill now includes executable-safe commands in `scripts/factory_os.py` and generated project tools:

```bash
python scripts/factory_os.py scaffold-saas "reseller b2b portal" --project-name reseller-demo --output ./out/reseller-demo
python scripts/factory_os.py validate-project ./out/reseller-demo
python scripts/factory_os.py validate-content ./out/reseller-demo
python scripts/factory_os.py github-bootstrap --owner YOUR_ORG --repo reseller-demo --private
python scripts/factory_os.py railway-bootstrap --project reseller-demo --service api
```

Default mode is dry run. Real write actions require explicit `--execute`:

```bash
GITHUB_TOKEN=... python scripts/factory_os.py github-bootstrap --owner YOUR_ORG --repo reseller-demo --private --execute
RAILWAY_TOKEN=... python scripts/factory_os.py railway-bootstrap --project reseller-demo --service api --execute
```

Generated SaaS projects also include:

- `tools/github_bootstrap.py`: GitHub API repo/label/issue bootstrap helper.
- `tools/railway_bootstrap.py`: Railway CLI execution helper with token and human gate checks.
- `tools/secret-guard.mjs`: local CI secret leak guard.
- `.github/workflows/ci.yml`: proof CI.
- `.github/ISSUE_TEMPLATE/*.yml`: feature and bug templates.
- `railway.json`, `railway.backend.json`, `Dockerfile.api`: Railway deployment readiness.

### Safety rules

- Never run `--execute` unless the user explicitly approves the write action.
- Never print token values. Only report whether required env vars are present.
- Treat repository creation, production deploy, custom domain, billing, and destructive migration as Human Approval Gates.
- Dry-run output is acceptable proof for planning; execution proof requires API/CLI output, commit SHA, deployment ID, health result, and rollback plan.
