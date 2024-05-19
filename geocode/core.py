import os

from typing import List

from geopy.geocoders import Nominatim
from geopy.location import Location as GeopyLocation

from .api.v1.serializers.location import Location

geolocator = Nominatim(user_agent="GeoCode")


def get_docfile(file_path:str):
    root_dir = os.getcwd()

    with open(root_dir + file_path, 'r', encoding='utf-8') as file:
        return ''.join(file.read())


def to_serial_location(location: GeopyLocation):
    return Location(
        address=location.address, 
        latitude=location.latitude,
        longitude=location.longitude
    )


def search(term:str) -> List[Location] | None:
    """
    Busca por endereços, empresas e pontos de referência

    Em pesquisas por endereços, deve-se informar o tipo do logradouro como 
    rua ou avenida.

    Retorna uma lista de localização com base no termo informado
    """
    try:
        result : List[GeopyLocation] = geolocator.geocode(
            term, limit = 5, exactly_one = False
        )

        if not result: return None

        list_address : List[Location] = \
            list(map(lambda l: to_serial_location(l), result))

        return list_address
    except Exception as e:
        print(f"Error geocode.core:search: \n{e}")
