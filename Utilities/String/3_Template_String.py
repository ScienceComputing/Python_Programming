# Simpler syntax; 
# Slower than f-strings; 
# Don't allow format specifiers (e for scientific notation; f for float; d for digit); 
# Good when working with externally formatted strings

from string import Template
str1 = Template('$amino_acid helps prevent side effects due to drug reactions and toxic chemicals.')
str1.substitute(amino_acid='Cysteine')
# 'Cysteine helps prevent side effects due to drug reactions and toxic chemicals.'

Cys = 'Cysteine'
str1.substitute(amino_acid=Cys)
# 'Cysteine helps prevent side effects due to drug reactions and toxic chemicals.'
