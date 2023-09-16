# We have the option to create custom Python functions by employing the 'def' keyword, incorporating function headers, docstrings, and defining function bodies. 
# Nonetheless, there exists a faster method for crafting functions spontaneously, referred to as lambda functions, as they make use of the 'lambda' keyword.

# lambda argument(s) : expression 
lambda : print('Hello Anonymous Function!')
greet = lambda : print('Hello Anonymous Function!')
greet()

greet_stock = lambda stock_name: print('Welcome to the world of', stock_name, 'stocks!')
greet_stock('GOOGL')

raise_to_power = lambda m, n: m ** n
raise_to_power(8, 8)

# The map function accepts two parameters: a function and a sequence, e.g., a list, and then proceeds to apply the specified function to each element within the given sequence.
num_list = [6, 8, 15, 0, 90, 50]
cubic_all = map(lambda num: num ** 3, num_list)
print(cubic_all)
print(list(cubic_all))
