# Import SparkSession from pyspark.sql
from pyspark.sql import SparkSession

# Make a new SparkSession called RNA_velocity_spark
RNA_velocity_spark = SparkSession.builder.getOrCreate()
# The SparkSession.builder.getOrCreate() method returns an existing SparkSession if there's already one in the environment, or creates a new one if necessary.

# Print RNA_velocity_spark
print(RNA_velocity_spark)
