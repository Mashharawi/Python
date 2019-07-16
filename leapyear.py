def is_leap(year):
    leap = False
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

year = int(input("Enter:     "))
x=is_leap(year)
print(x)
