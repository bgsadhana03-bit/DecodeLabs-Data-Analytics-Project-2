# DecodeLabs Data Analytics Project 2: Exploratory Data Analysis (EDA)

## Project Overview

This project explores an order dataset using Python and exploratory data analysis (EDA). The aim is to understand the dataset's structure, summarize numerical data, identify missing values and potential outliers, and examine product, order-status, and monthly order patterns.

## Dataset

- **Size:** 1,200 rows and 14 columns
- **Date range:** January 1, 2023 – June 30, 2025
- **File:** `Dataset for Data Analytics (2).xlsx`

The dataset includes order IDs, dates, customer IDs, products, quantities, unit prices, shipping addresses, payment methods, order statuses, tracking numbers, items in cart, coupon codes, referral sources, and total prices.

## Tools and Libraries

- Python
- pandas
- matplotlib
- openpyxl

## Analysis Performed

- Inspected dataset dimensions, column names, and data types
- Checked missing values and duplicate rows
- Calculated descriptive statistics, including mean, median, and quartiles
- Summarized order statuses and product frequencies
- Counted orders by month
- Detected potential numerical outliers using the interquartile range (IQR) method
- Exported a CSV summary and generated charts

## Key Findings

- The dataset contains **1,200 rows and 14 columns**.
- There are **no duplicate rows** in the dataset.
- `CouponCode` has **309 missing values**; the other columns have no missing values.
- The average `Quantity` is approximately **2.95**, and its median is **3**.
- The average `TotalPrice` is approximately **1,053.97**, and its median is approximately **823.62**.
- `Cancelled` is the most frequent order status (**250 records**), followed by `Returned` (**247 records**).
- The three most frequent products are **Printer (181)**, **Tablet (179)**, and **Chair (178)**.
- Monthly order counts range from **27 to 53**. The highest count in the displayed monthly summary is **53 in June 2024**.
- The IQR method flagged **8 potential `TotalPrice` outliers** above the upper boundary of **3,330.41**. These records should be investigated rather than automatically removed.

## Generated Outputs

The analysis script generates the following files:

- `eda_summary.csv` — descriptive summary output
- `eda_findings.txt` — key findings in text format
- `order_status.png` — order-status chart
- `top_products.png` — product-frequency chart
- `monthly_trend.png` — monthly order-count chart

## How to Run

1. Make sure Python is installed.
2. Install the required libraries:

   ```bash
   pip install pandas openpyxl matplotlib
   ```

3. Place the Excel dataset and `eda_analysis.py` in the same folder.
4. Open a terminal in that folder and run:

   ```bash
   python eda_analysis.py
   ```

5. Check the generated CSV, text report, and chart images in the project folder.

## Notes and Limitations

- Missing `CouponCode` values have not been assumed to mean that no coupon was used.
- IQR-identified outliers are potential unusual values, not necessarily data errors.
- The findings describe patterns in this dataset and do not, by themselves, explain why those patterns occurred.
- The reported `TotalPrice` values should be checked against the dataset's business rules before making conclusions about unusually high orders.

## Conclusion

This EDA provides an initial overview of order data quality, numerical distributions, product frequencies, order statuses, and monthly order counts. The results can guide further investigation into order outcomes, sales patterns, and unusual transaction values.
