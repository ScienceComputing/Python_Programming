# .group can only be used with .search and .match methods.

import re
str1 = 'The Dr. Zkulla album is released on 2023-09-10.'
info = re.search(r'(\d{4})-(\d{2})-(\d{2})', str1)
# info
# <re.Match object; span=(36, 46), match='2023-09-10'>
info.group(0)
# '2023-09-10'
info.group(1)
# '2023'
info.group(2)
# '09'
info.group(3)
# '10'

# Use named groups
