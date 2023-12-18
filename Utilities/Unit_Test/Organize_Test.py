# Terminal:
# touch test_str_to_int.py
# vim test_str_to_int.py
# Inside test_str_to_int.py

import pytest

def str_to_int(number_with_commas):
    """
    Convert a number with commas as a string to an integer.

    :param number_with_commas: A string representation of a number with commas.
    :return: An integer representation of the input number.
    """
    try:
        return int(number_with_commas.replace(",", ""))
    except ValueError:
        return None

class TestStrToInt(object):
    def test_no_comma(self):
      result = str_to_int("9902")
      assert result == 9902, "Expected output: 9902, Return value: {0}".format(result)
    def test_one_comma(self):
        result = str_to_int("16,212")
        assert result == 16212, "Expected output: 16212, Return value: {0}".format(result)    
    def test_two_commas(self):
        result = str_to_int("29,155,336")
        assert result == 29155336, "Expected output: 29155336, Return value: {0}".format(result)
    def test_miss_comma(self):
        result = str_to_int("519666,129")
        assert result is None, "Expected: None, result: {0}".format(result)
    def test_incorrectly_placed_comma(self):
        result = str_to_int("89,11,546")
        assert result is None, "Expected: None, result: {0}".format(result)
    def test_float_value(self):
        result = str_to_int("1,233.50")
        assert result is None, "Expected: None, result: {0}".format(result)

# Terminal:
# pytest
# pytest -k "no_comma"
