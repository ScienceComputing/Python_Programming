# Use () to group and capture characters together
# ([A-Za-z]+)\s\w+\s(\d+)\s(\w+)

import re
str1 = 'Joty has 3 friends who she spends some time with every week. Zoey has 0 brothers.'
re.findall(r'([A-Za-z]+)\s\w+\s(\d+)\s(\w+)', str1)
# [('Joty', '3', 'friends'), ('Zoey', '0', 'brothers')]
a = re.findall(r'([A-Za-z]+)\s\w+\s(\d+)\s(\w+)', str1)
a[0][1]
# '3'

# Apply the quantifier to the entire group
str2 = '8F0j3r'
re.search(r'(\d[A-Za-z])+', str2)
# <re.Match object; span=(0, 6), match='8F0j3r'>

re.search(r'\d[A-Za-z]+', str2)
# <re.Match object; span=(0, 2), match='8F'>
