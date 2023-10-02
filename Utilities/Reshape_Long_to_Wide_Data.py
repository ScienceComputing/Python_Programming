# Reshape the long format data with 3 columns (barcode; gene; count) to a barcode x gene count matrix
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pivot.html
scRNA_raw_wide = scRNA_raw.pivot(index='barcode_id', columns='gene', values='count')
scRNA_raw_wide.head()
