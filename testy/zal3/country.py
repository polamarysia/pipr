import json


class Country:
    """
    households_with_running_water / per 100 households
    people_older_100 / all people
    """
    def __init__(self, name, surface, population, households_with_running_water=None, people_older_100=None):
        self.name = name
        self.surface = surface
        self.population = population
        self.running_water = households_with_running_water
        self.people_older_100 = people_older_100


class Countries:
    def __init__(self, countries=None):
        if not countries:
            self.countries = []
        else:
            self.countries = countries

    def read_from_file(self, path):
        self.countries = reading(read_json(path))

    def write(self, path):
        write_json(writing(self.countries), path)


def read_json(path):
    with open(path, "r") as handle:
        return json.load(handle)


def write_json(data, path):
    with open(path, "w") as handle:
        json.dump(data, handle)


def reading(countries):
    data = []
    for country in countries:
        name = country["country"]
        surface = country["surface"]
        population = country["population"]
        running_water = country["households with running water"] if "households with running water" in country.keys() else None
        people_older_100 = country["people old than 100"] if "people old than 100" in country.keys() else None
        data.append(Country(name, surface, population, running_water, people_older_100))
    return data


def writing(data):
    countries = []
    for country in data:
        dict_country = {}
        dict_country["country"] = country.name
        dict_country["surface"] = country.surface
        dict_country["population"] = country.population
        if country.running_water is not None:
            dict_country["households with running water"] = country.running_water
        if country.people_older_100 is not None:
            dict_country["people old than 100"] = country.people_older_100
        countries.append(dict_country)
    return countries