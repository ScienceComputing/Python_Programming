# Look-ahead
# Check if the first part of the expression is followed [positive] or not [negative] by the look-ahead expression; return the first part of the expression
# Positive look-ahead expression: (?=); negative look-ahead expression: (?!)

import re

# Find the expression followed by 'removed'
str1 = 'summer.txt removed; spring.txt; renamed autumn.txt removed'
re.findall(r'\w+\.txt(?=\sremoved)', str1)
# ['summer.txt', 'autumn.txt']

# Find the expression not followed by 'removed'
re.findall(r'\w+\.txt(?!\sremoved)', str1)
# ['spring.txt']

# Look-behind
# Obtain all the matches that are preceded [positive] or not [negative] by a specific pattern; return the matches after look-behind expression
# Positive look-behind expression: (?<=); negative look-behind expression: (?<!)

# Find the expression preceded by 'Member: '
str2 = 'Member: Michel Zong, Member: Jason Jhonson, Past: Olivera Gamma'
re.findall(r'(?<=Member:\s)\w+\s\w+', str2)
# ['Michel Zong', 'Jason Jhonson']

re.findall(r'(?<!Past:\s)\w+\s\w+', str2) # TD

# Find the expression not preceded by 'pink'
str3 = 'My pink pen lie at the table. However, my green bag is on the chair.'
re.findall(r'(?<!pink\s)(pen|bag)', str3) # (pen|bag) is an alternation group
# ['bag']
