# Construct a SQL query
query = "FROM RNA_velocity SELECT * LIMIT 10"

# Get the first 10 rows of RNA velocities; here we are in the SparkSession called RNA_velocity_spark
RNA_velocity_10 = RNA_velocity_spark.sql(query)

# Show the results
RNA_velocity_10.show()
