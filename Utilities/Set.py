# Sets [unordered, mutable] are useful for finding all the unique values in a column of the data, a list of elements, or rows from a file.

# Create a set
donut_consumed = ['Vanilla Sprinkle', 'Chocolate Sprinkle', 'Powder', 'Powder', 'Chocolate Sprinkle']
donut_type = set(donut_consumed)
print(donut_type)
# {'Vanilla Sprinkle', 'Chocolate Sprinkle', 'Powder'}


# See the length of a set = number of unique elements
print(len(set(['a', 'a', 'b', 'c']))) # 3

# Convert a tuple to a set
t = (5, 7, 9)
s = set(t)
s
type(s) # <class 'set'>
