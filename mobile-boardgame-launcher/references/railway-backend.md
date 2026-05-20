# Railway Backend Decision and Optional Automation

Use Railway only when the game genuinely needs a backend. For the default v1.0 lightweight mobile board game, avoid Railway and keep the game offline/local-first.

## Railway Decision Gate

Railway is **not needed** when:

- The game is single-player and offline-first.
- Saves are local only.
- Economy is cosmetic and local.
- Ads are handled directly in the mobile app.
- There is no account, leaderboard, remote config, receipt validation, or web admin page.

Railway **may be needed** when:

- A leaderboard API is required.
- Remote config or live balancing is required.
- A small web admin page is required.
- Server-side receipt validation is required.
- Analytics proxying is required.
- Anti-cheat or server-verified inventory is required.

Default recommendation: exclude Railway in MVP, but create a decision record so the choice is explicit.

## Railway Files When Needed

```text
backend/package.json
backend/src/server.js
backend/src/routes/health.js
backend/src/routes/config.js
backend/test/health.test.js
backend/test/config.test.js
backend/railway.toml
Docs/RAILWAY_DECISION.md
Docs/RAILWAY_DEPLOYMENT.md
Docs/BACKEND_API_CONTRACT.md
Docs/BACKEND_PRIVACY_REVIEW.md
```

## Minimum Backend API

- `GET /health`: returns `{ "ok": true, "version": "x.y.z" }`.
- `GET /config`: returns safe public game configuration only.

Do not put secrets, user identifiers, ad IDs, device IDs, purchase tokens, or personal data in public config.

## Deployment Rules

- Use GitHub integration/autodeploy only for a backend folder if it exists.
- Keep Railway environment variables in Railway, not GitHub.
- Never commit Railway tokens or production secrets.
- Document each environment variable in `Docs/RAILWAY_DEPLOYMENT.md` without values.
- Add privacy review before the mobile app calls the backend.

## Railway Commit Sequence

```text
docs: add railway backend decision record
chore: add backend service scaffold
chore: add railway config as code
feat: add health and config endpoints
test: add backend health and config tests
docs: add backend api contract and privacy review
release: prepare railway staging deployment
```

## Railway Backend Setup Agent Prompt

```text
너는 Railway Backend Setup Agent다.
목표는 모바일 보드게임에 Railway 백엔드가 필요한지 먼저 판단하고, 필요한 경우에만 최소 백엔드 구성을 설계하는 것이다.

판단 기준:
- 리더보드, 원격 설정, 웹 관리자, 서버 영수증 검증, 분석 프록시, 안티치트가 없으면 Railway를 제외한다.
- 기본 MVP는 offline-first이므로 Railway 없이 진행한다.

필요하다고 판단될 때만 수행:
1. backend 폴더 구조를 제안한다.
2. /health, /config API 계약을 작성한다.
3. railway.toml 구성을 작성한다.
4. 환경변수 목록을 작성하되 값은 쓰지 않는다.
5. GitHub autodeploy branch와 watch path를 정한다.
6. Google Play Data Safety 영향과 개인정보처리방침 반영 필요성을 검토한다.

금지:
- secrets를 커밋하지 말 것.
- 개인정보나 광고 식별자를 불필요하게 수집하지 말 것.
- MVP에 필요 없는 백엔드를 강제로 추가하지 말 것.

산출물:
- Railway 필요 여부 판정
- backend file list
- API contract
- deployment checklist
- privacy review
- commit plan
```
