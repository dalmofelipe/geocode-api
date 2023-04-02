from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from . import search

api = FastAPI(
    help="GeoCoding MicroService"
)

api.include_router(search.routes, prefix='/search')

@api.get('/', include_in_schema=False)
def index():
    return RedirectResponse("http://localhost:8000/docs")
