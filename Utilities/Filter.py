"""Case 1"""
aa = ['histidine', 'isoleucine', 'leucine', 'lysine', 'methionine', 'phenylalanine', 'threonine', 'tryptophan', 'valine']
target_aa = filter(lambda member: len(member) > 9, aa)
print(list(target_aa))

import pandas as pd
import numpy as np

"""Case 2"""
data = {'Patient ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'Age': [35, 42, 28, 50, 62, 47, 31, 55, 25, 68],
        'Gender': ['M', 'F', 'M', 'F', 'F', 'M', 'M', 'F', 'F', 'M'],
        'Day of Visit': ['Monday', 'Tuesday', 'Monday', 'Wednesday', 'Friday', 'Monday', 'Tuesday', 'Wednesday', 'Monday', 'Friday'],
        'Systolic Blood Pressure': np.random.randint(100, 160, 10),
        'Diastolic Blood Pressure': np.random.randint(60, 90, 10),
        'Cholesterol': np.random.randint(150, 250, 10),
        'Glucose Level': np.random.randint(70, 120, 10)}
health_data = pd.DataFrame(data)

# Filter days where the count of patients with high cholesterol (>240) is greater than or equal to 1
high_cholesterol_days = health_data.groupby('Day of Visit').filter(lambda x: (x['Cholesterol'] > 240).sum() >= 1)
high_cholesterol_days[['Day of Visit', 'Cholesterol']]
#  Day of Visit  Cholesterol
# 0       Monday          184
# 1      Tuesday          242
# 2       Monday          180
# 5       Monday          246
# 6      Tuesday          170
# 8       Monday          230
