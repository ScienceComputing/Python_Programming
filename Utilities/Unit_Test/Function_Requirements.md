## Highlight
- Normal arguments
- Special arguments
  - Boundary values
  - Arguments triggering special logic
- Bad arguments
- Return values
- Exceptions

```
# To design a well-tested function, let us think about normal and special arguments before implementing the function
# Normal arguments
def test_no_comma():
    result = str_to_int("9902")
    assert result == 9902, "Expected output: 9902, Return value: {0}".format(result)
    
def test_one_comma():
    result = str_to_int("16,212")
    assert result == 16212, "Expected output: 16212, Return value: {0}".format(result)
    
def test_two_commas():
    result = str_to_int("29,155,336")
    assert result == 29155336, "Expected output: 29155336, Return value: {0}".format(result)

# Special arguments
def test_miss_comma():
    result = str_to_int("519666,129")
    assert result is None, "Expected: None, result: {0}".format(result)
    
def test_incorrectly_placed_comma():
    result = str_to_int("89,11,546")
    assert result is None, "Expected: None, result: {0}".format(result)
    
def test_float_value():
    result = str_to_int("1,233.50")
    assert result is None, "Expected: None, result: {0}".format(result)

def str_to_int(number_with_commas):
    """
    Convert a number with commas as a string to an integer.

    :param number_with_commas: A string representation of a number with commas.
    :return: An integer representation of the input number.
    """
    return int(number_with_commas.replace(",", ""))

```
