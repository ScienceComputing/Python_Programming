from pyspark import SparkConf, SparkContext
conf = SparkConf().setMaster("local").setAppName("RNAVelocity")
sc = SparkContext.getOrCreate(conf = conf)

# Verify SparkContext
print(sc)

# Print Spark version
print(sc.version)
