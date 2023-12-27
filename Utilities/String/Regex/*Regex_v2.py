# Topic: Regex metacharacters
# re.match -> anchor at the begining of a string; so if the first character of a string does not match the regex, then re.match will return nothing
# re.search -> searche for a pattern within the string; return a match object or None otherwise; the search is usually followed by an if-statement to test if the search succeeds

# Special characters: 
# . -> match any character except newline
# .+ -> match any number (once or more) of any character except newline
# .? -> match any number (zero or once) of any character
# .+? -> match any number (once or more) of any character except newline, using the **non-greedy** matching
# ? matches a single character, so 200?.txt will match 2002.txt or 2009.txt, but not 2002-01.txt.
# ^ -> start of a string
# $ -> end of a string
# \ -> escape the special characters; e.g., \(.+\); \.
# | -> OR operand
# [] -> OR operand
# [^] -> take the opposite operation
# () -> capturing groups; enclose a part of the pattern of interest to extract or reference later

"""Extract any sequence of digits and/or periods starting at the beginning of the string in a old column, and assign it to a new column"""
df['new_col'] = df['old_col'].str.extract('^([\d.]+)').astype(float)


import re
str1 = 'There are 8900023 students attending the NYU graduate school fair!'
re.search(r'\d+', str1)
# <re.Match object; span=(10, 17), match='8900023'>

match = re.search(r'\d+', str1)
if match:
  print('found', match.group()) 
else:
  print('did not find the number of students')
# found 8900023

match2 = re.search(r'(\d+)', str1)
if match2:
  print('found', match2.group(1)) 
else:
  print('did not find the number of students')
# found 8900023

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

"""
A complex case
"""
from collections import Counter
import re

def tokenize(text):
    """
    Tokenize the text using a regular expression. 
    This function serves as a wrapper for re.findall, performing case-insensitive matching.
    :param text: text to be tokenized
    :return: a list of resulting tokens
    >>> tokenize("Hello, word!")
    ['Hello', 'word']
    """
    return re.findall(r'[a-zA-z]+', text, flags=re.IGNORECASE)

class Document:
    def __init__(self, text):
        self.text = text
        self.tokens = self._tokenize()
        self.word_counts = self._count_words()
    def _tokenize(self):
        # Tokenize the document using a non-public method.
        return tokenize(self.text)
    def _count_words(self):
        # Tally the document's word counts using Counter (non-public method).
        return Counter(self.tokens)

quote = 'It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair.'
quote_doc = Document(text=quote)
print(quote_doc.tokens[:3]) 
# ['It', 'was', 'the']
print(quote_doc.word_counts.most_common(3))
# [('was', 10), ('the', 10), ('of', 10)]

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
