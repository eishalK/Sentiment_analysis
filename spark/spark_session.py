import os
import sys
from pyspark.sql import SparkSession

def get_spark_session(app_name):
 
    os.environ['PYSPARK_PYTHON'] = sys.executable
    os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
    os.environ['JAVA_HOME'] = r'C:\Program Files\Eclipse Adoptium\jdk-11.0.29.7-hotspot'
    os.environ['HADOOP_HOME'] = r'C:\hadoop'
    
    return SparkSession.builder \
        .appName(app_name) \
        .master("local[*]") \
        .getOrCreate()