from geopy.geocoders import Nominatim


geolocator = Nominatim(user_agent="GeoCode")


def search_address(address:str):
    try:
        location = geolocator.geocode(address)
        return location.raw
    except Exception as e:
        print(f"Error geocode.core.main:search_address: \n{e}")
