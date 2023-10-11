# Case 1: process the first 500 rows of a file line by line, to create a dictionary of the counts of how many times each country appears in a column in the dataset.
# Open a connection to a target file using a context manager 'with' statement, ensuring that resources are efficiently allocated when opening a connection to a file.
with open('world_dev_ind.csv') as file:
    
    # Skip the column names
    file.readline()

    # Initialize an empty dictionary: counts_dict
    counts_dict = {}

    # Process only the first 500 rows
    for j in range(0,500):

        #! Split the current line into a list: line
        line = file.readline().split(',')

        #! Return the value for the first column; in this case, it is the country name
        first_col_val = line[0] 

        # If the column value is in the dict, increment its value
        if first_col_val in counts_dict.keys():
            counts_dict[first_col_val] += 1

        # Else, add to the dict and set value to 1
        else:
            counts_dict[first_col_val] = 1

print(counts_dict)
