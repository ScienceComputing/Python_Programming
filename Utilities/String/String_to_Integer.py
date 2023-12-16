def convert_to_int(number_with_commas):
    """
    Convert a number with commas as a string to an integer.

    :param number_with_commas: A string representation of a number with commas.
    :return: An integer representation of the input number.
    """
    return int(number_with_commas.replace(",", ""))

convert_to_int("102,901") # 102901
