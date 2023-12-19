import sys
import pytest
import numpy as np

class TestGetDataAsNumpyArray(object):
    @pytest.mark.skipif(
        sys.version_info > (2, 7) or sys.platform != "linux",
        reason="Skipped on Python 2.7 or higher and non-Linux platforms"
    )
    def test_on_clean_file(self):
        expected = np.array([[2366.9, 3567.0],
                             [35.0, 789.7],
                             [129.0, 2.0],
                             [666.2, 123.5]
                             ]
                            )
        result = get_data_as_numpy_array("raw_data.txt", num_columns=2)
        message = "Expected return value: {0}, Actual return value: {1}".format(expected, result)
        assert result == pytest.approx(expected), message

# Terminal:
# pytest -rs
