# Unpack lists
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

df = pd.DataFrame(columns=[*adata_cell_pop.var_names, *obs_to_keep])

# The * operator is used to unpack elements from the lists (or any iterable) adata_cell_pop.var_names and obs_to_keep. 
# This operator is often used to unpack iterables in Python.
# For example, if adata_cell_pop.var_names is ['gene1', 'gene2', 'gene3'] and obs_to_keep is ['age', 'gender'], then [*adata_cell_pop.var_names, *obs_to_keep] becomes ['gene1', 'gene2', 'gene3', 'age', 'gender'].
