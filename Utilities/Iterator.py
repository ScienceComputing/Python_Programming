# Iterable: a Python object which can be iterated over in a loop, and has an iter() method. 
# Examples of iterables include lists, sets, tuples, dictionaries, strings, range objects, file connections, etc. 
# All iterators are also iterable. 
# However, every iterable is not necessarily an iterator. 
# An iterable produces an iterator only once it is iterated on.
# An iterator produces the next value with its associated method called next().

# Iterate over an iterable
word = 'T cell'
it = iter(word)
next(it)
print(*it) # Print all elements in an iterator

# Iterate over a list
for element_i in element_list:
    print(element_i)

# Iterate over a string
for character_i in a_long_string:
    print(character_i)

# Iterate over a range sequence
for number_i in range(0, 9):
    print(number_i)

# Iterate over a dictionary
aa_dict = {'Alanine': 'Ala', 'Cysteine': 'Cys'}
for key, value in aa_dict.items():
    print(key, value)

# Iterate over a file connection
file = open('aa.txt')
it = iter(file)
print(next(it)) # Output the first line
print(next(it)) # Output the second line

