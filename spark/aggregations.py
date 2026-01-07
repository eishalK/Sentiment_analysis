from pyspark.sql.functions import count
from spark_session import get_spark_session

spark = get_spark_session("Aggregations")

# Load already-processed data
df = spark.read.parquet("data/processed/US_Airline_tweets")

# Sentiment distribution
sentiment_count = df.groupBy("sentiment").agg(count("*").alias("count"))
sentiment_count.show()

sentiment_count.write.mode("overwrite").parquet(
    "data/processed/sentiment_summary"
)

# Daily sentiment trend
sentiment_trend = (
    df.groupBy("date", "sentiment")
      .count()
      .orderBy("date")
)

sentiment_trend.show(5)

sentiment_trend.write.mode("overwrite").parquet(
    "data/processed/sentiment_trend"
)
