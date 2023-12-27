# .replace("word", "new", count)
str1 = 'Cysteine Cysteine helps prevent side effects due to drug reactions and toxic chemicals'
str1.replace('Cysteine ', '', 1)
# 'Cysteine helps prevent side effects due to drug reactions and toxic chemicals'


"""Clean the values in a feature of a ML dataset"""
# Remove ICD-10-CM code from the disease column
df_train['disease'] = df_train['disease'].str.replace('A15-A19:', '')
df_train
