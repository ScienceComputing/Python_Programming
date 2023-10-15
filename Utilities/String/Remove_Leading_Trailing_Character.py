str1 = ' Cysteine helps prevent side effects due to drug reactions and toxic chemicals '
str1.strip()
# 'Cysteine helps prevent side effects due to drug reactions and toxic chemicals'

str1.rstrip() # Right remove
# ' Cysteine helps prevent side effects due to drug reactions and toxic chemicals'

str1.lstrip() # Left remove
# 'Cysteine helps prevent side effects due to drug reactions and toxic chemicals '


str2 = '&Cysteine helps prevent side effects due to drug reactions and toxic chemicals'
str2.strip('&')
# 'Cysteine helps prevent side effects due to drug reactions and toxic chemicals'
