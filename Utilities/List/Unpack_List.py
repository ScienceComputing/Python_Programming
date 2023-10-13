# Unpacking lists
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

line = 'https://ftp.ncbi.nlm.nih.gov/geo/series/GSE85nnn/GSE85241/suppl/GSE85241%5Fcellsystems%5Fdataset%5F4donors%5Fupdated%2Ecsv%2Egz'
ncbi, base_name = line.split('suppl/')
base_name
