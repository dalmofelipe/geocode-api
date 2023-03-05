from fastapi import FastAPI

from . import search

api = FastAPI(help="GeoCoding MicroService")

api.include_router(search.routes, prefix='/search')