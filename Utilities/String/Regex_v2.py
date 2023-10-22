# Topic: Regex metacharacters
# re.match -> anchor at the begining of a string; so if the first character of a string does not match the regex, then re.match will return nothing
# re.search -> searche for a pattern within the string; return a match object or None otherwise; the search is usually followed by an if-statement to test if the search succeeds

# Special characters: 
# . -> match any character except newline
# .+ -> match any number (once or more) of any character except newline
# .? -> match any number (zero or once) of any character
# .+? -> match any number (once or more) of any character except newline, using the **non-greedy** matching
# ^ -> start of a string
# $ -> end of a string
# \ -> escape the special characters; e.g., \(.+\); \.
# | -> OR operand
# [] -> OR operand
# [^] -> take the opposite operation

import re
str1 = 'There are 8900023 students attending the NYU graduate school fair!'
re.search(r'\d+', str1)
# <re.Match object; span=(10, 17), match='8900023'>

match = re.search(r'\d+', str1)
if match:
  print('found', match.group()) 
else:
  print('did not find the number of students')

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

str6 = "I want to have a car. But I don't know if I want a Tesla, an Audi, a BMW, a Mercedes-Benz, or a Toyota."
re.findall(r'Tesla|Audi|BMW|Mercedes-Benz|Toyota', str6)
# ['Tesla', 'Audi', 'BMW', 'Mercedes-Benz', 'Toyota']

str7 = "I want to order a bunch of cars for my company. But I don't know if I want 2 Tesla, 3 Audi, 1 BMW, 2 Mercedes-Benz, or 5 Toyota."
re.findall(r'\d+\sTesla|Audi|BMW|Mercedes-Benz|Toyota', str7)
# ['2 Tesla', 'Audi', 'BMW', 'Mercedes-Benz', 'Toyota']

re.findall(r'\d+\s(Tesla|Audi|BMW|Mercedes-Benz|Toyota)', str7)
# ['Tesla', 'Audi', 'BMW', 'Mercedes-Benz', 'Toyota']

re.findall(r'(\d+)\s(Tesla|Audi|BMW|Mercedes-Benz|Toyota)', str7)
# [('2', 'Tesla'), ('3', 'Audi'), ('1', 'BMW'), ('2', 'Mercedes-Benz'), ('5', 'Toyota')]

# Match but not capture a group (?:Regex)
str8 = 'Andy Wang: 56-56-9820'
re.findall(r'(?:\d{2}-){2}(\d{4})', str8)
# ['9820']

str9 = 'Today is 2nd March 2023. Tomorrow is 3rd March 2023.'
re.findall(r'(\d+)(?:nd|rd)', str9)
# ['2', '3']

str10 = 'I totally love the concert Peace of Love World Tour. It kinda wonderful!'
re.findall(r'(love|like|enjoy).+?(movie|concert)\s(.+?)\.', str10)
# [('love', 'concert', 'Peace of Love World Tour')]

re.findall(r'(love|like|enjoy).+?(?:movie|concert)\s(.+?)\.', str10)
# [('love', 'Peace of Love World Tour')]
