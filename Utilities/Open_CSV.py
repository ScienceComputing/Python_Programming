import csv

"""Case: If a CSV file has only 2 columns without column headers"""
features = []
with open('variable_dictionary.csv') as f:
    r = csv.reader(f) # A reader returns lists
    for f1_val, f2_val in f: # this file only has 2 columns
        # f1_val, f2_val = line.rstrip().split(','); no need to write this anymore
        features.append({"variable": f1_val, "code": f2_val})

for feature in sorted(features, key=lambda feature : feature['variable']): 
    print(f"{feature['variable']} is coded as follows: {feature['code']}")

"""Case: If a CSV file more than 2 columns without column headers"""
features = []
with open('variable_dictionary.csv') as f:
    r = csv.reader(f)
    for row in f: # this file has more than 2 columns
        features.append({"variable": row[0], "code": row[2]})

for feature in sorted(features, key=lambda feature : feature['variable']): 
    print(f"{feature['variable']} is coded as follows: {feature['code']}")

"""Case: If a CSV file more than 2 columns with column headers: variable name, variable type, code"""
# csv.DictReader is robust against changing the orders of columns; while csv.reader is sensitive to this.
features = []
with open('variable_dictionary.csv') as f:
    r = csv.DictReader(f)
    for row in f: 
        features.append({"variable": row['variable name'], "code": row['code']})

for feature in sorted(features, key=lambda feature : feature['variable']): 
    print(f"{feature['variable']} is coded as follows: {feature['code']}")

