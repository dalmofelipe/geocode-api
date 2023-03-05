from typing import List

from geopy.geocoders import Nominatim
from geopy.location import Location as GeopyLocation

from .serializers import Location as SerialLocation

geolocator = Nominatim(user_agent="GeoCode")


def to_serial_location(location: GeopyLocation):
    return SerialLocation(
        address=location.address, 
        latitude=location.latitude,
        longitude=location.longitude
    )


def search(term:str) -> List[SerialLocation] | None:
    """
    Busca por endereços, empresas e pontos de referência

    Em pesquisas por endereços, deve-se informar o tipo do logradouro como 
    rua ou avenida.

    Retorna uma lista de localização com base no nome informado
    """
    try:
        result : List[GeopyLocation] = geolocator.geocode(
            term, limit = 5, exactly_one = False
        )

        if not result: return None

        list_address : List[SerialLocation] = \
            list(map(lambda l: to_serial_location(l), result))

        return list_address
    except Exception as e:
        print(f"Error geocode.core.main:search: \n{e}")
