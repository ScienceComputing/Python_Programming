# Method 1: {}
amino_acid_galleries = {}

for name, function in gallery_info: # gallery_info is a given tuple
    amino_acid_galleries[name] = function

# Find the last 5 amino acid names
for name in sorted(amino_acid_galleries)[-5:]: # Loop over the key
    print(name)

# Method 2: dict()
