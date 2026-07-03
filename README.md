# Universal CSV Data Quality Analyzer

##  Overview

Universal CSV Data Quality Analyzer is a Python-based tool that automatically evaluates the quality of any CSV dataset. It helps identify common data quality issues such as missing values, duplicate records, inconsistent data types, invalid entries, and outliers. The tool generates detailed reports, visualizations, and an overall data quality score, enabling users to clean and prepare data efficiently before analysis, machine learning, or business intelligence tasks.

---

##  Features

*  Analyze any CSV dataset
*  Detect missing values and duplicate records
*  Identify inconsistent data types
*  Detect invalid or inconsistent data entries
*  Perform outlier detection for numerical columns
*  Generate visualizations for data quality metrics
*  Create detailed PDF and CSV reports
*  Calculate an overall Data Quality Score
*  Fast and easy-to-use command-line interface

---

##  Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* ReportLab
* CSV
* OS

---

##  Project Structure

```text
Universal_CSV_Data_Quality_Analyzer/
│
├── data/                 # Input CSV files
├── reports/              # Generated PDF and CSV reports
├── charts/               # Data quality visualizations
├── analyzer.py           # Core data quality analysis
├── report.py             # PDF report generation
├── visualization.py      # Graph generation
├── utils.py              # Helper functions
├── main.py               # Main application
├── requirements.txt
└── README.md
```

---

##  Use Cases

* Data Cleaning
* Data Engineering
* Data Analytics
* Machine Learning Data Preparation
* ETL Validation
* Business Intelligence
* Academic Research

---

##  Data Quality Checks

* Missing Values Analysis
* Duplicate Record Detection
* Data Type Validation
* Null Percentage Calculation
* Outlier Detection
* Unique Value Analysis
* Column Statistics
* Overall Data Quality Score

---

##  How to Run

1. Clone the repository.
2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Place your CSV file inside the `data/` folder.
4. Run the application:

   ```bash
   python main.py
   ```
5. View the generated reports and charts in the `reports/` and `charts/` folders.

---

##  Future Enhancements

* Interactive Streamlit dashboard
* Excel (.xlsx) support
* Automated data cleaning suggestions
* AI-powered anomaly detection
* Database connectivity (MySQL, PostgreSQL)
* Email report generation
* Cloud storage integration (AWS S3, Azure Blob, Google Cloud Storage)

---

##  Contributions

Contributions, feature requests, and suggestions are welcome. Feel free to fork the repository and submit a pull request.

---

##  License

This project is intended for educational and portfolio purposes. You are welcome to modify and extend it for your own use.

## Author:Sai Chethana

-  B.Tech in Computer Science and Artificial Intelligence
-  Aspiring Software Developer | Python | SQL | Data Analytics
-  Passionate about building real-world Python applications and solving data-driven problems.
