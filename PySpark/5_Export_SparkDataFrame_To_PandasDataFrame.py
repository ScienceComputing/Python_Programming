# Construct a SQL query
query = "SELECT * FROM meta_info WHERE mt_percent < 0.1 "

# Run the query
meta_info_mt_filtered = RNA_velocity.sql(query)

# Convert the results to a pandas DataFrame
meta_info_mt_filtered_pd = meta_info_mt_filtered.toPandas()

# Print the head of meta_info_mt_filtered_pd
print(meta_info_mt_filtered_pd)
