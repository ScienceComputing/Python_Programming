num = 100**10
print(f"{num:,}") 
# 100,000,000,000,000,000,000

type(f"{num:,}")
# <class 'str'>
type(print(f"{num:,}"))
# <class 'NoneType'>
# Notice that printing a value but not returning a value will result in <NoneType>.
