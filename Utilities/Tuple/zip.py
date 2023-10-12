# zip accepts an arbitrary number of iterables and returns an iterator of tuples.
# Case 1: 
list1 = ['cake1', 'cake2', 'cake3']
list2 = ['Vanilla Cake', 'Red Velvet Cake', 'Black Forest Cake']
zip_iterator = zip(list1, list2) # Create a zip iterator by using the zip function
full_list = list(zip_iterator)
print(full_list)
# [('cake1', 'Vanilla Cake'), ('cake2', 'Red Velvet Cake'), ('cake3', 'Black Forest Cake')]

zip_iterator = zip(list1, list2)
print(*zip_iterator) # Print all the elements
# ('cake1', 'Vanilla Cake') ('cake2', 'Red Velvet Cake') ('cake3', 'Black Forest Cake')

for z1, z2 in zip(list1, list2):
    print(z1, z2)
# cake1 Vanilla Cake
# cake2 Red Velvet Cake
# cake3 Black Forest Cake

zip_iterator = zip(list1, list2)
result1, result2 = zip(*zip_iterator)
print(result1) 
# (1, 2, 3)
print(result2) 
# ('a', 'b', 'c')

# Case 2: 
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zip_iterator = zip(list1, list2)
result_dict = dict(zip_iterator)
print(result_dict)
# {1: 'a', 2: 'b', 3: 'c'}
