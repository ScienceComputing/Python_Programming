# A regex to match a valid link/date/token/email/password address
link_regex = r'http\S+' # Very useful to use when you know a pattern doesn't contain spaces and you have reached the end when you do find one
date_regex = r'\d{1,2}\w+\s\w+\s\d{4}\s\d{1,2}:\d{2}' # 1st October 2023 17:25
token_regex = r'#\w+'
email_regex = r'[A-Za-z0-9!#%&*$.]+@\w+\.com'
password_regex = r'[a-zA-Z0-9*#$%!&.]{8,20}'
