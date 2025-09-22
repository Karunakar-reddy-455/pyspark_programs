from pyspark.sql.connect.session import SparkSession

spark = SparkSession.builder.appName("Student").getOrCreate()

data = [
    (1,"Jagan",50),
    (2,"Modi",70)
]