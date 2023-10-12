tup = zip(list1, list2)
df['new_col'] = [int (tup[0]*tup[1]*0.01) for tup in pops_list]
