# Reshape the long format data with 3 columns (barcode; gene; count) to a barcode x gene count matrix
scRNA_raw_wide = scRNA_raw.pivot(index='barcode_id', columns='gene', values='count', fill_value=0)
scRNA_raw_wide.head()
