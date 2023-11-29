from datetime import date
birthdate_list = ['03/09/1998', '12/07/2000']

birthdate_list_2 = [date(1998, 3, 9), date(2000, 12, 7)]
print(birthdate_list_2[1].year) # 2000
print(birthdate_list_2[1].month) # 12
print(birthdate_list_2[1].day) # 7

print(birthdate_list_2[1].weekday()) # Find the weekday of a date
# Weekdays in python: 0 -> Monday, 1 -> Tuesday, ..., 6 -> Sunday

"""
Count how many patients were born before June 1
"""
from datetime import datetime
patient_birthdates = [
    "1995-01-15",
    "1987-07-10",
    "2000-06-30",
    "1992-12-20",
    "1985-05-12"
]

birthdates = [datetime.strptime(i, "%Y-%m-%d") for i in patient_birthdates] # Convert birthdate strings to datetime objects

early_birthdays = 0
for birthdate in birthdates:
    if birthdate.month < 6 or (birthdate.month == 6 and birthdate.day < 1):
        early_birthdays += 1

print(f"There are {early_birthdays} patients born before June 1") # There are 2 patients born before June 1

"""
Count patients born in each calendar month
"""
from datetime import date
from collections import defaultdict

patient_birthdates = [
    date(1990, 1, 15),
    date(1992, 3, 20),
    date(1995, 6, 10),
    date(1990, 1, 25),
    date(1992, 3, 5)
]

patients_each_month = defaultdict(int)

for birthdate in patient_birthdates:
    month = birthdate.month
    patients_each_month[month] += 1

for month, count in patients_each_month.items():
    print(f"Patients born in month {month}: {count}")


