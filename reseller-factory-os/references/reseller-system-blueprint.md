# Reseller System Blueprint

## Common Modules

- Admin dashboard.
- Reseller/partner onboarding.
- Role and permission management.
- Product/catalog management.
- Price policy, discount, tax, margin, settlement rules.
- Quotation and approval workflow.
- Order management.
- Inventory/reservation visibility.
- Invoice, billing, settlement, refund/adjustment.
- Customer/company master data.
- Notifications and activity feed.
- Audit log and export/reporting.

## Role Examples

| Role | Typical permissions |
|---|---|
| Super Admin | all tenants/settings/audit |
| Sales Admin | products, pricing, quotes, orders |
| Finance Admin | invoices, settlement, adjustments |
| Reseller Manager | own company users/orders/quotes |
| Reseller Staff | create quotes/orders, view own data |
| Viewer/Auditor | read-only reports and logs |

## MVP Recommendation

Start with:

1. Login/RBAC.
2. Reseller company/user management.
3. Product catalog.
4. Quote/order workflow.
5. Admin approval.
6. Basic reporting.
7. Audit log.

Defer advanced ERP integration, payments, warehouse sync, multi-currency, and complex settlement until the core workflow is proven.
