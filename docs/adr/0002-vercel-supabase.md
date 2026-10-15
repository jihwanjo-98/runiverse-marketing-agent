# 0002. Vercel(Next.js) + Supabase로 무료 배포

- 상태: 채택 · 2026-10-14 · [0006](0006-fastapi-gateway.md) · [0008](0008-data-access-sharing.md)에서 일부 변경

## 맥락
비용 0, 팀원 3명만 접근, 요청·결과·지표 저장이 필요하다. Cloudflare(Pages+Workers+D1+Access)와 Vercel+Supabase를 비교했다.

## 결정
Next.js 화면을 Vercel Hobby에 배포한다. 저장·파일·인증은 Supabase 무료 플랜을 쓴다.

> 변경(0006): API는 Next.js가 아니라 별도 FastAPI 프로젝트로 분리한다.

## 근거
- 프로젝트가 비상업이라 Vercel Hobby 약관(비상업 개인 용도)에 맞는다.
- Hobby에는 프로덕션 비밀번호 보호가 없어, Supabase Auth + 이메일 허용 목록으로 접근 제어를 직접 구현한다 (권한 검사는 0006에 따라 FastAPI가 담당).
- 로컬 워커가 1분마다 조회하므로 Supabase 무료 프로젝트의 비활성 일시정지 대상이 되지 않는다.

## 결과
- ~~서비스 키(service role)는 로컬 워커에만 두고, 브라우저는 공개 키 + RLS로만 접근한다.~~ → 0006: DB 접속 정보는 FastAPI에만 두고, 워커와 브라우저는 FastAPI만 호출한다.
- 상업적 운영으로 바뀌면 Vercel Pro 또는 Cloudflare로 이전을 재검토한다.
