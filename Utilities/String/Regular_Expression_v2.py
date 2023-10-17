# Quantifier
# {3} {3, 4} -> Regular_Expresson_v1.py
# +: once or more
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
