# Process a file line by line at once
with open('trial.py') as f: # Notice that f is a generator
    for line in f:
        print(line)
# The with statement, also known as a context manager, ensures that the file is properly opened and closed, even if an exception occurs during file operations. 
# It helps with resource management and prevents common issues like forgetting to close the file.

# The following code is not good practice
f = open('trial.py', 'r')
for line in f:
    print(line)
f.close()

target_dictionary = {} 
# Open the input file for reading and the output file for writing
with open("trial_input.txt", 'r') as file1, open("trial_output.txt", 'w') as file2:
    for line1 in file1: 
        line11 = line1.rstrip("\n") # Remove the trailing newline character ('\n') from the end of the string line1
        words1 = line11.split("\t") # Splits the string line11 into a list of words or tokens using the tab character ('\t') as the delimiter.
        name = words1[0] 
        target = words1[1] + "\t" + words1[2]  
        target_dictionary[name] = target
        
# The file1 and file2 are automatically closed when we exit the 'with' block


# Process a file line by line on the fly
def read_large_file(file_object):
    """A generator function to read a large file."""

    # Loop indefinitely until the end of the file
    while True:
        # Read a line from the file: data
        line = file_object.readline()
        # Break if this is the end of the file
        if not line:
            break
        # Yield the line of data
        yield line
        
# Open a connection to the file
with open('large_data.csv') as file:
    gen_file = read_large_file(file)
    # Print the first three lines of the file
    print(next(gen_file))
    print(next(gen_file))
    print(next(gen_file))
