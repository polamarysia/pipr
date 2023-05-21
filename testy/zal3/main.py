import plotter
import country

# Napisz program do rysowania wykresów dotyczących danych demograficznych dla różnych państw. Program ma umożliwiać:
# * wczytywanie i zapisywanie danych dotyczących państw z i do pliku w formacie JSON,
# * rysowanie wykresów dotyczących jednej cechy demograficznej.
# Każde z państw jest opisane zestawem cech. Część cech jest obowiązkowa
# (nazwa państwa, powierzchnia, liczba ludności). Inne cechy są opcjonalne
# i nie zawsze są dostępne dla każdego z państw (przykładowo: odsetek
# gospodarstw domowych posiadających wodę bieżącą, liczba osób w wieku ponad 100 lat, i tym podobne).
# Program powinien posiadać interfejs, w którym możemy podać argumenty takie jak:
# * nazwa pliku json, z którego wczytujemy dane,
# * rodzaju wykresu, który chcemy narysować (do wyboru: kołowy, słupkowy poziomy oraz pionowy),
# * cecha liczbowa, której dotyczy wykres.
# W przypadku wyboru cechy opcjonalnej należy uwzględnić tylko te kraje, dla których występują dane w pliku.


def main(path, plotter_number=1, data_number=1):
    """
    plotter_number = 1: pie, 2: bar, 3: barh
    data_number = 1: suface, 2: population, 3: running_water, 4: people_older_100
    users choose this
    """
    countries = country.Countries()
    countries.read_from_file(path)
    plotter.plotter(data_number, plotter_number, countries.countries)


if __name__ == "__main__":
    main("countries.json", 1, 2)