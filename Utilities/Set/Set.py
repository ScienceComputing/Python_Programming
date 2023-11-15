# Sets [unordered, mutable] are useful for finding all the unique values in a column of the data, a list of elements, or rows from a file.

# Create a set
donut_consumed = ['Vanilla Sprinkle', 'Chocolate Sprinkle', 'Powder', 'Powder', 'Chocolate Sprinkle']
donut_type = set(donut_consumed)
print(donut_type)
# {'Vanilla Sprinkle', 'Chocolate Sprinkle', 'Powder'}

# Convert a tuple to a set
t = (5, 7, 9)
s = set(t)
s
type(s) # <class 'set'>

# See the length of a set = number of unique elements
print(len(set(['a', 'a', 'b', 'c']))) # 3

# Add a single element
donut_type.add('Yeast')
print(donut_type)
# {'Yeast', 'Vanilla Sprinkle', 'Chocolate Sprinkle', 'Powder'}

donut_type.add('Chocolate Sprinkle')
print(donut_type)
# {'Yeast', 'Vanilla Sprinkle', 'Chocolate Sprinkle', 'Powder'}

# Merge a set with another set or list
more_donut = ['Glazed', 'Boston Cream', 'Cider']
donut_type.update(more_donut)
print(donut_type)
# {'Glazed', 'Cider', 'Powder', 'Chocolate Sprinkle', 'Yeast', 'Vanilla Sprinkle', 'Boston Cream'}

# Remove an element from a set
# Method 1: no error will happen if the value is not found
donut_type.discard('Cider')
print(donut_type)
# {'Glazed', 'Powder', 'Chocolate Sprinkle', 'Yeast', 'Vanilla Sprinkle', 'Boston Cream'}
donut_type.pop('Hole')

# Method 2: KeyError will happen if the set is empty
donut_type.pop
# 'Glazed'

# Set operations
set1.union(set2) # Return a union set
set1.intersection(set2) # Return an intersection set
set1.difference(set2) # Return a set with unique elemements in set1
set2.difference(set1) # Return a set with unique elemements in set2
set1 = {1, 2, 3, 4, 5} 
set2 = {4, 5, 6, 7, 8}
sym_diff = set1 ^ set2 # Return a set of elements that are in either of the sets but not in their intersection
print("Symmetric difference using ^:", sym_diff)
# Symmetric difference using ^: {1, 2, 3, 6, 7, 8}


