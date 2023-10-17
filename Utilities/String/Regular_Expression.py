# Why use pattern matching?
# 1. Find and replace text
# 2. Validate strings

# Example to construct a pattern:
# r'st\d\s\w{3,10}'
# r: raw string
# st: these are normal characters; they exactly match s and t
# ---The followings are the metacharacters
# \d: a digit
# \s: a whitespace
# \w: a word character
# {3, 10}: \w should appear between 3 and 10 times

import re

# Find all matches of a pattern:
# re.findall(r'regex', string)
re.findall(r'Lessions in Chemistry', 'Love Lessions in Chemistry! Really love Lessions in Chemistry!')
# ['Lessions in Chemistry', 'Lessions in Chemistry']

# Split string at each match
re.split(r'!', 'Love Lessions in Chemistry! Really love Lessions in Chemistry!')
# ['Love Lessions in Chemistry', ' Really love Lessions in Chemistry', '']
