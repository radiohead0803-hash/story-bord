import argparse
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "factory_os.py"
sys.path.insert(0, str(ROOT / "scripts"))
import factory_os  # noqa: E402


def run_cmd(*args, check=True):
    env = os.environ.copy()
    if "--execute" in args:
        env.pop("GITHUB_TOKEN", None)
        env.pop("RAILWAY_TOKEN", None)
    return subprocess.run([sys.executable, str(SCRIPT), *args], check=check, text=True, capture_output=True, env=env)


def scaffold(out: Path, idea="reseller b2b portal"):
    factory_os.scaffold_saas(argparse.Namespace(idea=idea, project_name="saas", output=str(out)))


def init_project(out: Path, idea="reseller portal"):
    factory_os.init_project(argparse.Namespace(idea=idea, project_name="demo", output=str(out)))


class FactoryOsTests(unittest.TestCase):
    def test_route_contains_github_railway_for_deploy_request(self):
        data = factory_os.route("리셀러 시스템 GitHub Railway 배포")
        self.assertIn("GitHub", data["active_packs"])
        self.assertIn("Railway Deployment", data["active_packs"])
        self.assertIn("SaaS Scaffold", data["active_packs"])

    def test_route_has_human_approval_gates(self):
        data = factory_os.route("reseller portal")
        self.assertIn("production secrets", data["human_approval_gates"])
        self.assertIn("production release", data["human_approval_gates"])

    def test_init_and_validate_project(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "demo"
            init_project(out)
            self.assertTrue((out / "Docs" / "GOAL.md").exists())
            self.assertTrue((out / "dashboard" / "factory-control-board.html").exists())
            code = factory_os.validate_project(argparse.Namespace(project_path=str(out)))
            self.assertEqual(code, 0)

    def test_validate_content_passes_generated_project(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "demo"
            init_project(out)
            code = factory_os.validate_content(argparse.Namespace(project_path=str(out)))
            self.assertEqual(code, 0)

    def test_validate_project_fails_missing_doc(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "demo"
            init_project(out)
            (out / "Docs" / "GOAL.md").unlink()
            code = factory_os.validate_project(argparse.Namespace(project_path=str(out)))
            self.assertNotEqual(code, 0)

    def test_scaffold_saas_creates_monorepo_files(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "saas"
            scaffold(out)
            for rel in ["package.json", "apps/web/src/app/page.tsx", "apps/api/src/server.ts", "packages/shared/src/index.ts", "prisma/schema.prisma"]:
                self.assertTrue((out / rel).exists(), rel)

    def test_scaffold_saas_creates_github_files(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "saas"
            scaffold(out)
            self.assertTrue((out / ".github" / "workflows" / "ci.yml").exists())
            self.assertTrue((out / ".github" / "pull_request_template.md").exists())
            self.assertTrue((out / ".github" / "ISSUE_TEMPLATE" / "feature_request.yml").exists())
            self.assertTrue((out / ".github" / "ISSUE_TEMPLATE" / "bug_report.yml").exists())

    def test_scaffold_saas_creates_railway_files(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "saas"
            scaffold(out, "reseller b2b portal railway")
            self.assertTrue((out / "railway.json").exists())
            self.assertTrue((out / "railway.backend.json").exists())
            self.assertTrue((out / "Dockerfile.api").exists())

    def test_scaffold_saas_creates_automation_scripts(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "saas"
            scaffold(out)
            self.assertTrue((out / "tools" / "github_bootstrap.py").exists())
            self.assertTrue((out / "tools" / "railway_bootstrap.py").exists())
            self.assertTrue((out / "tools" / "secret-guard.mjs").exists())

    def test_validate_content_passes_scaffold(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "saas"
            scaffold(out)
            code = factory_os.validate_content(argparse.Namespace(project_path=str(out)))
            self.assertEqual(code, 0)

    def test_validate_content_detects_missing_scaffold_file(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "saas"
            scaffold(out)
            (out / "railway.json").unlink()
            code = factory_os.validate_content(argparse.Namespace(project_path=str(out)))
            self.assertNotEqual(code, 0)

    def test_github_bootstrap_dry_run(self):
        result = run_cmd("github-bootstrap", "--owner", "demo", "--repo", "demo-repo", "--private")
        data = json.loads(result.stdout)
        self.assertTrue(data["dry_run"])
        self.assertEqual(data["plan"]["repo"], "demo-repo")

    def test_github_bootstrap_execute_requires_token(self):
        result = run_cmd("github-bootstrap", "--owner", "demo", "--repo", "demo-repo", "--execute", check=False)
        self.assertEqual(result.returncode, 2)
        self.assertIn("GITHUB_TOKEN", result.stdout)

    def test_railway_bootstrap_dry_run(self):
        result = run_cmd("railway-bootstrap", "--project", "demo", "--service", "api")
        data = json.loads(result.stdout)
        self.assertTrue(data["dry_run"])
        self.assertIn(["railway", "status"], data["commands"])

    def test_railway_bootstrap_execute_requires_token(self):
        result = run_cmd("railway-bootstrap", "--project", "demo", "--execute", check=False)
        self.assertEqual(result.returncode, 2)
        self.assertIn("RAILWAY_TOKEN", result.stdout)

    def test_env_example_has_no_real_secret(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "saas"
            scaffold(out)
            text = (out / ".env.example").read_text()
            self.assertIn("replace-in-railway-not-in-git", text)
            self.assertNotIn("sk-", text)

    def test_api_contract_contains_required_endpoint(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "saas"
            scaffold(out)
            api = (out / "Docs" / "API_CONTRACT.md").read_text()
            self.assertIn("/health", api)
            self.assertIn("/api/resellers", api)

    def test_database_schema_contains_audit_log(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "saas"
            scaffold(out)
            schema = (out / "prisma" / "schema.prisma").read_text()
            self.assertIn("model AuditLog", schema)

    def test_readme_mentions_execute_gate(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "saas"
            scaffold(out)
            readme = (out / "README.md").read_text()
            self.assertIn("--execute", readme)
            self.assertIn("GITHUB_TOKEN", readme)
            self.assertIn("RAILWAY_TOKEN", readme)

    def test_html_dashboard_is_created(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "saas"
            scaffold(out)
            html = (out / "dashboard" / "developer-decision-board.html").read_text()
            self.assertIn("Decision Board", html)

    def test_project_has_factory_quality_gate_99_doc(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "saas"
            scaffold(out)
            self.assertTrue((out / "Docs" / "FACTORY_QUALITY_GATE_99.md").exists())

    def test_slugify_fallback_via_project_output(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "saas"
            scaffold(out, "!!!")
            self.assertTrue((out / "package.json").exists())


    def test_final_prisma_crud_files_created(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "saas"
            scaffold(out)
            for rel in ["apps/api/src/lib/prisma.ts", "apps/api/src/routes/auth.ts", "apps/api/src/routes/products.ts", "apps/api/src/routes/quotes.ts", "prisma/seed.ts"]:
                self.assertTrue((out / rel).exists(), rel)

    def test_final_jwt_auth_security_doc_created(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "saas"
            scaffold(out)
            text = (out / "Docs" / "JWT_AUTH_SECURITY.md").read_text()
            self.assertIn("JWT", text)
            self.assertIn("bcrypt", text)
            self.assertIn("role", text)

    def test_final_prisma_schema_has_user_and_indexes(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "saas"
            scaffold(out)
            schema = (out / "prisma" / "schema.prisma").read_text()
            self.assertIn("model User", schema)
            self.assertIn("@@index", schema)
            self.assertIn("model AuditLog", schema)

    def test_final_ci_has_postgres_and_prisma_steps(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "saas"
            scaffold(out)
            ci = (out / ".github" / "workflows" / "ci.yml").read_text()
            self.assertIn("postgres", ci)
            self.assertIn("npm run db:generate", ci)
            self.assertIn("npx prisma db push", ci)

    def test_final_verify_tools_created(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "saas"
            scaffold(out)
            self.assertTrue((out / "tools" / "verify_github_actions.py").exists())
            self.assertTrue((out / "tools" / "verify_railway_url.py").exists())
            self.assertTrue((out / "Docs" / "RAILWAY_URL_VERIFICATION.md").exists())

    def test_final_cli_verify_github_requires_token(self):
        result = run_cmd("verify-github-actions", "--owner", "demo", "--repo", "demo", check=False)
        self.assertEqual(result.returncode, 2)
        self.assertIn("GITHUB_TOKEN", result.stdout)


if __name__ == "__main__":
    unittest.main()
