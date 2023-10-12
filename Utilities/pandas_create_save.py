# Initialize an empty DataFrame
df = pd.DataFrame()

# Create a dictionary 
my_dict = {"key_1": val_1, "key_2": val_2, "key_3", val_3} 
my_dict["key_1] # Access values of a dictionary 

# Create DataFrames from a list of dictionaries	- construct the df row by row
# Link: Convert_List_to_Dictionary.py
list_of_dict = [{"col_1": val_11, "col_2": val_21"}, {"col_1": val_12, "col_2": val_22"}]
my_df = pd.DataFrame(list_of_dict)
print(my_df)

# ***Create DataFrames from a dictionary of lists - construct the df column by column 
dict_of_list = {"col_1": [val_11, val_12], "col_2": [val_21, val_22]}
my_df = pd.DataFrame(list_of_dict)
print(my_df)

# Horizontally concatenate a new DataFrame to the old DataFrame
df_whole = pd.concat([df_old, df_new])

# Share DataFrames in the comma-separated values files
import pandas as pd
df = pd.read_csv("data.csv")  
print(df)

df["new_col"] = df["col_1"] / df["col_2"] * 1000
print(df)

df.to_csv("new_data.csv")
