# Quantifier - immediately to the left
# The following quantifiers are greedy; they tend to match as many characters as possible and return the longest match
# {3} {3, 4} {3,} -> 3 times; 3 times at least, 4 times at most; 3 times at least
# +: once or more -> r'violin+': + applies to n, not to violin 
# *: zero times or more
# ?: zero times or once -> useful for detecting the word variation

import re
str1 = '1681 Broadway WMM OP 9-0'
re.findall(r'\d+-\d+', str1)
# ['9-0']

str2 = 'The visual abstract was amazing! @Limma&!n @John!!n @Jake09'
re.findall(r'@\w+\W*\w+', str2)
# ['@Limma&!n', '@John!!n', '@Jake09']

str3 = 'The color of this image is wonderful! But, the colour could be more colorful.'
re.findall(r'colou?r', str3)
# ['color', 'colour', 'color']
# or re.findall(r'colo[u]{0,1}r', str3)
# ['color', 'colour', 'color']
re.match(r'[0-9]+?', str1) # Match any digt 0 times or once
# <re.Match object; span=(0, 1), match='1'>

# Non-greedy matching
# The quantifiers tend to match as few characters as needed and they return the shortest match
# Append ? to the greedy quantifiers
re.match(r'\d+?', str1)
# <re.Match object; span=(0, 1), match='1'>
re.match(r'\d+', str1)
# <re.Match object; span=(0, 4), match='1681'>

# Summary:
# When longer matches are necessary, the greedy quantifiers are the best option.
# When we hope to match as few as possible, the lazy quantifiers sound perfect.
