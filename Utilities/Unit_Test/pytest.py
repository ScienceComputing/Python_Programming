# Terminal:
# touch test_trigonometric_func.py
# vim test_trigonometric_func.py

import math
import pytest

def trigonometric_functions(angle_degrees):
    """Calculate trigonometric functions for a given angle in degrees

    :param angle_degrees: Angle in degrees
    :return: Tuple of (sin, cos, tan) values for the angle
    """
    angle_radians = math.radians(angle_degrees)
    sin_value = math.sin(angle_radians)
    cos_value = math.cos(angle_radians)
    tan_value = math.tan(angle_radians)
    return sin_value, cos_value, tan_value

# Pytest unit test for trigonometric_functions
@pytest.mark.parametrize("angle_degrees, expected", [(30, (0.49999999999999994, 0.8660254037844387, 0.5773502691896257)),
                                                    (45, (0.7071067811865475, 0.7071067811865476, 0.9999999999999999)),
                                                    (60, (0.8660254037844387, 0.49999999999999994, 1.7320508075688772))])
def test_trigonometric_functions(angle_degrees, expected):
    result = trigonometric_functions(angle_degrees)
    assert pytest.approx(result, rel=1e-9) == expected

# Terminal:
# pytest test_trigonometric_func.py

# ============================= test session starts ==============================
# platform darwin -- Python 3.11.6, pytest-7.4.3, pluggy-1.3.0
# rootdir: /Users/your_name
# plugins: anyio-4.1.0
# collected 3 items

# test_trigonometric_func.py ...                                           [100%]

# ============================== 3 passed in 0.01s ===============================

# Add error message to improve the readability of the default output of pytest results
def test_trigonometric_functions_2(angle_degrees, expected):
    result = trigonometric_functions(angle_degrees)
    expect = (0.49999999999999994, 0.8660254037844387, 0.5773502691896256)
    error_message = "trigonometric_functions(30) should return the floats {0}, but it actually returned {1}".format(expect, result)
    assert pytest.approx(result, rel=1e-9) == expect, error_message
    
