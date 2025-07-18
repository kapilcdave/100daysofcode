year = int(input("how many years?"))
days = 365 * year
hours = days * 24
minutes = hours * 60
seconds = minutes * 60
if year >= 4:
    print("There is at least 1 leap year...loading")
    leap_years = year // 4 - year // 100 + year // 400
    days2 = days + leap_years
    print(f"With leap years: {days2} days, {days2 * 24} hours, {days2 * 24 * 60} minutes, {days2 * 24 * 60 * 60} seconds.")
else:
    print(f"Without leap years: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds.")