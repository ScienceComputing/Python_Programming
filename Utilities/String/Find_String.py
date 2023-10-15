str1 = 'Cysteine helps prevent side effects due to drug reactions and toxic chemicals'
str1.find('Cysteine') # The find method returns the lowest index in the string where it can find the substring
# 0

str1.find('Alanine')
# -1

str1.find('Cysteine', 1, 9)
# -1
