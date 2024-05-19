from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from .api.v1 import main as api_v1

api = FastAPI(help="GeoCoding")

api.include_router(api_v1.routes)


@api.get('/', include_in_schema=False)
def index():
    return RedirectResponse("http://localhost:8000/docs")
