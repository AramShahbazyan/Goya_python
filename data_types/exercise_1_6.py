# The program has a month and a year of two dates.
# The user enters another date (month and year only).
# Determine if the third date ranges from the first date to the second, inclusive.
# Solve the problem using dict.

import datetime

dates = {
    "start_date": datetime.date(2020, 2, 1),
    "end_date": datetime.date(2022, 2, 1)
}
try:
    year = int(input('input year: '))
    month = int(input('input month: '))
    input_date = datetime.date(year, month, 1)
    if dates["end_date"] >= input_date >= dates["start_date"]:
        print(f'{input_date.strftime("%b" " " "%Y")} in our range')
    else:
        print(f'{input_date.strftime("%b" " " "%Y")} out of our range')
except:
    print('year range 1-9999, month range 1-12')
