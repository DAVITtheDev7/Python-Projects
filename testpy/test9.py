month_year = input("Enter month and year (MM-YYYY): ")

month, year = map(int, month_year.split("-"))


century = year // 100
year_in_century = year % 100

leap = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
num_days_in_month = [31, 28 + leap, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if month == 2:
    if leap:
        num_days_in_month[1] = 29
    else:
        num_days_in_month[1] = 28
    year_in_century -= 1
    if year_in_century < 0:
        year_in_century += 100
        century -= 1

day_of_week = (1 + ((11*(month+1))//5) + year_in_century + (year_in_century//4) + (century//4) - (2*century)) % 7

month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

print(month_names[month - 1], year)

print("Mo Tu We Th Fr Sa Su")
if month == 2 and leap :
    for i in range(day_of_week+3):
        print("   ", end="")

    for day in range(1, num_days_in_month[month - 1] + 1):
        print("{:2d}".format(day), end=" ")
        if (day + day_of_week-4) % 7 == 0:
            print()

    if (num_days_in_month[month - 1] + day_of_week) % 7 != 0:
        print()
else:
    for i in range(day_of_week):
        print("   ", end="")

    for day in range(1, num_days_in_month[month - 1] + 1):
        print("{:2d}".format(day), end=" ")
        if (day + day_of_week) % 7 == 0:
            print()

if (num_days_in_month[month - 1] + day_of_week) % 7 != 0:
    print()