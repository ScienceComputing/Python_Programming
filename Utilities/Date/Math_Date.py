from datetime import date

"""
Minimum date
"""
birthdate_list = [date(1998, 3, 9), date(2000, 12, 7)]
print(min(birthdate_list))
# 1998-03-09

"""
Duration
"""
(date(2000, 12, 7) - date(1998, 3, 9)).days
# 1004

"""
Add days
"""
from datetime import timedelta

print(date(1998, 3, 9) + timedelta(days=1004))
# 2000-12-07

"""
Add hours
"""
time_1 = datetime(2017, 3, 12, tzinfo = tz.gettz('America/New_York'))
time_2 = time_1 + timedelta(hours=7)
print(time_1) 
# 2017-03-12 00:00:00-05:00
print(time_2)
# 2017-03-12 07:00:00-04:00

# How many hours between time_2 and time_1?
print((time_2 - time_1).total_seconds()/(3600))
# 7
