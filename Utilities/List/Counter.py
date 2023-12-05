from collections import Counter

"""
Case 1
"""
list1 = ['a', 'a', 'b']
list1_freq = Counter(list1)
print(list1_freq)
# Counter({'a': 2, 'b': 1})
print(list1_freq['a'])
# 2

"""
Case 2
"""
list2 = ['a', 'a', 'b', 'c', 'a', 'a', 'd', 'c', 100]
list2_freq = Counter(list2)
list2_freq.most_common()
# [('a', 4), ('c', 2), ('b', 1), ('d', 1), (100, 1)]
list2_freq.most_common(3)
# [('a', 4), ('c', 2), ('b', 1)]

"""
Case 3
"""
def element_counter(obj, n_most_common=3):
  counter_obj = Counter(obj)
  top_elements = counter_obj.most_common(n_most_common)
  return top_elements

list2 = ['a', 'a', 'b', 'c', 'a', 'a', 'd', 'c', 100]
element_counter(list2)
# [('a', 4), ('c', 2), ('b', 1)]
