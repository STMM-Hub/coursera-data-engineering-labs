# 🧠 Python for Data Engineering — ETL Projects

This folder contains two end-to-end ETL (Extract, Transform, Load) projects completed as part of the **IBM Data Engineering Professional Certificate**.  
Each project demonstrates key data engineering tasks such as web scraping, data transformation, and database integration using Python.

---

## 📁 Files Included
| File | Description |
|------|--------------|
| **ETL Project Bank.py** | Extracts data on the world’s largest banks, transforms market capitalization data into multiple currencies, and loads it into a local SQLite database. |
| **ETL Project GDP.py** | Extracts and transforms global GDP data from an online source and stores the results in both CSV and SQLite formats for analysis. |

---

## 🧩 ETL Project — Banks

**Objective:**  
To build a mini ETL pipeline that collects the latest data on the largest banks by market capitalization from Wikipedia, transforms it using exchange rates, and loads it into a relational database.

**Key Steps:**
1. **Extract:** Scrapes the HTML table of the *List of Largest Banks* from Wikipedia using `requests` and `BeautifulSoup`.  
2. **Transform:** Converts market capitalization from USD to GBP, EUR, and INR using exchange rates provided in a CSV file.  
3. **Load:** Saves the processed data to both a CSV file and a SQLite database (`Banks.db`), then runs SQL queries for validation.

**Technologies Used:**
- Python (`requests`, `pandas`, `numpy`, `sqlite3`, `BeautifulSoup`)
- Data persistence: CSV and SQLite
- Logging using custom `log_progress()` function

**Output Files:**
- `Largest_banks_data.csv`
- `Banks.db` (SQLite database)

---

## 🧩 ETL Project — GDP

**Objective:**  
To perform similar ETL operations on global GDP data, transforming and storing economic indicators for analytical use.

**Key Steps:**
1. **Extract:** Retrieves GDP data from a specified online dataset or web page.  
2. **Transform:** Cleans, normalizes, and structures the data for analysis.  
3. **Load:** Stores results in a SQLite database and CSV file for downstream reporting.

**Technologies Used:**
- Python (`pandas`, `sqlite3`)
- ETL principles (Extract → Transform → Load)
- Data persistence and validation via SQL queries

---

## ⚙️ How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/<yourusername>/ibm-data-engineering-portfolio.git
   cd ibm-data-engineering-portfolio/01-python-for-data-engineering

