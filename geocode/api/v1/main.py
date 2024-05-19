from fastapi import APIRouter

from .endpoints.search import search_routes

routes = APIRouter(
    prefix='/api/v1',
    tags=['GeoCode API v1']
)

routes.include_router(search_routes)
