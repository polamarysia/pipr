from country import Country, reading, writing


def test_create_country():
    country = Country("Poland", 10000, 20000, 99, 100)
    assert country.name == "Poland"
    assert country.surface == 10000
    assert country.population == 20000
    assert country.running_water == 99
    assert country.people_older_100 == 100


def test_create_country_parameterless():
    country = Country("Poland", 10000, 20000)
    assert country.name == "Poland"
    assert country.surface == 10000
    assert country.population == 20000
    assert country.running_water is None
    assert country.people_older_100 is None


def test_reading():
    countries = [{
        "country": "Poland",
        "surface": 10000,
        "population": 20000,
        "households with running water": 99,
        "people old than 100": 100
    }]
    data = reading(countries)
    country = data[0]
    assert country.name == "Poland"
    assert country.surface == 10000
    assert country.population == 20000
    assert country.running_water == 99
    assert country.people_older_100 == 100


def test_reading_paramaterless():
    countries = [{
        "country": "Poland",
        "surface": 10000,
        "population": 20000
    }]
    data = reading(countries)
    country = data[0]
    assert country.name == "Poland"
    assert country.surface == 10000
    assert country.population == 20000
    assert country.running_water is None
    assert country.people_older_100 is None


def test_writing():
    country1 = Country("Poland", 10000, 20000)
    country2 = Country("Poland2", 20000, 20000, 99, 100)
    countries = [country1, country2]
    data = writing(countries)
    test_data = [{
        "country": "Poland",
        "surface": 10000,
        "population": 20000
    },
    {
        "country": "Poland",
        "surface": 10000,
        "population": 20000,
        "households with running water": 99,
        "people old than 100": 100
    }]
    assert data == test_data
