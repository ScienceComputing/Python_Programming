from pyspark import SparkConf, SparkContext
conf = SparkConf().setMaster("local").setAppName("RNA_velocity")
sc = SparkContext.getOrCreate(conf = conf)

# Verify SparkContext
print(sc)

# Print Spark version
print(sc.version)
