# Conventional way to construct a multi-dictionary from a dictionary
stock_data_list = {
    'GOOG': [136.23, 135.21, 130.75, 137.25],
    'AAPL': [150.25, 151.50, 149.75, 148.60],
    'MSFT': [305.20, 307.40, 303.80, 305.60]
}
stock_data={}
for symbol, price_list in stock_data_list.items():
    if symbol not in stock_data:
        stock_data[symbol] = [] # Initialize the first value
    stock_data[symbol].extend(price_list)

print(stock_data)

# Smart way to construct a multi-dictionary from a dictionary
stock_data=defaultdict(list)
for symbol, price_list in stock_data_list.items():
    stock_data[symbol].extend(price_list)

print(stock_data)
print(stock_data['GOOG'])


# Create a multi-dictionary that maps keys to more than one value
# If we are interested in preserving the insertion order of the items, we could build a list-based multi-dictionary
stock_data_list = {
    'GOOG': [136.23, 135.21, 130.75, 137.25],
    'AAPL': [150.25, 151.50, 149.75, 148.60],
    'MSFT': [305.20, 307.40, 303.80, 305.60]
}

# If we are interested in eliminating the duplicates and do not care about the insertion order of the items, we could build a set-based multi-dictionary
stock_data_set = {
    'GOOG': {136.23, 135.21, 130.75, 137.25},
    'AAPL': {150.25, 151.50, 149.75, 148.60},
    'MSFT': {305.20, 307.40, 303.80, 305.60}
}

print(stock_data_list['GOOG'])
print(stock_data_set['GOOG'])

# An alternative approach to construct a multi-dictionary
from collections import defaultdict
stock_data_list = defaultdict(list)
stock_data_list['GOOG'].append(136.23)
stock_data_list['GOOG'].append(135.21)
stock_data_list['GOOG'].append(130.75)
stock_data_list['GOOG'].append(137.25)
print(stock_data_list)
# defaultdict(<class 'list'>, {'GOOG': [136.23, 135.21, 130.75, 137.25]})
print(stock_data_list['GOOG'])
# [136.23, 135.21, 130.75, 137.25]

stock_data_set = defaultdict(set)
stock_data_set['GOOG'].add(136.23)
stock_data_set['GOOG'].add(135.21)
stock_data_set['GOOG'].add(130.75)
stock_data_set['GOOG'].add(137.25)
print(stock_data_set['GOOG'])

# Caveat: defaultdict will automatically create values for non-exisitng keys
stock_data_set['MSFT']
print(stock_data_set)
