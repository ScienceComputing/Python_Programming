# France has 12 time zones
# https://www.guinnessworldrecords.com/world-records/584626-country-with-the-most-time-zones
from datetime import datetime, timedelta, timezone

NYC_ET = timezone(timedelta(hours=-5)) #!
print(NYC_ET)
# UTC-05:00

NYC_time = datetime(2023, 6, 7, 6, 6, 6, tzinfo=NYC_ET) #!
print(NYC_time)
# 2023-06-07 06:06:06-05:00 # 5-hour UTC offset

NYC_time_2 = NYC_time.astimezone(NYC_ET)
print(NYC_time_2)
# 2023-06-07 06:06:06-05:00

"""
Recommend
"""
# The Internet Assigned Numbers Authority (IANA) time zone data is refreshed approximately every 3-4 months to accommodate various jurisdictional adjustments to their time-related regulations and to incorporate newly discovered historical information about time zones.
from datetime import datetime
from dateutil import tz # Import tz class from the package dateutil
NYC_ET_2 = tz.gettz('America/New_York') # Continent/City
NYC_time_3 = datetime(2023, 6, 7, 6, 6, 6, tzinfo=NYC_ET_2)
print(NYC_time_3)
# 2023-06-07 06:06:06-04:00 # The UTC offset is adjusted, as the clock in NYC changes twice a year.

UTC_time = datetime(2023, 6, 7, 6, 6, 6)
print(UTC_time)
# 2023-06-07 06:06:06

UTC_time_2 = datetime(2023, 6, 7, 6, 6, 6, tzinfo=timezone.utc)
print(UTC_time_2)
# 2023-06-07 06:06:06+00:00

Paris_CET = timezone(timedelta(hours=1))
Paris_time = datetime(2023, 6, 7, 6, 6, 6, tzinfo=Paris_CET) 
print(Paris_time)
# 2023-06-07 06:06:06+01:00

print(datetime(2023, 6, 7, 6, 6, 6).replace(tzinfo=Paris_CET))
# 2023-06-07 06:06:06+01:00
# When set the timezone information of the datetime object to a new timezone (e.g., Paris_CET), we keep the same clock time.

print(Paris_time.astimezone(timezone.utc))
# 2023-06-07 05:06:06+00:00
# When we adjust the timezone using astimezone(), both the UTC offset (+00:00) and the clock time (05:06:06) are adjusted to match the new timezone (UTC). 

"""
Update all outpatient datetimes to Paris time
"""
from dateutil import tz

paris_tz = tz.gettz('Europe/Paris')

outpatient_datetimes_strings = [
    "2023-11-01 08:30:00",
    "2023-11-02 10:45:00",
    "2023-11-03 14:20:00",
]

updated_outpatient_datetimes = []

for dt_string in outpatient_datetimes_strings:
    dt = datetime.strptime(dt_string, "%Y-%m-%d %H:%M:%S")
    dt_paris = dt.replace(tzinfo=paris_tz)
    updated_outpatient_datetimes.append(dt_paris)

for dt_paris in updated_outpatient_datetimes:
    print(f"Outpatient Datetime in Paris Time: {dt_paris}")


