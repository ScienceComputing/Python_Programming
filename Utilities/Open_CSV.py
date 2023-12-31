import csv

# If a CSV file has only 2 columns
features = []
with open('variable_dictionary.csv') as f:
    r = csv.reader(f)
    for f1_val, f2_val in f: # this file only has 2 columns
        # f1_val, f2_val = line.rstrip().split(','); no need to write this anymore
        features.append({"variable": f1_val, "code": f2_val})


# If a CSV file more than 2 columns
features = []
with open('variable_dictionary.csv') as f:
    r = csv.reader(f)
    for row in f: # this file has more than 2 columns
        features.append({"variable": row[0], "code": row[2]})
