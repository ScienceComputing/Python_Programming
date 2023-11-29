# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes

from datetime import date

print(date(2023, 10, 9))
# 2023-10-09 # This is the ISO 8601 format of a date (YYYY-MM-DD)

print(date(2023, 10, 9).isoformat())
# 2023-10-09

type(date(2023, 10, 9))
# <class 'datetime.date'>

type(date(2023, 10, 9).isoformat())
# <class 'str'>

print(date(2023, 10, 9).strftime('%Y/%m/%d'))
# 2023/10/09

print(date(2023, 10, 9).strftime('%Y%b%d'))
# 2023Oct09
