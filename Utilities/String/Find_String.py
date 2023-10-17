str1 = 'Cysteine helps prevent side effects due to drug reactions and toxic chemicals'

# Method 1: .find()
str1.find('Cysteine') # The find method returns the lowest index in the string where it can find the substring
# 0

str1.find('Alanine')
# -1

str1.find('Cysteine', 1, 9)
# -1

# Method 2: .index()
str1.index('Cysteine')
# 0

str1.index('Alanine')
# ValueError: substring not found

try:
    str1.index('Alanine')
except ValueError:
    print("The string you've input are not found.")
               
# Method 3: str.contains() or str.startswith()
import pandas as pd
df_col = adata.obs['sm_name']
is_ONX0912 = df_col.str.contains('ONX 0912')
df_col[is_ONX0912]
