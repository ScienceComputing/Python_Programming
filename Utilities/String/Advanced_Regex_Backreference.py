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

# Use named groups to backreference
# Assign a name to a group: (?P<name>(regex))
str2 = 'New York, 10021'
city_info = re.search(r'(?P<city>[A-Za-z]+\s*[A-Za-z]*).*?(?P<zipcode>\d{5})', str2)
# city_info = re.search(r'(?P<city>\w+\s*\w*).*?(?P<zipcode>\d{5})', str2)
city_info.group('city')
# 'New York'
city_info.group('zipcode')
# '10021'

# Use \number to backreference a group
# (\d{1,2})\1
str3 = "You're very great great great!"
re.findall(r'(\w+)\s\1', str3) # Find the first occurence of the repeated words
# ['great']
re.sub(r'(\w+)\s\1', r'\1', str3)
# "You're very great great!"

regex = r"\w*(\w)\1\w*"
# \w*: This part matches zero or more word characters (letters, digits, or underscores).
# (\w): This is a capturing group that matches a single word character and captures it for later use.
# \1: This is a backreference to the first capturing group, **ensuring that the same character that was captured earlier is repeated**.
# \w*: This part matches zero or more word characters after the repeated character.
# In summary, this regular expression will match any sequence of word characters where the same character is repeated at least once. For example, it would match words like "hello," "bookkeeper," or "mississippi" because they contain repeated characters.

html_tag = '<body>To be a bioinformatician, you need to have knowledge in statistics and mathematics</body>'
re.findall(r'(<(\S+?)>)(?:.*)(</\S+?>)', html_tag) # TD

# Use the named group to reference back
# ?P<name>
str4 = 'Your one-time password is 904809. Please enter 904809 to login in the online system.'
re.findall(r'(?P<code>\d{6}).*?(?P=code)', str4)
# ['904809']

str5 = 'This function is not working! It often repeats error messages messages!'
re.sub(r'(?P<word>\w+)\s(?P=word)', r'\g<word>', str5) 
# 'This function is not working! It often repeats error messages!'
