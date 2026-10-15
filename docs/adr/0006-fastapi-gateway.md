# 0006. FastAPI를 단일 데이터 게이트웨이로

- 상태: 채택 · 2026-10-14 · [0002](0002-vercel-supabase.md) 일부 대체 · 인증 부분은 [0008](0008-data-access-sharing.md)에서 변경

## 맥락
초기 설계는 웹과 워커가 Supabase에 직접 붙고, 권한은 RLS 정책(SQL)으로 막는 구조였다. 이 경우 워커가 Supabase 관리자 키를 가져야 하고, 권한 로직이 SQL 정책에 흩어진다. 또 백엔드 API를 직접 설계·구현하는 것이 프로젝트 목표 중 하나다.

## 결정
- 데이터 출입은 모두 FastAPI(`apps/api`)를 거친다. 웹은 화면만, 워커는 처리만 맡는다.
- FastAPI는 별도 Vercel 프로젝트(Python 런타임, Root Directory `apps/api`)로 배포하고, 함수 실행 지역을 서울(`icn1`)로 맞춘다.
- 인증은 두 종류다.
  - 마케터: Supabase Auth 로그인 토큰(JWT)을 FastAPI가 검증하고, 이메일 허용 목록과 대조한다.
  - 워커: 워커 전용 API 토큰.
- API와 워커가 주고받는 형식은 `packages/contracts`의 pydantic 모델 하나로 정의하고, uv 워크스페이스로 함께 쓴다. 웹의 TypeScript 타입은 FastAPI의 OpenAPI 문서에서 생성한다.

## 서버리스 제약과 대응
| 제약 (Vercel Hobby) | 대응 |
|---|---|
| 요청 1건 최대 300초 | LLM 처리는 워커가 맡으므로 API는 짧은 요청만 처리한다 |
| 요청·응답 본문 최대 4.5MB | 소재 파일은 API가 Supabase Storage 서명 업로드 URL만 발급하고, 브라우저가 직접 올린다 |
| 백그라운드 작업 불가 | `BackgroundTasks`·스케줄러를 쓰지 않는다. 오래 걸리는 일은 워커가 처리한다 |
| 요청마다 새 인스턴스 가능 | DB는 Supabase 연결 풀러(transaction 모드) 주소로 접속하고 연결을 오래 붙잡지 않는다 |

## 결과
- 워커는 DB 키 없이 워커 토큰만 가진다. 토큰이 유출되어도 워커용 엔드포인트 범위로 피해가 제한된다.
- 권한 검사와 입력 검증이 Python 코드와 테스트로 한곳에 모인다. RLS는 켜 두되 공개 키로 테이블에 직접 접근하는 경로를 막는 보조 방어로만 쓴다.
- Vercel 프로젝트가 웹·API 두 개가 된다.
- 확인 필요: 워크스페이스 패키지(`packages/contracts`)가 Vercel Python 빌드에 포함되는지. M0 배포 단계에서 `/health` 배포로 먼저 확인하고, 안 되면 빌드 시 복사하는 방식으로 대체한다.
