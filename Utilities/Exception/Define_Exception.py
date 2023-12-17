"""
Case 1
"""
class DivisionError(ValueError):
    pass

class IntegerDivisionError(DivisionError):
    pass

class Divider:
    def divide(self, a, b):
        if b == 0:
            raise DivisionError("Division by zero!")
        if a % b != 0: # Check if the remainder of the division of a by b is not equal to zero. 
            raise IntegerDivisionError("Result is not an integer!")
        return a // b # Floor division: return the largest integer that is less than or equal to the result.

divider = Divider()
result = divider.divide(10, 2)  
result = divider.divide(10, 3)  
# IntegerDivisionError: Result is not an integer!
result = divider.divide(10, 0)  
# DivisionError: Division by zero!


# We should place the except block for child exceptions before the parent exceptions. 
# If not, the parent except block will capture all child exceptions, preventing the child except block from ever running.
try:  
    divider.divide(10, 3)
except DivisionError:  
    print("DivisionError caught")
except IntegerDivisionError:  
    print("IntegerDivisionError caught")

# DivisionError caught

try:  
    divider.divide(10, 3)
except IntegerDivisionError:  
    print("IntegerDivisionError caught")
except DivisionError:  
    print("DivisionError caught")

# IntegerDivisionError caught

"""
Case 2
"""
import numpy as np

def split_scRNAseq_data(data_matrix):
    """
    Split single-cell RNA-seq data into training and testing sets.

    Args:
        data_matrix (numpy.ndarray): The input data matrix with cells as rows and genes as columns.

    Returns:
        tuple: A tuple containing two numpy arrays, (training_data, testing_data).
    """
    num_cells, num_genes = data_matrix.shape
    if num_cells < 2000:
        raise ValueError("Input data_matrix must have at least 2000 cells, it actually has just {0}".format(num_cells))
    num_training = int(0.7 * num_cells)
    permuted_indices = np.random.permutation(num_cells)
    return data_matrix[permuted_indices[:num_training], :], data_matrix[permuted_indices[num_training:], :]

import pytest

def test_split_scRNAseq_data():
    # Test case with 2 cells
    test_data = np.array([[13, 39, 90, 100, 29], [15, 6, 7, 12, 0]])
    with pytest.raises(ValueError) as exc_info:
        split_scRNAseq_data(test_data)
    expected_error_msg = "Input data_matrix must have at least 2000 cells, it actually has just 2"
    assert exc_info.match(expected_error_msg)

# Run the test function
test_split_scRNAseq_data() # Nothing is returned, suggesting this test on the exception passes.



