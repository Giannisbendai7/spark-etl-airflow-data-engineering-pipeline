# spark-etl-airflow-data-engineering-pipeline
End-to-end data engineering pipeline using PySpark for ETL processing, SQL analytics, and business KPI generation from raw car sales data.
# 🚀 Car Sales Data Engineering Pipeline

## 📊 Overview
This project implements an end-to-end data engineering pipeline using PySpark and SQL to process raw car sales data, perform ETL transformations, and generate business insights.

The goal is to simulate a real-world production-style data pipeline similar to those used in analytics and finance companies.

---

## ⚙️ Architecture

Raw CSV Data  
↓  
PySpark ETL (Cleaning, Transformation, Feature Engineering)  
↓  
Processed Dataset  
↓  
SQL Analytics Layer  
↓  
Business KPIs & Reports  

---

## 🧰 Tech Stack

- Python
- PySpark
- SQL
- Data Engineering (ETL Concepts)

---

## 🔄 ETL Process

### 1. Extract
Load raw car sales dataset from CSV.

### 2. Transform
- Remove null values
- Create new features (Revenue = Price × Commission Rate)
- Aggregate data by car brand

### 3. Load
Export processed results for analytics and reporting.

---

## 📊 Business Insights

- Top performing car brands by total sales
- Average revenue per transaction
- Commission performance analysis
- High-value sales filtering

---

## ▶️ How to Run

```bash
python spark_jobs/etl_pipeline.py
