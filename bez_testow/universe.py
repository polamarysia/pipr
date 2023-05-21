import math


# W dwuwymiarowym wszechświecie trwa wojna pomiędzy planetami przy użyciu broni laserowej.
# Broń laserowa wysyła wiązkę w linii prostej i niszczy wszystkie planety na swojej drodze
# oraz w promieniu R od linii wiązki. Zasięg wiązki laserowej jest nieograniczony i nie jest
# ona zatrzymywana przez żadne planety będące na jej drodze. Napisz program, który na podstawie:
# nazw dwóch planet (np. A i B) i promienia R zwróci nazwy planet, które zostaną zniszczone w przypadku
# gdy planeta A wyśle wiązkę laserową w kierunku planety B, a planeta B wyśle wiązkę laserową w kierunku planety A.


laser_planets = {
    "ziemia": (2, 4),
    "mars": (3, 6)
    }

planets = {
    "wenus": (9, 0),
    "jowisz": (5, 6),
    "merkury": (2, 5),
    "saturn": (4, 8),
    "neptun": (0, 5),
    "uran": (0, 6),
    "xyz": (0, 4)
}


def reduction(name1, name2, radius):
    "prosta"
    line_between = line(laser_planets[name1], laser_planets[name2])
    "lista zniszczonych planet"
    destroyed_planets = [name1, name2]
    for planet, coordinates in planets.items():
        distance = planet_distance(coordinates, line_between)
        if destroyed(distance, radius):
            "dodanie zniszczonej planety"
            destroyed_planets.append(planet)
    return destroyed_planets


def line(coordinates1, coordinates2):
    "zwraca krotki prostej ax+by+c=0 (a, b, c)"
    if coordinates1[0] == coordinates2[0]:
        return (1, 0, -coordinates2[0])
    else:
        x1, y1 = coordinates1
        x2, y2 = coordinates2
        a = (y1-y2)/(x1-x2)
        c = y1 - x1*a
        return (a, -1, c)


def planet_distance(coordinates, line):
    "zwraca odległość planety od prostej"
    x, y = coordinates
    a, b, c = line
    denominator = a*x+b*y+c
    if denominator < 0:
        denominator = -denominator
    numerator = math.sqrt(a**2+b**2)
    return denominator/numerator


def destroyed(distance, radius):
    "zwraca czy planeta została zniszczona"
    return distance <= radius


if __name__ == "__main__":
    print(reduction("ziemia", "mars", 2))
