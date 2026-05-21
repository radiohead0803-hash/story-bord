# QA, Audit, and Proof System

## Test Harness Minimum

- Unit tests for domain logic.
- API integration tests for auth, reseller, product, quote, order, inventory, invoice/settlement flows.
- UI component tests for critical forms and tables.
- E2E smoke test for login -> dashboard -> create quote/order -> approve -> status update.
- Seed data and deterministic test users.
- Regression checklist for every release.

## Reseller System Critical Risks

| Area | Risk | Required proof |
|---|---|---|
| RBAC | reseller sees wrong tenant/customer data | permission matrix tests |
| Pricing | wrong discount/tax/settlement | calculation test cases |
| Order flow | duplicate or stuck orders | idempotency and status transition tests |
| Inventory | oversell/incorrect reservation | concurrency scenario notes/tests |
| Secrets | leaked Railway/GitHub credentials | secret scan and env inventory |
| Database | migration breaks production | migration dry run and rollback note |
| UI | admin approves wrong item | confirmation UX and audit log |

## Proof Report Template

```markdown
# Proof Report

## Stage
- Stage:
- Commit/branch:
- Environment:
- Date:

## Requirement Traceability
| Requirement | Implementation | Evidence | Result |
|---|---|---|---:|

## Test Evidence
| Test | Command | Result | Log/screenshot |
|---|---|---:|---|

## Security/Audit Evidence
| Check | Evidence | Result | Notes |
|---|---|---:|---|

## Deployment Evidence
| Item | Evidence | Result |
|---|---|---:|

## Decision
Pass / Conditional Pass / Fail

## Required Fixes
1. ...
```
