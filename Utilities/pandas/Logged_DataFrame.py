import pandas as pd
from datetime import datetime

class LoggedDF(pd.DataFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.created_at = datetime.today().strftime('%Y-%m-%d %H:%M:%S')

custom_data = {"A": [10, 20], "B": [30, 40]}
custom_df = LoggedDF(custom_data)

print(custom_df.values)
print(custom_df.created_at)

# Recap: create DataFrames from a dictionary of lists - construct the df column by column 
dict_of_list = {"col_1": [val_11, val_12], "col_2": [val_21, val_22]}
my_df = pd.DataFrame(list_of_dict)
print(my_df)
