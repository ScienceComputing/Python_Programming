# Unpacking tuples
data = ( 'XYZ', 90, 71.1, (2023, 12, 21) )
_, shares, price, (year, *_) = data
shares
price
year

list1 = ['cake1', 'cake2', 'cake3']
list2 = ['Vanilla Cake', 'Red Velvet Cake', 'Black Forest Cake']
full_list = list(zip(list1, list2))

for cake_index, cake_type in full_list:
    print(cake_index)
    print(cake_type)
  
# cake1
# Vanilla Cake
# cake2
# Red Velvet Cake
# cake3
# Black Forest Cake
