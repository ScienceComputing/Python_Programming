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

str3 = '8900 males and 900 females'
re.findall(r'^\d+\smales', str3)
# ['8900 males']
re.findall(r'\d+\sfemales$', str3)
# ['900 females']
