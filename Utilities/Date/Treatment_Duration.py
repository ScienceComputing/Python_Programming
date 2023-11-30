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
