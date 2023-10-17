# Topic: Regex metacharacters
# re.match -> anchor at the begining of a string
# re.search

import re
str1 = 'There are 8900023 students attending the NYU graduate school fair!'
re.search(r'\d+', str1)
# <re.Match object; span=(10, 17), match='8900023'>

re.match(r'\d+', str1)
# Nothing returns
