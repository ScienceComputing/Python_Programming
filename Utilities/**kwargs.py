# Reference: https://realpython.com/python-kwargs-and-args/
# We can use *args and **kwargs pass multiple arguments or keyword arguments to a function. 
def make_dict(**kwargs):
    return kwargs

make_dict(alpha = 1, beta = 2, gamma = 6)
# {'alpha': 1, 'beta': 2, 'gamma': 6}
