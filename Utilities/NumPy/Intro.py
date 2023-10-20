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

# 2: create a 2-d NumPy array from a list
list_1 = ['T cell', 'B cell', 'NK cell']
list_2 = ['patient1', 'patient2', 'patient3']
array_2 = np.array((list_1, list_2)) # Use tuple than list, giving more efficiency
print(array_2)
# [['T cell' 'B cell' 'NK cell']
#  ['patient1' 'patient2' 'patient3']]
