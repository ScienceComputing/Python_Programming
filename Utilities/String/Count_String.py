str1 = 'Cysteine Cysteine helps prevent side effects due to drug reactions and toxic chemicals'
str1.count('Cysteine')
# 2

str1.count('Cysteine', 2, len(str1))
# 1

str1.replace('Cysteine ', '', 1)
# 'Cysteine helps prevent side effects due to drug reactions and toxic chemicals'
