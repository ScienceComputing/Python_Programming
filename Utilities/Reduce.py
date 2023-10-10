# Import reduce from functools
from functools import reduce

fruits = ["apple", "banana", "cherry"]
result = reduce(lambda item1, item2: item1 + " " + item2, fruits)
print(result)
