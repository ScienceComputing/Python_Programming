# A regex to match a valid link/date/token/email/password address
link_regex = r'http\S+' # Very useful to use when you know a pattern doesn't contain spaces and you have reached the end when you do find one
date_regex = r'\d{1,2}\w+\s\w+\s\d{4}\s\d{1,2}:\d{2}' # 1st October 2023 17:25
token_regex = r'#\w+'
email_regex = r'[A-Za-z0-9!#%&*$.]+@\w+\.com'
email_user_account = r'([A-Za-z0-9]+)@\S+' # e.g., oppert009@hotmail.com -> oppert009
password_regex = r'[a-zA-Z0-9*#$%!&.]{8,20}'
html_tag_regex = r'<.+?>'

flight_regex = r'([A-Z]{2})(\d{4})\s([A-Z]{3})-([A-Z]{3})\s(\d{2}[A-Z]{3})'
flight_info = 'Here you have your boarding pass CB5678 AMS-MAD 01NOV.'
re.findall(flight_regex, flight_info)
# [('CB', '5678', 'AMS', 'MAD', '01NOV')]

flight_matches = re.findall(flight_regex, flight_info)
print("Airline: {} Flight number: {}".format(flight_matches[0][0], flight_matches[0][1]))
print("Departure: {} Destination: {}".format(flight_matches[0][2], flight_matches[0][3]))
print("Date: {}".format(flight_matches[0][4]))

# Airline: CB Flight number: 5678
# Departure: AMS Destination: MAD
# Date: 01NOV

# Obtain all phone numbers not preceded by area code
cellphones = ['4263-699221-05', '390-1723-500215', '8126-079012-09']
for phone in cellphones:
    number = re.findall(r"(?<!\d{3}-)\d{4}-\d{6}-\d{2}", phone)
    print(number)

# ['4263-699221-05']
# []
# ['8126-079012-09']

# Obtain all phone numbers not followed by optional extension
cellphones2 = ['126-4263-699221-05', '390-1723-500215', '109-8126-079012']
for phone in cellphones2:
    number = re.findall(r"\d{3}-\d{4}-\d{6}(?!-\d{2})", phone)
    print(number)

# []
# ['390-1723-500215']
# ['109-8126-079012']
