from pyspark.sql.functions import col, lower, regexp_replace
from spark_session import get_spark_session

spark = get_spark_session("DataCleaning")

# Load CSV
df = spark.read.csv("data/raw/US_Airline_tweets.csv", header=True, inferSchema=True)

# Keep only text & timestamp columns
df = df.select("text", "tweet_created").dropna()

# Clean text
df_clean = df.withColumn(
    "clean_text",
    lower(regexp_replace(col("text"), r"http\S+|[^a-zA-Z\s]", ""))
)


