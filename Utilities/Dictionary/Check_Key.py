# Check if the key in exists in a dictionary
amino_acid_galleries = {'Glutamine': 'Help the immune system function and normal brain function and digestion', 'Cysteine': 'Help prevent side effects due to drug reactions and toxic chemicals'}
'Tyrosine' in amino_acid_galleries
# False

if 'Cysteine' in amino_acid_galleries:
    print('Cysteine is in the database. Its function is: %s' % amino_acid_galleries['Cysteine'])
else:
    print('No this amino acid found in the databse.')
# Cysteine is in the database. Its function is: Help prevent side effects due to drug reactions and toxic chemicals
