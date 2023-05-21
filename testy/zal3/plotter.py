from matplotlib import pyplot as plt
import country

plotter_label = {
    1: "Surface",
    2: "Population",
    3: "Households with running water",
    4: "People old than 100"
}


def plotter(number_data, number_plotter, data):
    if number_plotter == 1:
        plotter_pie(number_data, data)
    elif number_plotter == 2:
        plotter_bar_vernical(number_data, data)
    elif number_plotter == 3:
        plotter_bar_horizontal(number_data, data)


def plotter_pie(number_data, data):
    x, labels = data_number(number_data, data)
    plt.pie(x, labels=labels)
    plt.title(label=plotter_label[number_data])
    plt.show()


def plotter_bar_vernical(number_data, data):
    x, labels = data_number(number_data, data)
    plt.bar(labels, x)
    plt.title(label=plotter_label[number_data])
    plt.show()


def plotter_bar_horizontal(number_data, data):
    x, labels = data_number(number_data, data)
    plt.barh(labels, x)
    plt.title(label=plotter_label[number_data])
    plt.show()


def data_number(number_data, countries):
    x = []
    labels = []
    if number_data == 1:
        for country in countries:
            x.append(country.surface)
            labels.append(country.name)
    elif number_data == 2:
        for country in countries:
            x.append(country.population)
            labels.append(country.name)
    elif number_data == 3:
        for country in countries:
            if country.running_water is not None:
                x.append(country.running_water)
                labels.append(country.name)
    elif number_data == 4:
        for country in countries:
            if country.people_older_100 is not None:
                x.append(country.people_older_100)
                labels.append(country.name)
    return x, labels


if __name__ == "__main__":
    country1 = country.Country("Poland", 10000, 20000)
    country2 = country.Country("Poland2", 20000, 20000, 99, 100)
    countries = [country1, country2]
    plotter_bar_horizontal(3, countries)
