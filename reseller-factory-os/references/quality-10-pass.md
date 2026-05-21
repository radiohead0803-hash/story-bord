# Ten-Pass Quality Improvement

Run this when creating an operating-system package or major release plan.

| Pass | Review question | Upgrade rule |
|---|---|---|
| 1 Scope | Is the scope precise and not bloated? | remove or defer vague modules |
| 2 Beginner | Can a beginner follow decisions? | add selection boards and copy-paste prompts |
| 3 Agents | Are builder/proof roles separated? | split conflicting responsibilities |
| 4 Requirements | Are roles, flows, edge cases covered? | add missing matrix/checklist |
| 5 Architecture | Is stack deployable and maintainable? | simplify, document tradeoffs |
| 6 GitHub/Railway | Can it be deployed safely? | add env, CI, rollback proof |
| 7 QA Harness | Can bugs be caught repeatably? | add tests, fixtures, smoke flows |
| 8 Security | Are secrets/RBAC/privacy safe? | add audit gates |
| 9 Evidence | Is proof stronger than claims? | require logs/screenshots/results |
| 10 Textbook | Can other systems reuse it? | generalize templates and decision rules |

Final output should include applied improvements, deferred improvements, and remaining risks.
