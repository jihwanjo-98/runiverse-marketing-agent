# apps/web

Next.js 16 (App Router, TypeScript, Tailwind CSS, ESLint) 웹 앱. `create-next-app`으로 생성한 기본 골격 상태입니다.

Vercel 프로젝트 설정: Root Directory = `apps/web`

- 브라우저는 FastAPI를 직접 호출하지 않는다. Next.js 서버(서버 컴포넌트 · Route Handler)가 `WEB_SERVER_TOKEN`과 세션 토큰을 붙여 FastAPI를 호출한다.
- 로그인은 팀 공용 계정(member)과 관리자 계정(admin). 세션 토큰은 httpOnly 쿠키에 둔다.
- 파일은 FastAPI가 발급한 서명 URL로 Supabase Storage에 직접 올린다. Supabase 키는 웹에 두지 않는다.

## 로컬 실행

```powershell
cd apps\web
npm install
Copy-Item .env.local.example .env.local
npm run dev      # http://localhost:3000
npm run lint
npm run build
```

`AGENTS.md` · `CLAUDE.md`는 Next.js가 생성한 파일로, 이 버전의 Next.js 문서(`node_modules/next/dist/docs/`)를 먼저 보라는 지침입니다. `next dev`가 다시 만들므로 그대로 둡니다.
