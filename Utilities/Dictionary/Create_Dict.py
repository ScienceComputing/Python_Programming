my_dict = {}
my_yogurt = {
  'kefir': 6.9,
  'filmjolk': 4.6,
  'regular yogurt': 3.7
}
print(my_yogurt['filmjolk'])
print(my_yogurt.get['filmjolk2']) # None

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
