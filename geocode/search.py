from typing import List

from fastapi import APIRouter

from .core import search
from .serializers import Location

routes = APIRouter()


@routes.get('/')
def endpoint_search(term:str) -> List[Location] | None:
    result = search(term)

    if result is None: 
        return []

    return result
