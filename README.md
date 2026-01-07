# 📊 Social Media Sentiment Analysis Dashboard

## 1. Project Overview

This project analyzes **large-scale social media data** (e.g., tweets) to extract meaningful **sentiment insights**. It leverages **PySpark** for distributed data processing and **Streamlit** for building an interactive dashboard.

The platform allows users to:

- Explore sentiment distribution (Positive / Negative / Neutral)
- Visualize sentiment trends over time
- Preview aggregated data
- Gain insights from large-scale datasets efficiently

---

## 2. Motivation

Social media platforms generate massive volumes of data every second. Traditional tools like Pandas struggle to handle such large datasets efficiently.

This project demonstrates **Big Data processing with Spark** and **visualization with Streamlit**, offering:

- **Scalable data processing**
- **Fast computation with distributed architecture**
- **Interactive and user-friendly dashboards**

---

## 3. Features

| Feature                     | Description                                                              |
| --------------------------- | ------------------------------------------------------------------------ |
| Large-scale data processing | Uses PySpark to handle thousands of tweets efficiently                   |
| Sentiment Analysis          | Text is analyzed for sentiment using TextBlob via Spark UDFs             |
| Aggregations                | Sentiment counts and daily trends are precomputed for fast visualization |
| Interactive Dashboard       | Streamlit UI shows KPIs, pie charts, line charts, and raw data           |
| Dark Theme                  | Professional dark UI for better readability                              |

---

## 4. Project Structure

```
SentimentAnalysis_BigData/
│
├── data/
│   ├── raw/
│   │   └── twitter_data.csv          # Raw dataset
│   └── processed/
│       ├── US_Airline_tweets/        # Cleaned & preprocessed data
│       ├── sentiment_summary/        # Sentiment counts
│       └── sentiment_trend/          # Daily sentiment trends
│
├── spark/
│   ├── spark_session.py               # Spark session setup
│   ├── data_cleaning.py               # Load & clean raw data
│   ├── sentiment_analysis.py          # Compute sentiment using Spark UDFs
│   └── aggregations.py                # Aggregated data for visualization
│
├── ui/
│   └── app.py                         # Streamlit dashboard
│
├── .venv/                              # Virtual environment (optional)
├── requirements.txt                    # Python dependencies
└── README.md                           # Project documentation
```

---

## 5. Installation & Setup

### 5.1 Prerequisites

- Python 3.9+
- Java JDK 8 or 11 (required for Spark)
- pip (latest version recommended)

### 5.2 Install Dependencies

Use your preferred Python environment. Example (conda environment):

```bash
# (optional) create and activate conda env
conda create -n senti python=3.10 -y
conda activate senti

# install dependencies
pip install -r requirements.txt

# download TextBlob corpora
python -m textblob.download_corpora
```

If you use the project's provided conda environment or virtualenv, adapt commands accordingly.

---

## 6. How to Run

### 6.1 Step 1 — Preprocess & Analyze Data

Run these scripts to create parquet outputs under `data/processed/` (the Streamlit UI reads these parquet folders):

```bash
python spark/data_cleaning.py
python spark/sentiment_analysis.py
python spark/aggregations.py
```

After successful runs you should see output under `data/processed/sentiment_summary/` and `data/processed/sentiment_trend/`.

### 6.2 Step 2 — Launch Streamlit Dashboard

```bash
streamlit run ui/app.py
```

Open the URL Streamlit prints in your terminal (usually http://localhost:8501).

---

## 7. Usage

1. Open the dashboard in your browser.
2. View **KPIs** for total tweets, positive, and negative counts.
3. Explore **sentiment distribution** via pie chart.
4. Observe **daily sentiment trends** via line chart.
5. Preview **raw aggregated data** at the bottom of the dashboard.

---

## 8. Key Learnings

- Distributed computing with PySpark for large datasets
- Integrating NLP (TextBlob) with Spark for sentiment analysis
- Optimizing Streamlit dashboards with caching
- Visualizing Big Data insights interactively

---

## 9. Future Improvements

- Real-time streaming analysis using **Twitter API**
- Advanced NLP using **BERT / spaCy** for more accurate sentiment
- Deploy dashboard to **AWS EC2** or **Heroku**
- Add **interactive filters** (date ranges, hashtags, keywords)

---

## 10. References

- https://spark.apache.org/docs/latest/
- https://textblob.readthedocs.io/
- https://docs.streamlit.io/
- https://www.kaggle.com/crowdflower/twitter-airline-sentiment

