from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, avg

def run_etl():
    spark = SparkSession.builder \
        .appName("CarSalesPipeline") \
        .getOrCreate()

    df = spark.read.csv(
        "data/car_sales_data.csv",
        header=True,
        inferSchema=True
    )

    df = df.dropna()

    df = df.withColumn(
        "Revenue",
        col("Sale Price") * col("Commission Rate")
    )

    report = df.groupBy("Car Make") \
        .agg(
            sum("Sale Price").alias("Total_Sales"),
            avg("Revenue").alias("Avg_Revenue")
        )

    report.write.mode("overwrite").csv(
        "output/car_sales_report"
    )

    spark.stop()

if __name__ == "__main__":
    run_etl()
