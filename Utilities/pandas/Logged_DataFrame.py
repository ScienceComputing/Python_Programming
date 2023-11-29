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

# Turn created_at into a read-only attribute
class LoggedDF2(pd.DataFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._created_at = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    @property  
    def created_at(self):
        return self._created_at

custom_data = {"A": [10, 20], "B": [30, 40]}
custom_df = LoggedDF2(custom_data)
print(custom_df.created_at)
custom_df.created_at = '2023 Nov 01' 
# AttributeError: property 'created_at' of 'LoggedDF2' object has no setter
