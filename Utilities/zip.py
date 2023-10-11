# zip accepts an arbitrary number of iterables and returns an iterator of tuples.
# Case 1: 
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zip_iterator = zip(list1, list2) # Create a zip iterator by using the zip function
result_list = list(zip_iterator)
print(result_list)
# [(1, 'a'), (2, 'b'), (3, 'c')]
print(*zip_iterator) # Print all the elements
# (1, 'a') (2, 'b') (3, 'c')

for z1, z2 in zip(list1, list2):
    print(z1, z2)
# 1 a
# 2 b
# 3 c

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
