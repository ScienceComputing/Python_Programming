# Reverse a list
list_1 = ["a", 200, 300, "ccc", 500]
list_1.reverse()
print(list_1)
# [500, 'ccc', 300, 200, 'a']

# List comprehensions allow us to create lists from other lists or from columns of DataFrames, among many other objects. 
# Construct a list comprehension
# newlist = [expression for item in iterable if condition == True]
aa = ['histidine', 'isoleucine', 'leucine', 'lysine', 'methionine', 'phenylalanine', 'threonine', 'tryptophan', 'valine']
aa_target = [x for x in aa if "t" in x]
print(aa_target)
# ['histidine', 'methionine', 'threonine', 'tryptophan']

aa_target_2 = [x if x != 'phenylalanine' else 'methionine' for x in aa]
print(aa_target_2)
# ['histidine', 'isoleucine', 'leucine', 'lysine', 'methionine', 'methionine', 'threonine', 'tryptophan', 'valine']

