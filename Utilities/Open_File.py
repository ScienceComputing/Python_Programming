# Process a file line by line at once
with open('trial.py') as f:
    for line in f:
        print(line)

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
