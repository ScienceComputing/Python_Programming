# Sets are useful for finding all the unique values in a column of the data, a list of elements, or rows from a file.

# See the length of a set = number of unique elements
print(len(set(['a', 'a', 'b', 'c']))) # 3

# Convert a tuple to a set
t = (5, 7, 9)
s = set(t)
s
type(s) # <class 'set'>
