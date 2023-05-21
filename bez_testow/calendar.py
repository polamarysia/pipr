
# Napisz program, który dla zadanego roku będzie wypisywać na ekran ładnie
# sformatowany kalendarz dla danego roku. Wiersze powinny zawierać numery
# dni miesiąca dla kolejnych tygodni. Poszczególne miesiące powinny być
# od siebie odseparowane. Należy zadbać o estetyczne formatowanie.

months = {
    "styczen": 31,
    "luty": (28, 29),
    "marzec": 31,
    "kwiecien": 30,
    "maj": 31,
    "czerwiec": 30,
    "lipiec": 31,
    "sierpien": 31,
    "wrzesien": 30,
    "pazdziernik": 31,
    "listopad": 30,
    "grudzien": 31
}

day_name = {
    1: "poniedzialek",
    2: "wtorek",
    3: "sroda",
    4: "czwartek",
    5: "piatek",
    6: "sobota",
    0: "niedziela"
}
# niedziela jest 0 bo jest to wynik 7 % 7

orient_day = {"2022": 6}


def leap_year(year):
    "czy rok przestepny"
    if year % 4 == 0:
        return True
    else:
        return False


def calendar(year):
    "tworzenie kalendarza"
    leap = leap_year(year)
    first = first_jun(year)
    calendar = f"\n{year}\n\n"
    for month, days in months.items():
        if leap and month == "luty":
            days = days[1]
        elif not leap and month == "luty":
            days = days[0]
        calendar += f"{month}\n\nndz\t pn\t wt\t sr\t cz\t pt\t sb\n"
        month_array = fill_array(days, first)
        first = first_month(first, days)
        for week in month_array:
            for day in week:
                if day == 0:
                    calendar += "\t"
                else:
                    calendar += f"{day}\t"
            calendar += '\n\n'
    return calendar


def first_month(first, days):
    "obliczanie pierwszego dnia miesiąca"
    rest = days % 7
    first += rest
    return first % 7


def fill_array(days, first):
    "tworzenie tablicy dni danego miesiąca"
    month = []
    day = 1
    week = []
    while day < days+1:
        if day == 1:
            while len(week) < first:
                week.append(0)
        week.append(day)
        if len(week) == 7:
            month.append(week)
            week = []
        if day == days:
            month.append(week)
        day += 1
    return month


def first_jun(year):
    "oblicznie pierwszego stycznia"
    if year == 2022:
        first_jun = 6
    elif year < 2022:
        dif = 2022 - year
        whole = dif // 4
        rest = dif % 4
        if rest > 1:
            first_jun = (6 - dif - whole - 1) % 7
        else:
            first_jun = (6 - dif - whole) % 7
    else:
        dif = year - 2022
        whole = dif // 4
        rest = dif % 4
        if rest == 3:
            first_jun = (6 + dif + whole + 1) % 7
        else:
            first_jun = (6 + dif + whole) % 7
    return first_jun


if __name__ == "__main__":
    print(calendar(1966))
