str1 = ' Cysteine helps prevent side effects due to drug reactions and toxic chemicals '
str1.strip()
# 'Cysteine helps prevent side effects due to drug reactions and toxic chemicals'

str1.rstrip()
# ' Cysteine helps prevent side effects due to drug reactions and toxic chemicals'

str1.lstrip()
# 'Cysteine helps prevent side effects due to drug reactions and toxic chemicals '


str2 = '&Cysteine helps prevent side effects due to drug reactions and toxic chemicals'
str2.strip('&')
# 'Cysteine helps prevent side effects due to drug reactions and toxic chemicals'
