# Reference: https://docs.python.org/3/library/datetime.html#timedelta-objects
# datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
# A millisecond is converted to 1000 microseconds.
# A minute is converted to 60 seconds.
# An hour is converted to 3600 seconds.
# A week is converted to 7 days.

from datetime import datetime

datetime(2023, 6, 6, 8, 10, 22) - datetime(2023, 6, 5, 8, 10, 22)
# datetime.timedelta(days=1)
print(datetime(2023, 6, 6, 8, 10, 22) - datetime(2023, 6, 5, 8, 10, 22))
# 1 day, 0:00:00
time_diff = datetime(2023, 6, 6, 8, 10, 22) - datetime(2023, 6, 5, 8, 10, 22)
print(time_diff.total_seconds())
# 86400.0

from datetime import timedelta
day_diff = timedelta(days=1)
print(datetime(2023, 6, 5, 8, 10, 22) + day_diff)
# 2023-06-06 08:10:22

day_diff = timedelta(days=-1)
print(datetime(2023, 6, 6, 8, 10, 22) + day_diff)
# 2023-06-05 08:10:22

"""
Estimate the patients' treatment duration
"""
from datetime import datetime

fmt = "%Y-%m-%d %H:%M:%S"

treatment_times_strings = [
    ("2023-11-01 08:30:00", "2023-11-01 09:15:00"),
    ("2023-11-02 10:45:00", "2023-11-02 11:30:00"),
    ("2023-11-03 14:20:00", "2023-11-03 15:05:00"),
]

patient_treatment_durations = []

for (start, end) in treatment_times_strings:
    treatment = {
        'start': datetime.strptime(start, fmt),
        'end': datetime.strptime(end, fmt)
    }
    duration = treatment['end'] - treatment['start']
    treatment['duration'] = duration
    patient_treatment_durations.append(treatment)

for treatment in patient_treatment_durations:
    print(f"Treatment Duration: {treatment['duration']}")
