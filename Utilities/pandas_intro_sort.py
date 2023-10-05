df.head()

df.info() # this info method shows information on each of the columns, such as the data type and number of missing values

df.describe() # descriptive statistics

df.shape # shape is an attribute, not a method; so there is no parenthesis 

df.values # values attribute extracts the data values in 2-D numpy array

df.columns # columns attribute extracts the column names

df.columns = new_column # assign new column names

df.index # index attribute extracts the row names/numbers

df.sort_values("column_name", ascending=False) # change the order of the rows by sorting on the particular column

df.sort_values(["column_name_1", "column_name_2"]) # sort on the first column then on the second column

df.sort_values(["column_name_1", "column_name_2"],  ascending=[True, False]) # sort on the first column by ascending order then on the second column by decreasing order

df["column_name_1"] # select one column

df[["column_name_1", "column_name_2"]] # select multiple columns

cols_to_select = ["column_name_1", "column_name_2"] # select multiple columns
df[cols_to_select]

df["column_name_1"] > 50 # subset rows and return a logical column

df[df["column_name_1"] > 50] # subset rows and return a subsetted data frame

df[df["column_name_1"]  == "labrador"] # subset rows and return a subsetted data frame

df[df["column_name_1"]  < "2017-09-09"] # subset rows and return a subsetted data frame

is_lab = df["column_name_1"]  == "labrador"
is_lab2 = df["column_name_1"]  == "labrador2"
df[is_lab & is_lab2] # subset rows based on multiple conditions

df[(df["column_name_1"]  == "labrador") & (df["column_name_1"]  == "labrador2")] 

is_lab_or_lab2 = df["column_name_1"].isin(["labrador", "labrador"])
df[is_lab_or_lab2] # subset rows based on multiple values of a categorical variable
