# Estimate the proportion of positives/negatives/zeros in a list
def calc_prop(data): 
    total = len(data)
    num_pos = sum([1 for i in data if i > 0])
    num_neg = sum([1 for i in data if i < 0])
    num_zero = total - (num_pos + num_neg)
    
    ratio_pos = num_pos / total
    ratio_neg = num_neg / total
    ratio_zero = num_zero / total
    
    print(f'{ratio_pos:.2f}')
    print(f'{ratio_neg:.2f}')
    print(f'{ratio_zero:.2f}')

sample = [-9, 2, 3, 0, 0, 2, 3, 6]
calc_prop(data=sample)
# 0.62
# 0.12
# 0.25
