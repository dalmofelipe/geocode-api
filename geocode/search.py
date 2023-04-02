from typing import List

from fastapi import APIRouter

from .core import search
from .serializers import Location

routes = APIRouter(tags=["Searching"])


@routes.get('/',
    description="""
## Endpoint de busca de endereços e coordenadas geográfica, pontos de referência e empressas

`Input`: QueryParam **term**

`Output`: Uma lista de possíveis endereços - incluindo coordenada (logintude e latitude) - de acordo com o termo pesquisado.

<br>

## Exemplos

**Empresas**

    http://localhost:8000/search?term=Google Belo Horizonte

**Ponto de referência**

    http://localhost:8000/search?term=Lagoa da Pampulha

**Em buscas de endereços, se deve especificar o tipo como Av ou Rua**

    http://localhost:8000/search?term=Av dos Andradas 3000 Belo Horizonte

**Caso contrário, não retornará endereços**

    http://localhost:8000/search?term=dos Andradas, 3000 Belo Horizonte
"""
)
def endpoint_search(term:str) -> List[Location] | None:
    result = search(term)

    if result is None: 
        return []

    return result
