# Enumeration is used in loops to return the position and the data in that position while looping

# enumerate() is a function that takes any iterable as argument, and returns an enumerate object, which consists of pairs containing the elements of the original iterable, along with their index within the iterable. 
print(list(enumerate(range(100, 1001, 100))))
# [(0, 100), (1, 200), (2, 300), (3, 400), (4, 500), (5, 600), (6, 700), (7, 800), (8, 900), (9, 1000)]`

programming_language_list = ['Python', 'JavaScript', 'Julia', 'R', 'C']
for index, value in enumerate(programming_language_list):
    print(index, value)
# 0 Python
# 1 JavaScript
# 2 Julia
# 3 R
# 4 C

for index, value in enumerate(programming_language_list, start=1): # Change the starting index
    print(index, value)
# 1 Python
# 2 JavaScript
# 3 Julia
# 4 R
# 5 C

programming_language_enumerate = enumerate(programming_language_list)
print(list(programming_language_enumerate))
# [(0, 'Python'), (1, 'JavaScript'), (2, 'Julia'), (3, 'R'), (4, 'C')]

# Map categorical labels to numerical indices
atac_train = pd.read_parquet('../single_cell_data/atac_train.parquet', engine='pyarrow')
row_labels = df['id'].values
row_label_to_index = {label: index for index, label in enumerate(row_labels)}
type(row_label_to_index)
# <class 'dict'>
