# Look-ahead
# Check if the first part of the expression is followed or not by the look-ahead expression; return the first part of the expression
# Positive look-ahead expression: (?=); negative look-ahead expression: (?!run)

import re
str1 = 'summer.txt removed; spring.txt; renamed autumn.text removed'
re.findall(r'\w+\.txt', str1)
