str1 = 'Cysteine helps prevent side effects due to drug reactions and toxic chemicals'
str1.split(sep=' ')
# ['Cysteine', 'helps', 'prevent', 'side', 'effects', 'due', 'to', 'drug', 'reactions', 'and', 'toxic', 'chemicals']

str1.split(sep=' ', maxsplit=2) # Left split
# ['Cysteine', 'helps', 'prevent side effects due to drug reactions and toxic chemicals']

str1.rsplit(sep=' ', maxsplit=2) # Right split
# ['Cysteine helps prevent side effects due to drug reactions and', 'toxic', 'chemicals']

str2 = 'Cysteine \nhelps prevent side effects due to drug reactions and toxic chemicals'
print(str2)
# Cysteine
# helps prevent side effects due to drug reactions and toxic chemicals

str2.splitlines() # Split at lines
# ['Cysteine ', 'helps prevent side effects due to drug reactions and toxic chemicals']

