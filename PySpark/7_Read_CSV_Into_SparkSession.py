# Set up the file path
file_path = "/usr/local/share/datasets/RNA_velocity_data.csv"

# Read in the RNA_velocity data; here we are in the RNA_velocity SparkSession
RNA_velocity_data = RNA_velocity.read.csv(file_path, header=True)

# Show the data
RNA_velocity_data.show()
