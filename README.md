# Clinical Trial Data Analysis & Dashboard (Python + Power BI)

## Project Overview
This project presents an end-to-end data analytics solution for monitoring a Phase II clinical trial. It combines **data cleaning in Python** with **interactive dashboards in Power BI** to track study performance, safety, and data quality.

The goal was to transform raw, multi-source clinical data into structured datasets and deliver actionable insights for stakeholders to support timely and informed decision-making.

---

## Business Context
Clinical trials require continuous monitoring to ensure:
- Efficient patient enrollment  
- Patient safety through adverse event tracking  
- High data quality and timely query resolution  

This project provides a centralized analytics solution across multiple study dimensions.

---

## End-to-End Workflow

1. **Raw Data Collection**
   - Multi-sheet clinical trial dataset (Excel)

2. **Data Cleaning & Preparation (Python)**
   - Data validation and transformation  
   - Handling missing and inconsistent values  
   - Feature engineering for key metrics  
   - Structuring multi-sheet data into analysis-ready datasets  

3. **Data Export**
   - Clean datasets initially exported as CSV  
   - Converted to Excel format for Power BI compatibility  

4. **Data Visualization (Power BI)**
   - Interactive dashboards built using DAX and data modeling  

---

## Key Contribution
This project demonstrates a complete data analytics workflow:
- Raw data ingestion and cleaning using Python  
- Feature engineering and dataset structuring  
- Business-focused dashboard development in Power BI  

It reflects a real-world analytics pipeline used in clinical trial monitoring.

---

## Data Preparation (Python)

The raw datasets were cleaned and transformed to ensure accuracy and usability.

### Key Cleaning Steps:
- Standardized date formats across all datasets  
- Handled missing values (e.g., screen failures, unresolved queries)  
- Created calculated fields (e.g., days between events, flags for key metrics)  
- Standardized categorical values (e.g., Yes/No fields)  
- Split multi-sheet data into structured datasets  

---

## Data Structure

```
data/
│
├── raw/
│   └── clinical_trial_data.xlsx
│
└── processed/
    ├── patients_clean.xlsx
    ├── sites_clean.xlsx
    ├── adverse_events_clean.xlsx
    └── queries_clean.xlsx
```

* `/data/raw` → Original dataset (multi-sheet Excel file)
* `/data/processed` → Cleaned datasets used in Power BI

> Cleaned datasets were first generated as CSV files in Python and later converted to Excel format for seamless integration with Power BI.

---

## Dashboards (Power BI)

### Enrollment Monitoring Dashboard
- Enrollment rate by site and country  
- Screen failure rate analysis  
- Time from screening to randomization  
- Identification of high- and low-performing sites  

---

### Safety Monitoring Dashboard
- Adverse events by site and country  
- Serious vs non-serious events  
- Distribution of adverse event types  
- Trend of adverse events over time  

---

### Query Resolution Dashboard
- Open, closed, and replied queries  
- Average query resolution time  
- Query trends over time  
- Data quality performance by site  

---

## Key Metrics
- Enrollment Rate  
- Screen Failure Rate  
- Time to Randomization  
- Adverse Event Rate (total & serious)  
- Query Resolution Time  
- Open vs Closed Queries  

---

## Dashboard Preview

### Enrollment Dashboard
![Enrollment Dashboard](images/enrollment-dashboard.png)  
*Overview of enrollment performance and site efficiency.*  
*Key insight: Variability across sites highlights differences in recruitment efficiency.*

---

### Safety Dashboard
![Safety Dashboard](images/safety-dashboard.png)  
*Insights into adverse events and safety trends.*  
*Key insight: Monitoring serious adverse events enables early detection of potential safety risks.*

---

### Query Dashboard
![Query Dashboard](images/query-dashboard.png)  
*Monitoring of data quality and query resolution performance.*  
*Key insight: Delays in query resolution may indicate operational inefficiencies at specific sites.*

---

## Tools & Technologies
- Python (Pandas, NumPy)  
- Power BI  
- Power Query  
- DAX (Data Analysis Expressions)  

---

## How to Use
1. Explore raw data in `/data/raw`  
2. Review cleaned datasets in `/data/processed` (Excel format used in Power BI)  
3. Open the `.pbix` file using Power BI Desktop  
4. Interact with dashboards using filters and slicers  

Tip: Use filters (site, country, date) to drill down into performance metrics.

---

## Key Insights
- Identified variability in enrollment performance across sites  
- Highlighted trends in adverse events and potential safety signals  
- Revealed delays in query resolution impacting data quality  
- Enabled early identification of operational risks  

---

## What I Learned
- Building an end-to-end data analytics pipeline  
- Data cleaning and transformation using Python  
- Designing business-focused dashboards in Power BI  
- Translating raw data into actionable insights  

---

## 📁 Project Structure

```
clinical-trial-dashboard/
│
├── README.md
├── clinical-trial-dashboard.pbix
│
├── python/
│   └── data_cleaning.py
│
├── data/
│   ├── raw/
│   │   └── clinical_trial_data.xlsx
│   │
│   └── processed/
│       ├── patients_clean.xlsx
│       ├── sites_clean.xlsx
│       ├── adverse_events_clean.xlsx
│       └── queries_clean.xlsx
│
├── images/
│   ├── enrollment-dashboard.png
│   ├── safety-dashboard.png
│   └── query-dashboard.png
```

---

## Note
> This project was developed as part of a technical assignment for a clinical data analyst role and has been independently implemented and enhanced for portfolio purposes.
