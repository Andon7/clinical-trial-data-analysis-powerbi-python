# Clinical Trial Data Analysis & Dashboard (Python + Power BI)

## Project Overview
This project presents an end-to-end data analytics solution for monitoring a Phase II clinical trial. It combines **data cleaning in Python** with **interactive dashboards in Power BI** to track study performance, safety, and data quality.

The goal was to transform raw clinical data into structured datasets and deliver actionable insights for stakeholders to support timely and informed decision-making.

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
   - Clinical trial dataset provided as a multi-sheet Excel file  

2. **Data Cleaning & Preparation (Python)**
   - Data validation and transformation  
   - Handling missing and inconsistent values  
   - Feature engineering for key metrics  

3. **Data Export**
   - Clean datasets exported as structured CSV files  

4. **Data Visualization (Power BI)**
   - Interactive dashboards built using DAX and data modeling  

---

## Data Preparation (Python)

The raw datasets were cleaned and transformed to ensure accuracy and usability.

### Key Cleaning Steps:
- Standardized date formats across all datasets  
- Handled missing values (e.g., screen failures, unresolved queries)  
- Created calculated fields (e.g., days between events, flags for key metrics)  
- Standardized categorical values (e.g., Yes/No fields)  
- Split multi-sheet data into structured datasets  

These steps ensured reliable downstream analysis and reporting.

---

## Data Structure

- `/data/raw` → Original dataset  
- `/data/processed` → Cleaned datasets used for analysis  

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

### Safety Dashboard
![Safety Dashboard](images/safety-dashboard.png)  
*Insights into adverse events and safety trends.*

### Query Dashboard
![Query Dashboard](images/query-dashboard.png)  
*Monitoring of data quality and query resolution performance.*

---

## Tools & Technologies
- Python (Pandas, NumPy)  
- Power BI  
- Power Query  
- DAX (Data Analysis Expressions)  

---

## How to Use
1. Explore raw data in `/data/raw`  
2. Review cleaned datasets in `/data/processed`  
3. Open the `.pbix` file using Power BI Desktop  
4. Interact with dashboards using filters and slicers  

Tip: Use filters (site, country, date) to explore trends and drill down into performance metrics.

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

## Project Structure
