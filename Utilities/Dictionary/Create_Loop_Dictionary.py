# Method 1: {}
amino_acid_galleries = {}
gallery_info = [('Glutamine', 'Help the immune system function and normal brain function and digestion'), ('Cysteine', 'Help prevent side effects due to drug reactions and toxic chemicals')]

# Turn tuples into a dictionary
for name, function in gallery_info: # gallery_info is a list of tuples
    amino_acid_galleries[name] = function
print(amino_acid_galleries)
# {'Glutamine': 'Help the immune system function and normal brain function and digestion', 'Cysteine': 'Help prevent side effects due to drug reactions and toxic chemicals'}

# Loop over a dictionary
for name, function in amino_acid_galleries.items():
    print(name)
    print(function)

# Glutamine
# Help the immune system function and normal brain function and digestion
# Cysteine
# Help prevent side effects due to drug reactions and toxic chemicals

# Find the last 5 amino acid names
for name in sorted(amino_acid_galleries)[-5:]: # Loop over the key
    print(name)

# Method 2: dict()
