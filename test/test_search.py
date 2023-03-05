from geocode.core import search


def test_search_exactly_address():
    address = 'Av dos Andradas 3000'
    result = search(address)
    assert result != None
    result_search = result[0]
    assert result_search.address\
        .__contains__('Mr. Black Café Gourmet') == True


def test_search_reference_point():
    reference = 'Lagoa da Pampulha'
    result = search(reference)
    assert result != None
    last_address = result[-1]
    assert last_address.address\
        .__contains__('Belo Horizonte') == True


def test_search_company():
    company = 'Google Belo Horizonte'
    result = search(company)
    assert result != None
    assert result[0].address\
        .__contains__('Andradas') == True


def test_search_with_type_address():
    address = 'Av dos Andradas, 3000 Belo Horizonte'
    result = search(address)
    assert result != None


def test_search_without_type_address():
    address = 'dos Andradas, 3000 Belo Horizonte'
    result = search(address)
    assert result == None
