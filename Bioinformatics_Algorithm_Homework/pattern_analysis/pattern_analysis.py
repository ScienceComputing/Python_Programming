def pattern_count(Text, Pattern):
    """Count the k-mier patterns from a genome sequence in text.

    Parameters
    ----------
    Text : str
        A genome sequence, e.g., ATTTTTCGTTTAAA.
        
    Pattern : str
        A k-mier pattern of interest, e.g., TTTA

    Returns
    -------
    int

    """
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count 
