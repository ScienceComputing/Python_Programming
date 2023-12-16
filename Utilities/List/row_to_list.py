def row_to_list(row):
    """
    Convert a tab-separated row to a list of entries.

    :param row: A string containing tab-separated values
    :return: A list of entries if valid, otherwise None
    """
    row = row.rstrip()
    separated_entries = row.split("\t")
    
    if len(separated_entries) == 2 and "" not in separated_entries:
        return separated_entries
    
    return None

row_to_list("27\t6667\n")
# ['27', '6667']
row_to_list("\t12678\n") # Nothing returned
row_to_list("27890\n") # Nothing returned
