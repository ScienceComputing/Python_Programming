# f-strings: f'literal string{expression}'


# Pair up the gene and protein names: pairs
pairs = zip(gene_names, protein_names)
# Iterate over pairs
for rank, pair in enumerate(pairs):
    # Unpack pair: gene_names, protein_names
    gene_names, protein_names = pair
    # Print the rank and names associated with each rank
    print(f'Rank {rank+1}: gene_name} and {protein_name}') # {rank+1}, {gene_name}, {protein_name} 

