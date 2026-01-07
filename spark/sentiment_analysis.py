from pyspark.sql.functions import udf, col, substring # Added substring
from pyspark.sql.types import StringType
from textblob import TextBlob
from spark_session import get_spark_session

spark = get_spark_session("SentimentAnalysis")

df = spark.read.csv(
    "data/raw/US_Airline_tweets.csv", 
    header=True, 
    inferSchema=True, 
    quote='"', 
    escape='"'
)
df = df.select("text", "tweet_created").dropna()

def analyze_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

sentiment_udf = udf(analyze_sentiment, StringType())

# Fix: Extract 10 characters (yyyy-MM-dd) to avoid the timezone/null issue
df_sentiment = df.withColumn("sentiment", sentiment_udf(col("text"))) \
    .withColumn("date", substring(col("tweet_created"), 1, 10))

# ✅ Save processed data
df_sentiment.write.mode("overwrite").parquet("data/processed/US_Airline_tweets")

print("Sentiment analysis completed and saved successfully.")