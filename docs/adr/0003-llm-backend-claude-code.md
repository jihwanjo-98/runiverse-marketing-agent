# 0003. LLM 실행부는 교체 가능한 인터페이스, 기본은 `claude -p`

- 상태: 대체됨 · 2026-10-15 · [0007](0007-llm-bedrock-langgraph.md)로 대체. 리서치 배치(A1 · A2)에서만 `claude -p` 사용

## 맥락
추가 비용 없이 운영자의 Claude Code 구독으로 agent를 돌려야 한다. 동시에 실제 조직 배포 시에는 API로 옮길 수 있어야 한다.

## 결정
`LLMBackend` 인터페이스를 두고, 기본 구현 `ClaudeCodeBackend`가 Claude Code 헤드리스 모드를 서브프로세스로 호출한다.

- `--output-format json --json-schema`로 구조화된 출력을 받고, 같은 pydantic 모델로 한 번 더 검증한다.
- `--permission-mode dontAsk --permission-prompts none`, `--allowedTools`로 무인 실행 권한을 고정한다.
- `--bare`는 쓰지 않는다. bare 모드는 구독 로그인을 읽지 않고 API 키를 요구한다. 대신 실행 위치를 `worker/agent_home/`으로 고정해 환경을 통제한다.

## 결과
- agent 1개 = 호출 1번. 흐름 제어·재시도·저장은 Python이 맡아 실패 지점 추적과 테스트가 쉽다.
- 테스트는 subprocess를 mock 처리해 사용량 없이 돌린다.
- 운영 배포 시 `ApiBackend`를 추가하고 `LLM_BACKEND` 설정만 바꾼다. 개인 구독으로 타인 요청을 상시 처리하는 형태는 피한다.
