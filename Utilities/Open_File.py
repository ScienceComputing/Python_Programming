# Reference:
# https://github.com/ScienceComputing/Python_Programming/blob/main/Utilities/String/*Remove_Character.py
# https://github.com/ScienceComputing/Python_Programming/blob/main/Python_Overview.ipynb
# https://docs.python.org/3/howto/sorting.html
# https://github.com/ScienceComputing/Python_Programming/blob/main/Utilities/Lambda_Function.py

"""
Case 1
"""
# Process a file line by line at once
with open('trial.py') as f: # Notice that f is a generator
    for line in f:
        print(line)
# The with statement, also known as a context manager, ensures that the file is properly opened and closed, even if an exception occurs during file operations. 
# It helps with resource management and prevents common issues like forgetting to close the file.

# The following code is not considered good practice, because it relies on explicitly calling f.close() to close the file. If an exception occurs before this line, the file might remain open, potentially leading to resource leaks or issues with subsequent file operations.
f = open('trial.py', 'r')
for line in f:
    print(line)
f.close()

with open('trial.py') as f: 
    lines = f.readlines() # lines is a list; each element of this list represents a line from the file.

for l in lines:
    print(l)

"""
Case 2
"""
with open('trial.csv') as f:
    for line in f:
        row = line.rstrip().split(',') # rstrip() removes the white space on the right side
        print(f"{row[0]} and {row[1]}")

"""
Case 2.1
"""
with open('trial.csv') as f:
    for line in f:
        feature1, feature2 = line.rstrip().split(',')
        print(f"{feature1} and {feature2}")

"""
Case 2.2
"""
features = []
with open('trial.csv') as f:
    for line in f:
        feature1, feature2 = line.rstrip().split(',')
        features.append(f"{feature1} and {feature2}")

for feature in sorted(features):
    print(feature)

"""
Case 2.3
"""
features = []
with open('trial.csv') as f:
    for line in f:
        f1_val, f2_val = line.rstrip().split(',')
        feature = {"feature 1": f1_val, "feature 2": f2_val}
        features.append(feature)

for feature in features:
    print(f"{feature['feature 1']} and {feature['feature 2']}")


"""
Case 2.4 - sort a list of dictionaries by the key/value
"""
features = []
with open('variable_dictionary.csv') as f:
    for line in f:
        f1_val, f2_val = line.rstrip().split(',')
        feature = {"variable": f1_val, "code": f2_val}
        features.append(feature)

def get_variable(feature):
    return feature['variable']

def get_code(feature):
    return feature['code']

for feature in sorted(features, key=get_variable): 
    print(f"{feature['variable']} is coded as follows: {feature['code']}")

for feature in sorted(features, key=get_code, reverse=True): 
    print(f"{feature['variable']} is coded as follows: {feature['code']}")

# Another way:
# Transform the list of dictionaries into a single dictionary, and then use lambda to sort this dictionary by key or value
features_dict = {feature["variable"]: feature["code"] for feature in features}
print(dict(sorted(features_dict.items(), key=lambda item : item[0])))
print(dict(sorted(features_dict.items(), key=lambda item : item[1])))

# An elegant solution:
for feature in sorted(features, key=lambda feature : feature['variable']): 
    print(f"{feature['variable']} is coded as follows: {feature['code']}")

"""
Case 3
"""
target_dictionary = {} 
# Open the input file for reading and the output file for writing
with open("trial_input.txt", 'r') as file1, open("trial_output.txt", 'w') as file2:
    for line1 in file1: 
        line11 = line1.rstrip("\n") # Remove the trailing newline character ('\n') from the end of the string line1
        words1 = line11.split("\t") # Splits the string line11 into a list of words or tokens using the tab character ('\t') as the delimiter.
        name = words1[0] 
        target = words1[1] + "\t" + words1[2]  
        target_dictionary[name] = target
    for name, target in target_dictionary.items():
        file2.write(f"{name}\t{target}\n")  # Write name and target to output file with a tab separator

# The file1 and file2 are automatically closed when we exit the 'with' block

"""
Case 4
"""
# Process a file line by line on the fly
def read_large_file(file_object):
    """A generator function to read a large file."""
    while True: # Read a line from the file: data
        line = file_object.readline()
        if not line:
            break # Break if this is the end of the file
        yield line # Yield the line of data
        
# Open a connection to the file
with open('large_data.csv') as file:
    gen_file = read_large_file(file)
    # Print the first three lines of the file
    print(next(gen_file))
    print(next(gen_file))
    print(next(gen_file))
