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

str2 = Template('Cysteine helps prevent side effects due to ${function}s and toxic chemicals.')
str2.substitute(function='drug reaction')
# 'Cysteine helps prevent side effects due to drug reactions and toxic chemicals.'

# $$ -> escape the dollar sign
str3 = Template('I paid for the Roma tomatoes only $$$price, amazing!') # $price -> identifier
str3.substitute(price='1.5')
# 'I paid for the Roma tomatoes only $1.5, amazing!'

favor_donut = dict(flavor='Glazed donut')
str4 = Template('I enjoy $flavor $donut very much!')
try:
    str4.substitute(favor_donut)
except KeyError:
    print('Missing information')

# Missing information

# Set up safe substitution whereby missing placeholders will appear in resulting string
favor_donut = dict(flavor='Glazed donut')
str4 = Template('I enjoy $flavor $donut very much!')
str4.safe_substitute(favor_donut)
# 'I enjoy Glazed donut $donut very much!'
