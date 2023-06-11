
# GeoCode

API para busca de endereço, companhias e pontos de referência. 

Retorna diversas informações sobre o endereço informado, além de sua coordenada geografica.

<br>

### Iniciando

    > git clone [repo]
    > cd geocode 
    > poetry shell
    > poetry install
    > geocode

Servidor iniciará na porta 8000. Acesse `http://localhost:8000/docs` para consulta documentação.

<br>

### Rota `/search`

    GET http://localhost:8000/search?term=Av dos Andradas 3000 HTTP/1.1
    GET http://localhost:8000/search?term=3000 Av dos Andradas HTTP/1.1
    GET http://localhost:8000/search?term=Lagoa da Pampulha HTTP/1.1
    GET http://localhost:8000/search?term=Google Belo Horizonte HTTP/1.1


**QUERY PARAMS**

`term` : termo de busca, pode ser endereço, ponto de refência ou nome de empresas. 

Em caso de pesquisa de endereço, deve-se informar o tipo do logradouro, como Av, Avenida ou Rua. Também é indicado informar o numero do endereço, no inicio da string. Exemplo `3000 Av dos Andradas`.

**RETORNO**

Retona uma lista de localidades encontradas.

    [
        {
            addres: string,
            latitude: float,
            logitude: float,
        }
    ]

<br>
