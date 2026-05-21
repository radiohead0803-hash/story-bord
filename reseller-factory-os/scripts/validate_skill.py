#!/usr/bin/env python3
from pathlib import Path
import sys

REQUIRED = [
    "SKILL.md",
    "agents/openai.yaml",
    "scripts/factory_os.py",
    "references/agent-operating-model.md",
    "references/github-railway-automation.md",
    "references/qa-audit-proof.md",
    "references/html-dashboard-spec.md",
    "references/quality-10-pass.md",
]

def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    missing = [p for p in REQUIRED if not (root / p).exists()]
    text = (root / "SKILL.md").read_text(encoding="utf-8") if (root / "SKILL.md").exists() else ""
    required_terms = ["GOAL", "Railway", "GitHub", "Proof", "Ten-Pass", "HTML", "Windsurf", "Codex", "Claude"]
    missing_terms = [t for t in required_terms if t not in text]
    if missing or missing_terms:
        print({"valid": False, "missing_files": missing, "missing_terms": missing_terms})
        return 1
    print({"valid": True, "message": "reseller factory os skill structure is complete"})
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
