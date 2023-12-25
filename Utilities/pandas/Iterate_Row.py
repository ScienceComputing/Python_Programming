import pandas as pd
import numpy as np

num_rows = 10000
num_columns = 20
data = np.random.rand(num_rows, num_columns)
column_names = [f"Column_{i+1}" for i in range(num_columns)]
df = pd.DataFrame(data, columns=column_names)
print(df.head())

df_generator = df.iterrows()
first_row = next(df_generator)
second_row = next(df_generator)
print(first_row, second_row)

for idx, vals in df_generator:
    if (idx%2) != 0:
        val_sum = sum([vals[0], vals[1], vals[2], vals[3], vals[4]])/5
        print(val_sum)


# Case study: select patients with Stage 1/2 hypertension using .iterrows()
# Reference: https://www.health.harvard.edu/heart-health/a-look-at-diastolic-blood-pressure
data = {'Patient ID': [1, 2, 3, 4, 5],
        'Age': [35, 42, 28, 50, 62],
        'Gender': ['M', 'F', 'M', 'F', 'F'],
        'Diagnosis': ['Diabetes', 'Hypertension', 'Asthma', 'Cancer', 'Arthritis'],
        'BMI': [25.5, 22.3, 28.1, 20.2, 31.7],
        'Systolic Blood Pressure': [130, 120, 145, 110, 155],
        'Diastolic Blood Pressure': [80, 70, 90, 65, 100],
        'Cholesterol': [200, 180, 240, 160, 220],
        'Smoker': [True, False, True, False, False]}

df = pd.DataFrame(data)

# Approach 1:
import time
t0 = time.time()
stage1_hypertension_patients = []
stage2_hypertension_patients = []
for _, row in df.iterrows():
  systolic_bp = row['Systolic Blood Pressure']
  diastolic_bp = row['Diastolic Blood Pressure']
  if (130 <= systolic_bp <= 139) or (80 <= diastolic_bp <= 89):
    stage1_hypertension_patients.append(row['Patient ID'])
  elif (systolic_bp >= 140) or (diastolic_bp >= 90):
    stage2_hypertension_patients.append(row['Patient ID'])

print("Patients with Stage 1 Hypertension have the following IDs:")
print(stage1_hypertension_patients) # [1]
print("Patients with Stage 2 Hypertension have the following IDs:")
print(stage2_hypertension_patients) # [3, 5]
t1 = time.time() 
t1 - t0 # 0.007513761520385742 seconds

# Approach 2:
t0 = time.time()
stage1_hypertension_patients = []
stage2_hypertension_patients = []
def is_stage1_hypertension(row):
  systolic_bp = row['Systolic Blood Pressure']
  diastolic_bp = row['Diastolic Blood Pressure']
  return (130 <= systolic_bp <= 139) or (80 <= diastolic_bp <= 89)

def is_stage2_hypertension(row):
  systolic_bp = row['Systolic Blood Pressure']
  diastolic_bp = row['Diastolic Blood Pressure']
  return (systolic_bp >= 140) or (diastolic_bp >= 90)

stage1_hypertension_patients = df[df.apply(is_stage1_hypertension, axis=1)]['Patient ID'].tolist()
stage2_hypertension_patients = df[df.apply(is_stage1_hypertension, axis=1)]['Patient ID'].tolist()

print("Patients with Stage 1 Hypertension have the following IDs:")
print(stage1_hypertension_patients) 
print("Patients with Stage 2 Hypertension have the following IDs:")
print(stage2_hypertension_patients)
t1 = time.time() 
t1 - t0 # 0.011487960815429688 seconds
