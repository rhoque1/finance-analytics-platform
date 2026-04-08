# Personal Finance Analytics Platform (ETL Pipeline)

An automated, end-to-end data engineering pipeline that transforms raw bank exports into interactive financial intelligence.

## 🏗️ Architecture
- **Extract**: Ingests raw CSV data from Chase bank exports.
- **Transform**: Python (Pandas) pipeline that cleans data and utilizes an **AI-Assisted Master Mapping** system for intelligent expense categorization.
- **Load**: Automated loading into a **SQLite** relational database to ensure data integrity and concurrency.
- **Visualize**: Interactive **Power BI** dashboard utilizing custom **DAX** measures for chronological trend analysis and category-level drill-downs.
- **Automation**: One-click orchestration via Windows Batch scripting.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Libraries:** Pandas, SQLite3
- **Database:** SQLite
- **BI Tool:** Power BI (DAX)
- **Automation:** Windows Batch

## 🚀 How it Works
1. Drop raw bank CSVs into `data/raw/`.
2. Run `run_pipeline.bat` to execute the full ETL cycle.
3. Refresh the Power BI dashboard to visualize updated trends.