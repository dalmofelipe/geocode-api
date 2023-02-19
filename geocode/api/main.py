from fastapi import FastAPI

from geocode.core.geocode import search_address


api = FastAPI(help="GeoCoding MicroService")


@api.get('/geocode/location')
def api_search_address(
    address:str
):
    return search_address(address)
