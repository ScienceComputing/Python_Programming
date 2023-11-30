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

