# Topic: Regex metacharacters
# re.match -> anchor at the begining of a string; so if the first character of a string does not match the regex, then re.match will return nothing
# re.search

# Special characters: 
# . -> match any character except newline
# .+ -> match any number of any character except newline
# ^ -> start of a string
# $ -> end of a string
# \ -> escape the special characters
# | -> OR operand
# [] -> OR operand
# [^] -> take the opposite operation

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

str4 = 'I love the growth-mind culture of this company. I learn lots of from this company!.'
re.split(r'\.\s', str4) # \. escape the actual meaning of ., that is, match any character except newline
# ['I love the growth-mind culture of this company', 'I learn lots of from this company!.']

str5 = 'I love the growth-mind culture of this Company. I learn lots of from this company!.'
re.findall(r'Company|company', str5)
# ['Company', 'company']

re.findall(r'[Cc]ompany', str5)
# ['Company', 'company']

regex = r'[a-zA-Z]+\d' # Match the lower-case/upper-case letter any times followed by a digit
regex_non_word = r'[#$%&]'
regex_no_digit = r'[^0-9]'
