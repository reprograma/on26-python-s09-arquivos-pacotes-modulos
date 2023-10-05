from useful_data.age_calculation import calculate_age
from useful_data.leap_year import is_leap_year
from useful_data.formate_date import format_date

date_of_birth_str = input("Enter your date of birth in DD/MM/YYYY format: ")

age = calculate_age(date_of_birth_str)
if age is not None:
    print(f"Age is: {age} years")
else:
    print("Invalid date format. Use the format DD/MM/YYYY.")

if is_leap_year(2023):
    print("It's a leap year")
else:
    print("It's not a leap year")

formatted_date = format_date(date_of_birth_str)
print(f'Formatted date: {formatted_date}')