from collections import Counter
list1 = ['a', 'a', 'b']
list1_freq = Counter(list1)
print(list1_freq)
# Counter({'a': 2, 'b': 1})
print(list1_freq['a'])
# 2

list2 = ['a', 'a', 'b', 'c', 'a', 'a', 'd', 'c', 100]
list2_freq = Counter(list2)
list2_freq.most_common()
# [('a', 4), ('c', 2), ('b', 1), ('d', 1), (100, 1)]
list2_freq.most_common(3)
# [('a', 4), ('c', 2), ('b', 1)]
