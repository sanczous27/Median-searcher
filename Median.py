import calendar

expenses = {
    "2023-01": {
        "01": {
            "food": [ 22.11, 43, 11.72, 2.2, 36.29, 2.5, 19 ],
            "fuel": [ 210.22 ]
        },
        "09": {
            "food": [ 11.9 ],
            "fuel": [ 190.22 ]
        }
    },
    "2023-03": {
        "07": {
            "food": [ 20, 11.9, 30.20, 11.9 ]
        },
        "04": {
            "food": [ 10.20, 11.50, 2.5 ],
            "fuel": []
        }
    },
    "2023-04": {}
}
def chek_sunday(expenses):
    sundays = {}

    for year_month, days in expenses.items():
        for day in days.keys():
            year, month = map(int, year_month.split("-"))
            i_day = day
            day = int(day)
            if calendar.weekday(year, month, day) == 6:
                sundays[year_month] = i_day
                break


    return sundays

def solution1(expenses):
    first_sunday = []
    sundays = chek_sunday(expenses)
    median = {}
    for year, days in expenses.items():
            if year in sundays:
                for category, values in expenses[year][sundays[year]].items():
                    first_sunday.extend(values)

                first_sunday.sort()



            else:
                for day, categories in days.items():
                    for values in categories.values():
                        first_sunday.extend(values)

                first_sunday.sort()
            if first_sunday:
                first_sunday.sort()
                n = len(first_sunday)
                if n % 2 == 0:
                    the_median = (first_sunday[n // 2 - 1] + first_sunday[n // 2]) / 2
                else:
                    the_median = first_sunday[n // 2]
                median[year] = the_median
            else:
                median[year] = None
            first_sunday = []
    print(median)

    result = None
    return result

def solution2(expenses):
    result = None

    return result
solution1(expenses)
