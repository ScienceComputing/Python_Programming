# Import NumPy (numerical python)
# TensorFlow/SciPy/pandas/matplotlib/scikit-learn are built upon NumPy
import numpy as np

# NumPy main oject is array
# NumPy arrays store the data in any number of dimensions (1, 2, 3)

# We can create the NumPy arrays from lists/csv files/NumPy functions (e.g., np.arange())/pandas dataframe
# 1: create a 1-d NumPy array from a list
list_1 = ['T cell', 'B cell', 'NK cell']
array_1 = np.array(list_1)
print(array_1)
# array(['T cell', 'B cell', 'NK cell'], dtype='<U7')

# 2: create a 2-d NumPy array from a tuple of lists
list_1 = ['T cell', 'B cell', 'NK cell']
list_2 = ['patient1', 'patient2', 'patient3']
array_2 = np.array((list_1, list_2)) # Use tuple than list (though you can use list here), giving more efficiency
print(array_2)
# [['T cell' 'B cell' 'NK cell']
#  ['patient1' 'patient2' 'patient3']]

# 3: create a 1-d NumPy array from a range -> useful for creating the synthetic data which is for testing the NumPy code
array_3 = np.array(range(0, 30))
print(array_3)
# [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
# 24 25 26 27 28 29]

# 4: create a 2-d NumPy array from a tuple of ranges
array_4 = np.array((range(0, 30), range(10, 40)))
print(array_4)
# [[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
#  24 25 26 27 28 29]
# [10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33
#  34 35 36 37 38 39]]

# 5: reshape a 1-d NumPy array to a 2-d one
array_3.reshape((5, 6)) # (num_row, num_col)
# array([[ 0,  1,  2,  3,  4,  5],
#        [ 6,  7,  8,  9, 10, 11],
#        [12, 13, 14, 15, 16, 17],
#        [18, 19, 20, 21, 22, 23],
#        [24, 25, 26, 27, 28, 29]])

# 6: reshape a 1-d NumPy array to a 3-d one, which is a list of 2-d arrays
array_3.reshape((3, 2, 5)) # (num_2-d_array, num_row, num_col)
# array([[[ 0,  1,  2,  3,  4],
#         [ 5,  6,  7,  8,  9]],

#        [[10, 11, 12, 13, 14],
#         [15, 16, 17, 18, 19]],

#        [[20, 21, 22, 23, 24],
#         [25, 26, 27, 28, 29]]])


# 7: reshape a 1-d NumPy array to a 4-d one, which is a list of 3-d arrays, or a list of a list of 2-d arrays
array_3.reshape((1, 3, 2, 5)) # (num_3-d_array, num_2-d_array, num_row, num_col)
# array([[[[ 0,  1,  2,  3,  4],
#          [ 5,  6,  7,  8,  9]],

#         [[10, 11, 12, 13, 14],
#          [15, 16, 17, 18, 19]],

#         [[20, 21, 22, 23, 24],
#          [25, 26, 27, 28, 29]]]])
