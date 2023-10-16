# f-strings: f'literal string{expression}'

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
name = "Cystein"
print(f'{name!r} helps prevent side effects due to drug reactions and toxic chemicals.')
# 'Cystein' helps prevent side effects due to drug reactions and toxic chemicals.

