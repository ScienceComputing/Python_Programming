from datetime import date
birthdate_list = ['03/09/1998', '12/07/2000']

birthdate_list_2 = [date(1998, 3, 9), date(2000, 12, 7)]
print(birthdate_list_2[1].year) # 2000
print(birthdate_list_2[1].month) # 12
print(birthdate_list_2[1].day) # 7

print(birthdate_list_2[1].weekday()) # Find the weekday of a date
# Weekdays in python: 0 -> Monday, 1 -> Tuesday, ..., 6 -> Sunday

