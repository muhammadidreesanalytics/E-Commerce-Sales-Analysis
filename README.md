# 🛒 E-Commerce Sales Dashboard

## 📊 Project Overview

This project is an interactive **E-Commerce Sales Dashboard** developed using **Microsoft Power BI** to analyze sales performance and generate meaningful business insights.

The project uses **10,000 e-commerce transaction records** and covers sales, profit, orders, products, categories, customers, and regional performance.

---

## 🎯 Project Objective

The main objective of this project is to transform raw e-commerce data into an interactive dashboard that helps understand:

* Overall sales performance
* Profit performance
* Order trends
* Product performance
* Category performance
* Regional sales
* Monthly sales trends
* Top-performing products

---

## 🛠️ Tools & Technologies

* **Power BI** — Dashboard development & visualization
* **SQL** — Data querying and analysis
* **Python** — Data analysis and data preparation
* **Pandas** — Data cleaning and transformation
* **Excel / CSV** — Dataset

---

## 📁 Project Files

| File                       | Description                                  |
| -------------------------- | -------------------------------------------- |
| `README.md`                | Project documentation                        |
| `Ecommerce_10000_Rows.csv` | E-commerce dataset containing 10,000 records |
| `Ecommerce_Dashboard.png`  | Dashboard preview                            |
| `SQL_Analysis.sql`         | SQL queries used for analysis                |
| `Python_Analysis.py`       | Python/Pandas analysis                       |
| `Ecommerce_Dashboard.pbix` | Power BI dashboard file                      |

---

## 📈 Dashboard KPIs

The dashboard includes the following key performance indicators:

* **Total Sales**
* **Total Profit**
* **Total Orders**
* **Total Quantity**
* **Average Order Value**

---

## 📊 Dashboard Features

### Sales Analysis

* Sales by month
* Sales trends
* Sales by category
* Sales by region

### Product Analysis

* Top products
* Product sales performance
* Product profitability

### Customer Analysis

* Customer order activity
* Customer sales contribution

### Profit Analysis

* Total profit
* Profit by category
* Profit trends
* Profit performance by region

---

## 🧮 DAX Measures

### Total Sales

```DAX
Total Sales =
SUM(EcommerceData[Sales])
```

### Total Profit

```DAX
Total Profit =
SUM(EcommerceData[Profit])
```

### Total Orders

```DAX
Total Orders =
DISTINCTCOUNT(EcommerceData[Order_ID])
```

### Total Quantity

```DAX
Total Quantity =
SUM(EcommerceData[Quantity])
```

### Average Order Value

```DAX
Average Order Value =
DIVIDE([Total Sales], [Total Orders], 0)
```

> **Note:** If your Power BI table has a different name, replace `EcommerceData` with your actual table name.

---

## 🗃️ Dataset

The dataset contains **10,000 e-commerce transaction records**.

### Main Dataset Columns

```text
Order_ID
Customer_ID
Customer_Name
Product_ID
Product_Name
Category
Quantity
Price
Sales
Profit
Region
City
Order_Date
Payment_Method
```

---

## 🔍 SQL Analysis

SQL was used to analyze the dataset and answer business-related questions such as:

* What are the total sales?
* What are the total profits?
* Which products generate the highest sales?
* Which categories perform best?
* Which regions generate the most revenue?
* What are the monthly sales trends?
* Which products generate the highest profit?

SQL queries are available in:

`SQL_Analysis.sql`

---

## 🐍 Python Analysis

Python and Pandas were used for data analysis and preparation.

The Python analysis includes:

* Loading the dataset
* Checking missing values
* Checking duplicate records
* Data type verification
* Basic statistical analysis
* Sales and profit analysis
* Grouping and aggregation
* Preparing data for visualization

Python code is available in:

`Python_Analysis.py`

---

## 🖼️ Dashboard Preview

![E-Commerce Sales Dashboard](Ecommerce_Dashboard.png)

---

## 💡 Key Business Questions

This dashboard helps answer questions such as:

1. What are the total sales and profit?
2. How are sales changing over time?
3. Which category generates the most sales?
4. Which products are top performers?
5. Which region contributes the most sales?
6. Which products generate the highest profit?
7. How many orders have been placed?
8. What is the average order value?

---

## 📌 Project Workflow

```text
Raw Dataset
     ↓
Data Cleaning
     ↓
SQL Analysis
     ↓
Python / Pandas Analysis
     ↓
Power BI Data Modeling
     ↓
DAX Measures
     ↓
Interactive Dashboard
     ↓
Business Insights
```

---

## 🚀 Skills Demonstrated

This project demonstrates practical skills in:

* Data Cleaning
* Data Analysis
* SQL
* Python
* Pandas
* Power BI
* DAX
* Data Visualization
* Dashboard Development
* Business Intelligence
* Business Analytics

---

## 👨‍💻 Author

**Muhammad Idrees**

Data Analyst | Power BI | SQL | Python | Excel

---

## 📂 Repository Structure

```text
E-Commerce-Dashboard/
│
├── README.md
├── Ecommerce_10000_Rows.csv
├── Ecommerce_Dashboard.png
├── SQL_Analysis.sql
├── Python_Analysis.py
└── Ecommerce_Dashboard.pbix
```

---

## ⭐ Project Status

**Completed — Portfolio Project**

