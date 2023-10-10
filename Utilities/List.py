# Reverse a list
list_1 = ["a", 200, 300, "ccc", 500]
list_1.reverse()
print(list_1)
# [500, 'ccc', 300, 200, 'a']

# List comprehensions allow us to create lists from other lists or from columns of DataFrames, among many other objects.
# It is a single line of code, and more efficient than a for loop.
# Construct a list comprehension
# newlist = [expression for item in iterable if condition == True]
# Case 1:
nums = [2, 8, 10, 1, 21, 60]
nums_minus_1 = [num + 1 for num in nums]
print(nums_minus_1) 
# [3, 9, 11, 2, 22, 61]

# Case 2:
aa = ['histidine', 'isoleucine', 'leucine', 'lysine', 'methionine', 'phenylalanine', 'threonine', 'tryptophan', 'valine']
aa_target = [x for x in aa if "t" in x]
print(aa_target)
# ['histidine', 'methionine', 'threonine', 'tryptophan']

# Case 3:
aa_target_2 = [x if x != 'phenylalanine' else 'methionine' for x in aa]
print(aa_target_2)
# ['histidine', 'isoleucine', 'leucine', 'lysine', 'methionine', 'methionine', 'threonine', 'tryptophan', 'valine']

