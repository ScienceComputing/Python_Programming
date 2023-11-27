# Create a dictionary
my_dict = {}
my_yogurt = {
  'kefir': 6.9,
  'filmjolk': 4.6,
  'regular yogurt': 3.7
}
print(my_yogurt['filmjolk'])
print(my_yogurt.get['filmjolk2']) # None

def make_dict(**kwargs):
    return kwargs

make_dict(alpha = 1, beta = 2, gamma = 6)
# {'alpha': 1, 'beta': 2, 'gamma': 6}

# Obtain items
print(my_yogurt.items())
print(my_yogurt.keys())
print(my_yogurt.values())

# Add new item
my_yogurt['filmjolk2': 5.6]
print(my_yogurt.items())

# Modify the value
my_yogurt['regular yogurt'] = 3.5
print(my_yogurt['regular yogurt'])

# Delete a dictionary
del my_yogurt

# Remove a key-value pair
del my_yogurt['regular yogurt']

# Empty a dictionary
my_yogurt.clear()

# Iterate a dictionary
for key, value in my_yogurt.items():
  print(f'\nproduct: {key}')
  print(f'price: {value}')

for key, value in my_yogurt.items():
  print(f"The price of the {key} is {value}.")

# Iterate the key
for key in my_yogurt:
  print(f'\nproduct: {key}')

# Iterate the value
for value in my_yogurt.values():
  print(f'\nprice: {value}')
