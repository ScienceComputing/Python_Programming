data = [ 'XYZ', 90, 71.1, (2023, 12, 21) ] 
_, shares, price, _ = data
shares
price

# Extended unpacking
data = [ 'XYZ', 90, 71.1, (2023, 12, 21) ]
_, shares, price, (year, *_) = data
shares
price
year

data = ( 'XYZ', 90, 71.1, (2023, 12, 21) )
_, shares, price, (year, *_) = data
shares
price
year
