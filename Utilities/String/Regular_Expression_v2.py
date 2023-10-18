# Quantifier - immediately to the left
# {3} {3, 4} {3,} -> 3 times; 3 times at least, 4 times at most; 3 times at least
# +: once or more -> r'violin+': + applies to n, not to violin 
# *: zero times or more
# ?: zero times or once -> useful for detecting the word variation

import re
str1 = '56-9000998 WMM OP 9-0'
re.findall(r'\d+-\d+', str1)
# ['56-9000998', '9-0']

str2 = 'The visual abstract was amazing! @Limma&!n @John!!n @Jake09'
re.findall(r'@\w+\W*\w+', str2)
# ['@Limma&!n', '@John!!n', '@Jake09']

str3 = 'The color of this image is wonderful! But, the colour could be more colorful.'
re.findall(r'colou?r', str3)
# ['color', 'colour', 'color']

# A regex to match a valid link/date/token/email/password address
link_regex = r'http\S+' # Very useful to use when you know a pattern doesn't contain spaces and you have reached the end when you do find one
date_regex = r'\d{1,2}\w+\s\w+\s\d{4}\s\d{1,2}:\d{2}' # 1st October 2023 17:25
token_regex = r'#\w+'
email_regex = r'[A-Za-z0-9!#%&*$.]+@\w+\.com'
password_regex = r'[a-zA-Z0-9*#$%!&.]{8,20}'