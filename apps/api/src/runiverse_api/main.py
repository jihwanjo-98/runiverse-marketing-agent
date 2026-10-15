"""FastAPI 앱 진입점. 라우터·인증·DB 연결은 M2에서 구현한다."""

from fastapi import FastAPI

from runiverse_api import __version__

app = FastAPI(title="Runiverse Marketing Agent API", version=__version__)


@app.get("/health")
def health() -> dict[str, str]:
    """배포 확인용 헬스 체크."""
    return {"status": "ok", "version": __version__}
