
### `SQL/ecommerce_analysis.sql`

```sql
CREATE DATABASE ecommerce_analysis;

USE ecommerce_analysis;

-- Total Sales
SELECT SUM(Sales) AS Total_Sales
FROM ecommerce_data;

-- Total Profit
SELECT SUM(Profit) AS Total_Profit
FROM ecommerce_data;

-- Total Orders
SELECT COUNT(DISTINCT Order_ID) AS Total_Orders
FROM ecommerce_data;

-- Sales by Category
SELECT
    Category,
    SUM(Sales) AS Total_Sales
FROM ecommerce_data
GROUP BY Category
ORDER BY Total_Sales DESC;

-- Profit by Region
SELECT
    Region,
    SUM(Profit) AS Total_Profit
FROM ecommerce_data
GROUP BY Region
ORDER BY Total_Profit DESC;

-- Top 5 Products
SELECT
    Product_Name,
    SUM(Sales) AS Total_Sales
FROM ecommerce_data
GROUP BY Product_Name
ORDER BY Total_Sales DESC
LIMIT 5;

-- Monthly Sales
SELECT
    YEAR(Order_Date) AS Year,
    MONTH(Order_Date) AS Month,
    SUM(Sales) AS Total_Sales
FROM ecommerce_data
GROUP BY YEAR(Order_Date), MONTH(Order_Date)
ORDER BY Year, Month;