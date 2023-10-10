# Iterable: a Python object which can be iterated over in a loop, and has an iter() method. 
# Examples of iterables include lists, sets, tuples, dictionaries, strings, range objects, file connections, etc. 
# All iterators are also iterable. 
# However, every iterable is not necessarily an iterator. 
# An iterable produces an iterator only once it is iterated on.
# An iterator produces the next value with next().

# Iterate over a list
for element_i in element_list:
    print(element_i)

# Iterate over a string
for character_i in a_long_string:
    print(character_i)

# Iterate over a range sequence
for number_i in range(0, 9):
    print(number_i)
