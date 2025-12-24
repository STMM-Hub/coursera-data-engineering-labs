# 🛠 Apache Airflow ETL Pipeline — Toll Data

This project demonstrates an **end-to-end ETL pipeline orchestrated using Apache Airflow**, completed as part of the **IBM Data Engineering Professional Certificate**.

The DAG processes toll collection data from multiple file formats, consolidates them, applies transformations, and produces a clean dataset ready for downstream analytics.

---

## 📁 Files
| File | Description |
|------|------------|
| **etl_toll_data_dag.py** | Apache Airflow DAG defining the ETL workflow using BashOperator tasks |

---

## 🧩 ETL Workflow Overview

The DAG `ETL_toll_data` is scheduled to run **daily** and consists of the following steps:

### 1️⃣ Unzip Raw Data
- Extracts compressed toll data files (`.tgz`)
- Source files include CSV, TSV, and fixed-width formats

### 2️⃣ Extract Data
- **CSV extraction:**  
  Extracts `Rowid`, `Timestamp`, `Anonymized Vehicle Number`, and `Vehicle Type`
- **TSV extraction:**  
  Extracts `Number of Axles`, `Tollplaza ID`, and `Tollplaza Code`
- **Fixed-width extraction:**  
  Extracts `Type of Payment Code` and `Vehicle Code`

### 3️⃣ Consolidate Data
- Merges extracted data from all sources into a single file:
