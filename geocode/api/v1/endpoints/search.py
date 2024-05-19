from typing import List

from fastapi import APIRouter

from ....core import search, get_docfile
from ..serializers.location import Location

search_routes = APIRouter(
    prefix="/search",
)


@search_routes.get(
    '/',
    description = get_docfile('/geocode/api/v1/docs/v1_search/search.md')
)
def endpoint_search(term:str) -> List[Location] | None:
    result = search(term)

    if result is None: 
        return []

    return result
