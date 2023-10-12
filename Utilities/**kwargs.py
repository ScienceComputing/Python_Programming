# https://realpython.com/python-kwargs-and-args/
def make_dict(**kwargs):
    return kwargs

make_dict(alpha = 1, beta = 2)
# {'alpha': 1, 'beta': 2}
