import streamlit as st
import matplotlib.pyplot as plt
from pyspark.sql import SparkSession

# --------------------------------------------------
# Page Config
# --------------------------------------------------
st.set_page_config(
    page_title="Social Media Sentiment Analysis",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------------------
# Header
# --------------------------------------------------
st.markdown(
    """
    <h1 style='text-align: center;'>📊 Social Media Sentiment Analysis</h1>
    <p style='text-align: center; color: gray;'>
    Big Data Analytics using PySpark & Streamlit
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

# --------------------------------------------------
# Spark Session (cached)
# --------------------------------------------------
@st.cache_resource
def get_spark():
    spark = (
        SparkSession.builder
        .appName("StreamlitUI")
        .getOrCreate()
    )
    spark.sparkContext.setLogLevel("ERROR")
    return spark

spark = get_spark()

# --------------------------------------------------
# Load Preprocessed Data (cached)
# --------------------------------------------------
@st.cache_data
def load_data():
    summary = spark.read.parquet("data/processed/sentiment_summary")
    trend = spark.read.parquet("data/processed/sentiment_trend")
    return summary.toPandas(), trend.toPandas()

summary_pd, trend_pd = load_data()

# --------------------------------------------------
# KPI Section
# --------------------------------------------------
total_records = trend_pd["count"].sum()
positive = summary_pd.loc[summary_pd["sentiment"] == "Positive", "count"].values[0]
negative = summary_pd.loc[summary_pd["sentiment"] == "Negative", "count"].values[0]

k1, k2, k3 = st.columns(3)

k1.metric("📌 Total Tweets Analyzed", f"{total_records:,}")
k2.metric("😊 Positive Tweets", f"{positive:,}")
k3.metric("😠 Negative Tweets", f"{negative:,}")

st.divider()

# --------------------------------------------------
# Charts Section
# --------------------------------------------------
col1, col2 = st.columns(2)

# Pie Chart
with col1:
    st.subheader("Sentiment Distribution")

    fig, ax = plt.subplots(facecolor="#0E1117")
    ax.set_facecolor("#0E1117")

    ax.pie(
        summary_pd["count"],
        labels=summary_pd["sentiment"],
        autopct="%1.1f%%",
        startangle=90
    )
    ax.axis("equal")

    st.pyplot(fig)

# Line Chart
with col2:
    st.subheader("Daily Sentiment Trend")

    pivot_df = (
        trend_pd
        .pivot(index="date", columns="sentiment", values="count")
        .fillna(0)
    )

    st.line_chart(pivot_df)

st.divider()

# --------------------------------------------------
# Data Preview
# --------------------------------------------------
st.subheader("📄 Aggregated Data Preview")
st.dataframe(
    trend_pd.head(25),
    use_container_width=True
)

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown(
    """
    <hr>
    <p style='text-align:center; font-size: 14px; color: gray;'>
    Built using PySpark for Big Data Processing & Streamlit for Visualization
    </p>
    """,
    unsafe_allow_html=True
)
