# Access the elements in a nested dictionary
# Method 1:
amino_acid_galleries = {
    'Cysteine': {
         'Formula': 'HOOC−CH(−NH2)−CH2−SH', 
         'Function': 'Help prevent side effects due to drug reactions and toxic chemicals'
    },
    'Serine': {
        'Formula': 'HO2C−CH(NH2)−CH2OH',
        'Function': 'Involved in the synthesis of purines and pyrimidines'
    },
    'Lysine': {
        'Formula': 'H2N−(CH2)4−CH(NH2)−COOH',
        'Function': 'Used in the biosynthesis of proteins'
    }
}
amino_acid_galleries['Cysteine']['Formula']
# 'HOOC−CH(−NH2)−CH2−SH'

# Method 2:
print(amino_acid_galleries['Cysteine'].keys())
# dict_keys(['Formula', 'Function'])
amino_acid_galleries['Cysteine'].get('Formula')
# 'HOOC−CH(−NH2)−CH2−SH'

for name in amino_acid_galleries:
     print(name, amino_acid_galleries[name].get('Formula', 'N/A'))
# Cysteine HOOC−CH(−NH2)−CH2−SH

# Show all the amino acids that have the formulas
print([name for name in amino_acid_galleries if 'Formula' in amino_acid_galleries[name]])
# ['Cysteine']
