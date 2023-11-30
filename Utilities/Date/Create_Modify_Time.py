# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
# %Y: 4 digit year (0000-9999)
# %m: 2 digit month (1-12)
# %d: 2 digit day (1-31)
# %H: 2 digit hour (0-23)
# %M: 2 digit minute (0-59)
# %S: 2 digit second (0-59)


# import datetime class from the datetime package
from datetime import datetime

dt = datetime(year=2023, month=1, day=6, hour=14, minute=30, second=25, microsecond=500000)
# 0.5 second = 500000 microseconds
print(dt)
# 2023-01-06 14:30:25.500000
print(dt.strftime('%Y-%b-%d'))
# 2023-Jan-06
print(dt.strftime('%Y-%b-%d %H:%M:%S'))
# 2023-Jan-06 14:30:25

dt_2 = dt.replace(minute=18, second=9, microsecond=0)
print(dt_2)
# 2023-01-06 14:18:09

# Parse string into datetime
dt_3 = datetime.strptime('2023-01-06 14:18:09', '%Y-%m-%d %H:%M:%S') 
print(dt_3)
# 2023-01-06 14:18:09

dt_4 = 19203489.0 # Number of seconds since January 1, 1970. 
print(datetime.fromtimestamp(dt_4))
# 1970-08-11 02:18:09
