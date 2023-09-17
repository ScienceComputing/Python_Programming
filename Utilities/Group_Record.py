# Group records
scrna_data = [
    {'cell_barcode': 'CGTACGTA', 'gene': 'Gene1', 'expression': 10},
    {'cell_barcode': 'AGTACGTA', 'gene': 'Gene2', 'expression': 5},
    {'cell_barcode': 'CGTACGTA', 'gene': 'Gene3', 'expression': 15},
    {'cell_barcode': 'AGTACGTA', 'gene': 'Gene4', 'expression': 20},
    {'cell_barcode': 'TCAGTCAG', 'gene': 'Gene5', 'expression': 12},
]

from operator import itemgetter
from itertools import groupby

# Sort by the desired field first
# A crucial initial stage involves arranging the data based on the relevant field. Without proper sorting, groupby() won't organize the records as intended because it only considers consecutive items.
scrna_data.sort(key=itemgetter('expression'), reverse=True)

# Iterate in groups
for expression, record in groupby(scrna_data, key=itemgetter('expression')):
    print(expression)
    for x in record:
        print(' ', x)

# The objective is to organize the data based on expression, creating a large data structure that enables random access.
# It may not be required to sort the records beforehand. Therefore, if memory usage is not an issue, it might be more efficient to perform this operation rather than initially sorting the records and then iterating using 'groupby()'.
from collections import defaultdict

scrna_data_by_expression = defaultdict(list)
for data in scrna_data:
    scrna_data_by_expression[data['expression']].append(data)

for d in scrna_data_by_expression[10]:
    print(d)
