pip install openpyxl
import pandas as pd
dict_1 = {'var_1': [1, 8, 9], 'var_2': [7, 12, 23], 'var_3': [23, 99, 6]}
df = pd.DataFrame(data=dict_1, index=(['idx_1', 'idx_2', 'idx_3']))
df.to_excel('temp.xlsx', sheet_name='frequency')
