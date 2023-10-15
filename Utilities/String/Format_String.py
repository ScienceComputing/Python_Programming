# Format the title in a graph; show the message or error; pass the statement into a function

# Pair up the girl and boy names: pairs
pairs = zip(gene_names, protein_names)

# Iterate over pairs
for rank, pair in enumerate(pairs):
    # Unpack pair: girl_name, boy_name
    gene_names, protein_names = pair
    # Print the rank and names associated with each rank
    print(f'Rank {rank+1}: gene_name} and {protein_name}')
