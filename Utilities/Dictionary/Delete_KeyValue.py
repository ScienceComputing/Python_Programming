# Method 1: del will throw a KeyError if the key to delete does not exist
del amino_acid['Cys'] # Cys is a key

# Method 2:
amino_acid_cys = amino_acid.pop('Cys') # Save the removed key-value pair
print(amino_acid_cys) 
