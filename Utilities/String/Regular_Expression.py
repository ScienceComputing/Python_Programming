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

# Usage: find all matches of a pattern:
# re.findall(r'regex', string)
re.findall(r'Lessions in Chemistry', 'Love Lessions in Chemistry! Really love Lessions in Chemistry!')
# ['Lessions in Chemistry', 'Lessions in Chemistry']

# Usage: split string at each match
# re.split(r'regex', string)
re.split(r'!', 'Love Lessions in Chemistry! Really love Lessions in Chemistry!')
# ['Love Lessions in Chemistry', ' Really love Lessions in Chemistry', '']

# Usage: replace one or many matches with a string
# re.sub(r'regex', new, string)
re.sub(r'Lessions', 'Lessons', 'Love Lessions in Chemistry! Really love Lessions in Chemistry!')
# 'Love Lessons in Chemistry! Really love Lessons in Chemistry!'

# Usage: supported metacharacters
re.findall(r'User\s\d', 'The winners are: User 80, User 12, User x')
# ['User 8', 'User 1']
re.findall(r'User\s\d{2}', 'The winners are: User 80, User 12, User x')
# ['User 80', 'User 12']


