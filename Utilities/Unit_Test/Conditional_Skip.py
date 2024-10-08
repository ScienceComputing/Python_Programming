import sys
import pytest
import numpy as np

class TestReturnDataAsNumpyArray(object):
    @pytest.mark.skipif(
        sys.version_info > (2, 7) or sys.platform != "linux",
        reason="Skipped on Python 2.7 or higher and non-Linux platforms"
    )
    def test_on_clean_data(self):
        expected = np.array([[2366.9, 3567.0],
                             [35.0, 789.7],
                             [129.0, 2.0],
                             [666.2, 123.5]
                             ]
                            )
        result = return_data_as_numpy_array("raw_data.txt", num_columns=2)
        error_message = "Expected return value: {0}, Actual return value: {1}".format(expected, result)
        assert result == pytest.approx(expected), error_message

# Terminal:
# pytest -rs
