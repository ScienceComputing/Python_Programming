# Unpacking tuples
data = ( 'XYZ', 90, 71.1, (2023, 12, 21) )
_, shares, price, (year, *_) = data
shares
price
year
