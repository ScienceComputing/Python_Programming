# Topic: Regex metacharacters
# re.match -> anchor at the begining of a string
# re.search

# Special characters: 
# . -> match any character except newline
# .+ -> match any number of any character
# ^ -> start of the string

import re
str1 = 'There are 8900023 students attending the NYU graduate school fair!'
re.search(r'\d+', str1)
# <re.Match object; span=(10, 17), match='8900023'>

re.match(r'\d+', str1)
# Nothing returns

str2 = 'https://www.harvard.edu'
re.findall(r'www.+edu', str2)
# ['www.harvard.edu']

str3 = 'There are 8900 male and 900 female students attending the NYU graduate school fair!'
re.findall(r'^There\sare\s\d+', str3)
# ['There are 8900']
