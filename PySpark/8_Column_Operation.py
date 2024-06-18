# Create the Spark DataFrame
RNA_velocity_train = RNA_velocity_spark.table("RNA_velocity_train")
# We are in a SparkSession called RNA_velocity_spark

# Show the head
RNA_velocity_train.show()

# Add a new column
RNA_velocity_train = RNA_velocity_train.withColumn("duration_hrs", RNA_velocity_train.time/60) 
