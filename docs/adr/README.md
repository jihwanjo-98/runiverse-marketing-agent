# 설계 결정 기록 (ADR)

| # | 결정 | 상태 |
|---|---|---|
| [0001](0001-web-request-hub.md) | 마케터 창구는 웹(요청 + 대시보드), 노션은 기록 보관 | 채택 |
| [0002](0002-vercel-supabase.md) | Vercel(Next.js) + Supabase로 무료 배포 | 채택 (0006 · 0008에서 일부 변경) |
| [0003](0003-llm-backend-claude-code.md) | LLM 실행부는 교체 가능한 인터페이스, 기본은 `claude -p` | 대체됨 (0007) |
| [0004](0004-adaptive-polling-worker.md) | 로컬 워커가 1분 적응형 폴링으로 작업을 가져감 | 채택 |
| [0005](0005-router-registry.md) | 라우터 + agent 레지스트리, 숫자는 코드 · 판단은 LLM | 채택 |
| [0006](0006-fastapi-gateway.md) | FastAPI를 단일 데이터 게이트웨이로 | 채택 (인증은 0008에서 변경) |
| [0007](0007-llm-bedrock-langgraph.md) | LLM은 Bedrock + LangChain · LangGraph, 리서치는 Claude Code 배치 | 채택 |
| [0008](0008-data-access-sharing.md) | 데이터 저장 · 공유, Notion MCP, 팀 계정 로그인 | 채택 |
