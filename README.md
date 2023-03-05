
# GeoCode Microservice

Serviço de pesquisa de endereço, coordenadas, companhias e pontos de referência.

## Iniciando

    > git clone [repo]
    > cd geocode 
    > poetry shell
    > poetry install
    > geocode

Servidor iniciará na porta 8000.

## Rota `/search`

    GET http://localhost:8000/search?term=Av dos Andradas 3000 HTTP/1.1
    GET http://localhost:8000/search?term=3000 Av dos Andradas HTTP/1.1
    GET http://localhost:8000/search?term=Lagoa da Pampulha HTTP/1.1
    GET http://localhost:8000/search?term=Google Belo Horizonte HTTP/1.1


### **QUERY PARAMS**

`term` : termo de busca, pode ser endereço, ponto de refência ou nome de empresas. 

Em caso de pesquisa de endereço, deve-se informar o tipo do logradouro, como Av, Avenida ou Rua. Também é indicado informar o numero do endereço, no inicio da string. Exemplo `3000 Av dos Andradas`.

### **Retorno**

Retona uma lista de localidades encontradas ou não.

    [
        {
            addres: string,
            latitude: float,
            logitude: float,
        }
    ]
