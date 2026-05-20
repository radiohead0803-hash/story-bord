# Unity Operations Add-On Packs

Use this reference when the user asks what additional automation should be added to Unity operations, or when strengthening the production workflow for AI-agent-driven Unity development.

## Selection Rule

Do not add every pack blindly. Select packs that reduce the current project's highest risk. Prefer lightweight documentation, deterministic Editor scripts, and proof logs before adding heavy services or SDKs.

## Recommended Add-On Packs

### 1. Unity Project Doctor Pack
Purpose: find broken Unity setup before coding agents continue.

Checks:
- Missing scenes in Build Settings.
- Missing or null Inspector references.
- Missing ScriptableObject config assets.
- Duplicate singletons or scene managers.
- Invalid package versions.
- Missing Android build support assumptions.
- Broken prefab references.
- Untracked generated assets.

Expected outputs:
- `Docs/UNITY_PROJECT_DOCTOR.md`
- `Docs/BROKEN_REFERENCES_REPORT.md`
- `Tools/Mobile Boardgame/Run Project Doctor` menu item requirement

### 2. Dependency and Package Governance Pack
Purpose: prevent package bloat and SDK/privacy surprises.

Rules:
- Require an approval note before adding Unity packages, ad SDKs, analytics SDKs, networking libraries, or asset-store packages.
- Record package name, version, reason, license, data collection, and rollback plan.
- Prefer built-in Unity features for MVP unless a package removes clear risk.

Expected outputs:
- `Docs/PACKAGE_GOVERNANCE.md`
- `Docs/SDK_PRIVACY_REGISTER.md`
- `Docs/PACKAGE_ROLLBACK_PLAN.md`

### 3. Addressables and Asset Pipeline Decision Pack
Purpose: decide whether the project needs Addressables or a simple Resources/serialized reference model.

Default:
- Do not use Addressables in v1 unless the game has many downloadable themes, live content, or large asset bundles.

Use Addressables only when:
- Assets are too large for simple build packaging.
- The game needs post-launch downloadable boards/themes.
- Remote content is planned and privacy/network policy is reviewed.

Expected outputs:
- `Docs/ASSET_PIPELINE_DECISION.md`
- `Docs/ASSET_NAMING_RULES.md`

### 4. Save Data Migration and Versioning Pack
Purpose: keep local data safe across updates.

Requirements:
- Version every save payload.
- Provide migration from old keys/schema to new keys/schema.
- Provide corrupt data fallback.
- Provide debug reset only in dev/test builds.
- Test upgrade from v0.1 to v0.2 style scenarios.

Expected outputs:
- `Docs/SAVE_MIGRATION_PLAN.md`
- `SaveLoadMigrationTestRunner`
- proof entry in `Docs/PROOF_LOG.md`

### 5. Performance Budget and Device Matrix Pack
Purpose: keep low-end Android devices playable.

Budgets:
- Target FPS: 60 if feasible, 30 minimum acceptable for simple board games.
- Memory: keep textures/audio small for MVP.
- Startup time: avoid long first-load waits.
- Battery/network: avoid background work for offline-first v1.

Expected outputs:
- `Docs/PERFORMANCE_BUDGET.md`
- `Docs/DEVICE_TEST_MATRIX.md`
- device smoke evidence in `Docs/BUILD_PROOF.md`

### 6. Automated Screenshot and Store Asset Capture Pack
Purpose: reduce manual screenshot work and keep store assets consistent with the actual build.

Automation target:
- Dedicated screenshot scene or capture mode.
- Fixed device aspect ratios.
- Preconfigured gameplay states: main menu, dice roll, reward, shop, result.
- Evidence that screenshots match implemented features.

Expected outputs:
- `Docs/STORE_SCREENSHOT_PLAN.md`
- `Assets/Scripts/Editor/ScreenshotCaptureTool.cs` prompt requirement
- screenshot proof checklist

### 7. Keystore and Release Signing Governance Pack
Purpose: avoid losing release signing credentials.

Rules:
- Never commit keystore files, passwords, service account JSON, API keys, or secrets.
- Store credentials in a private password manager or approved secret store.
- Record who owns the key and where recovery instructions are stored, without exposing secrets.
- Use placeholder paths in docs.

Expected outputs:
- `Docs/RELEASE_SIGNING_RUNBOOK.md`
- `Docs/SECRET_HANDLING_POLICY.md`

### 8. Rollback and Hotfix Pack
Purpose: keep post-launch fixes controlled.

Rules:
- Use release tags for every internal/closed/production test build.
- Create `hotfix/*` branches from the latest release tag.
- Require bug reproduction, fix proof, regression result, and release note.

Expected outputs:
- `Docs/HOTFIX_RUNBOOK.md`
- `Docs/ROLLBACK_PLAN.md`
- hotfix PR template section

### 9. AI Agent Memory and Handoff Pack
Purpose: prevent parallel agents from losing context or overwriting each other.

Rules:
- Maintain one handoff file per agent lane.
- Every agent must list changed files, assumptions, tests run, failed tests, and next owner.
- Verification agents must not edit production files.

Expected outputs:
- `Docs/AGENT_HANDOFF_LOG.md`
- `Docs/AGENT_OWNERSHIP_MATRIX.md`
- `Docs/STAGE_GATE_REPORT.md`

### 10. Unity Compile Error Triage Pack
Purpose: handle common AI-generated Unity errors quickly.

Triage order:
1. Read exact Unity Console error.
2. Class name must match file name for MonoBehaviour scripts.
3. Namespace/import errors.
4. Missing package references.
5. Assembly definition conflicts.
6. API usage incompatible with selected Unity version.
7. Serialized field renamed without migration.

Expected outputs:
- `Docs/COMPILE_ERROR_TRIAGE.md`
- `Docs/KNOWN_ERRORS.md`

## Add-On Recommendation Template

```markdown
# Unity Operations Add-On Recommendation

## Project Risk Snapshot
| Risk | Level | Evidence | Recommended pack |
|---|---:|---|---|

## Selected Packs
1. [Pack name] - why needed now
2. [Pack name] - why needed now

## Deferred Packs
| Pack | Reason deferred | Trigger to add later |
|---|---|---|

## New Files / Menus
- Docs/...
- Tools/Mobile Boardgame/...

## Proof Required
- Generated files:
- Unity Console:
- Test/harness:
- Build/device evidence:
```

## Windsurf Prompt: Unity Operations Add-On Architect

```text
너는 Unity Operations Add-On Architect Agent다.
목표는 현재 모바일 보드게임 프로젝트의 운영 리스크를 분석하고, 필요한 Unity 운영 자동화 Pack만 선택해 구현 계획을 만드는 것이다.

입력:
- 게임 타입
- 현재 Unity 자동화 상태
- 현재 GitHub/CI/SceneBaker/테스트 하네스 상태
- 출시 단계: concept / scaffold / playable / internal-test / closed-test / production

해야 할 일:
1. 현재 가장 큰 운영 리스크 5개를 선정하라.
2. Unity Project Doctor, Package Governance, Asset Pipeline, Save Migration, Performance Budget, Screenshot Capture, Keystore Governance, Hotfix/Rollback, Agent Handoff, Compile Error Triage 중 필요한 Pack만 선택하라.
3. 선택하지 않은 Pack은 왜 보류하는지 적어라.
4. 각 Pack의 생성 문서, Editor 메뉴, 테스트 증거, 담당 에이전트를 정의하라.
5. 실제 구현은 작은 PR 단위로 나누고, Verification/Proof Agent가 확인할 증거를 요구하라.

제약:
- MVP를 무겁게 만들지 마라.
- 새 SDK/패키지는 명확한 필요가 있을 때만 허용하라.
- 비밀키, keystore, service account, API key는 절대 커밋하지 마라.
- 검증 증거 없이 완료 처리하지 마라.

산출물:
- Unity Operations Add-On Recommendation
- 선택 Pack 목록
- 보류 Pack 목록
- 파일/메뉴 생성 목록
- PR/커밋 계획
- 검증/증명 기준
```
