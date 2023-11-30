# France has 12 time zones
# https://www.guinnessworldrecords.com/world-records/584626-country-with-the-most-time-zones
from datetime import datetime, timedelta, timezone

NYC_ET = timezone(timedelta(hours=-5)) #!
print(NYC_ET)
# UTC-05:00

UTC_time = datetime(2023, 6, 7, 6, 6, 6)
print(UTC_time)
# 2023-06-07 06:06:06

UTC_time_2 = datetime(2023, 6, 7, 6, 6, 6, tzinfo=timezone.utc)
print(UTC_time_2)
# 2023-06-07 06:06:06+00:00

NYC_time = datetime(2023, 6, 7, 6, 6, 6, tzinfo=NYC_ET) #!
print(NYC_time)
# 2023-06-07 06:06:06-05:00 # 5-hour UTC offset

NYC_time_2 = NYC_time.astimezone(NYC_ET)
print(NYC_time_2)
# 2023-06-07 06:06:06-05:00

Paris_CET = timezone(timedelta(hours=1))
Paris_time = datetime(2023, 6, 7, 6, 6, 6, tzinfo=Paris_CET) 
print(Paris_time)
# 2023-06-07 06:06:06+01:00

print(datetime(2023, 6, 7, 6, 6, 6).replace(tzinfo=Paris_CET))
# 2023-06-07 06:06:06+01:00
