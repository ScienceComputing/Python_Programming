import pandas as pd

# Create a pandas data frame
RNA_velocity_initial_value = pd.DataFrame(np.random.random(7))

# Create a Spark data frame from a pandas data frame
RNA_velocity_initial_value_spark = RNA_velocity.createDataFrame(RNA_velocity_initial_value)

# Examine the tables in the catalog
print(RNA_velocity.catalog.listTables())

# Add the Spark data frame to the catalog and name this data frame as "RNA_velocity_initial"
RNA_velocity_initial_value_spark.createOrReplaceTempView("RNA_velocity_initial")

# Examine the tables in the catalog again
print(RNA_velocity.catalog.listTables())
