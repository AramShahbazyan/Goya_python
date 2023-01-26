# Enter a date from the keyboard (for example, 1986).
# Decide whether the year entered by the user is a leap year or not.

year = int(input('please input year: '))
if year % 4 == 0:
    print(f'{year} is a leap year')

else:
    print(f'{year} is not a leap year')