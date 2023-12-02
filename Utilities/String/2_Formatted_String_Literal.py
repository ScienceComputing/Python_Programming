# f-strings: f'literal string{expression}'
# More reading: https://realpython.com/python-f-strings/

# Example:
# Pair up the gene and protein names: pairs
pairs = zip(gene_names, protein_names)
# Iterate over pairs
for rank, pair in enumerate(pairs):
    # Unpack pair: gene_names, protein_names
    gene_names, protein_names = pair
    # Print the rank and names associated with each rank
    print(f'Rank {rank+1}: gene_name} and {protein_name}') # {rank+1}, {gene_name}, {protein_name} 

# Type conversions
# !s: convert to a string
# !r: convert to a printable string with quotes
# !a: convert to a printable string with quotes, but escape the non-ASCII character
name = 'Cystein'
print(f'{name!r} helps prevent side effects due to drug reactions and toxic chemicals.')
# 'Cystein' helps prevent side effects due to drug reactions and toxic chemicals.

# Use the format specifier
# e for scientific notation; f for float; d for digit
# {index:specifier}
number = 0.12890
print(f'Only {number:.2f}% of the protein data produced worldwide is analyzed!')
# Only 0.13% of the protein data produced worldwide is analyzed!
# :.2f -> use the float with 2 decimals
# f'{value:{width}.{precision}}'
# value -> any expression that evaluates to a number
# width -> the number of characters used in total to display, but if value needs more space than the width specifies, then the additional space is used.
# precision -> the number of characters used after the decimal point

fact = 2500000000000000000
print(f'About {fact:e} of data is produced daily in the world')
# About 2.500000e+18 of data is produced daily in the world

# Use the index
data = {'method': 'Supervised learning', 'goal': 'find patterns'}
print(f"{data['method']} tries to {data['goal']} in the dataset.")
# Supervised learning tries to find patterns in the dataset.
