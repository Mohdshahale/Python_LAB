
def is_leap_year(year):
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)

year1 = int(input("Enter the first year: "))
year2 = int(input("Enter the second year: "))

print(f"Leap years between {year1} and {year2} are:")
for year in range(year1, year2 + 1):
    if is_leap_year(year):
        print(year)
