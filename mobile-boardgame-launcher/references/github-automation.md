# GitHub New Repository and Commit Automation

Use this reference whenever the game project needs a new GitHub repository, initial commit plan, issue setup, pull request workflow, or release branch structure.

## Default GitHub Connection

- Default owner/account: `radiohead0803-hash`
- Known connected repositories:
  - `radiohead0803-hash/PVIM-System`
  - `radiohead0803-hash/cams-mold-management-system`
  - `radiohead0803-hash/change-point-management-system`
  - `radiohead0803-hash/dfmea-system-v4`

If the user is creating a brand-new game, propose a new repository under the default owner unless the user provides another owner.

## New Repository Defaults

- Visibility: private by default during development.
- Suggested repo name format: `<game-slug>-mobile-boardgame`, for example `pocket-trail-mobile-boardgame`.
- Default branches:
  - `main`: protected release-ready branch.
  - `develop`: integration branch for MVP work.
  - `feature/*`: feature work.
  - `test-harness/*`: harness and QA work.
  - `release/*`: internal test or production candidate.
- Require pull requests into `main` and prefer pull requests into `develop`.
- Require PR descriptions to include changed files, test evidence, known risks, and rollback notes.

## Initial Repository Files

Create these files before or with the first commit:

```text
README.md
.gitignore
Docs/GAME_DESIGN_BRIEF.md
Docs/TEST_HARNESS_PLAN.md
Docs/LICENSE_INVENTORY.md
Docs/PROOF_LOG.md
Docs/GOOGLE_PLAY_LAUNCH_CHECKLIST.md
Docs/SDK_AND_DATA_SAFETY_REGISTER.md
Docs/RELEASE_EVIDENCE.md
.github/ISSUE_TEMPLATE/bug_report.md
.github/ISSUE_TEMPLATE/feature_request.md
.github/pull_request_template.md
```

Use Unity-focused `.gitignore` rules. Never commit `Library/`, `Temp/`, `Obj/`, `Build/`, `Builds/`, `.gradle/`, user-specific IDE files, keystores, API keys, or Railway/Play Console secrets.

## Initial Labels

Create or recommend these labels:

- `mvp`
- `unity-core`
- `ui-ux`
- `test-harness`
- `qa-proof`
- `license-ip`
- `google-play`
- `backend-optional`
- `railway-optional`
- `bug`
- `blocker`
- `release-candidate`

## Initial Issues

Create or recommend issues for:

1. Define MVP scope and non-MVP exclusions.
2. Complete license/IP review.
3. Implement Unity scene flow.
4. Implement deterministic dice and movement harness.
5. Implement board/tile events.
6. Implement economy and shop tests.
7. Implement save/load and corrupt-data fallback.
8. Prepare Android AAB smoke test.
9. Complete Google Play store listing assets.
10. Complete SDK and Data Safety review.

## Commit Sequence

Use small verifiable commits:

```text
docs: add initial game design and launch checklist
chore: add unity gitignore and repository templates
chore: scaffold unity project folders and scenes
feat: add main menu to game scene flow
test: add deterministic dice harness
feat: add board movement and finish clamp
test: add board event and economy runners
feat: add save manager and shop skins
docs: update license inventory and data safety register
release: prepare internal test build 0.1.0
```

## GitHub Repo Setup Agent Prompt

```text
너는 GitHub Repo Setup Agent다.
목표는 Unity 모바일 보드게임 프로젝트를 위한 신규 GitHub 저장소 구조, 브랜치 전략, 초기 문서, 이슈, PR 템플릿, 커밋 계획을 준비하는 것이다.

기본 owner는 radiohead0803-hash이며, 사용자가 다른 owner/repo를 지정하면 그 값을 우선한다.

해야 할 일:
1. repo 이름을 제안하라.
2. private 기본 설정을 권장하라.
3. main/develop/feature/test-harness/release 브랜치 전략을 작성하라.
4. README, Docs, .github 템플릿 파일 목록을 작성하라.
5. Unity .gitignore 핵심 제외 항목을 작성하라.
6. 초기 GitHub 이슈 10개를 작성하라.
7. 커밋 시퀀스와 PR 규칙을 작성하라.

금지:
- secrets, keystore, API keys, Railway tokens, Google Play credentials를 파일에 넣지 말 것.
- main에 직접 구현 커밋을 권장하지 말 것.

산출물:
- repo setup checklist
- initial files list
- labels list
- initial issues list
- commit sequence
- PR template
```
