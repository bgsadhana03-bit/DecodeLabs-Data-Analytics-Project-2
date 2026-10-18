
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

file_path = Path("Dataset for Data Analytics (2).xlsx")
df = pd.read_excel(file_path)

print("\n--- DATASET OVERVIEW ---")
print("Rows and columns:", df.shape)
print("\nColumn names:")
print(df.columns.tolist())

print("\n--- FIRST 5 ROWS ---")
print(df.head())

print("\n--- DATA TYPES ---")
print(df.dtypes)

print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())

print("\n--- NUMERICAL SUMMARY ---")
print(df.describe())

print("\n--- MEAN ---")
print(df.select_dtypes(include="number").mean())

print("\n--- MEDIAN ---")
print(df.select_dtypes(include="number").median())

print("\n--- NON-MISSING VALUE COUNTS ---")
print(df.count())

if "OrderStatus" in df.columns:
    print("\n--- ORDER STATUS COUNTS ---")
    print(df["OrderStatus"].value_counts(dropna=False))

    df["OrderStatus"].value_counts().plot(
        kind="bar", title="Orders by Status"
    )
    plt.xlabel("Order Status")
    plt.ylabel("Number of Orders")
    plt.tight_layout()
    plt.savefig("order_status.png")
    plt.close()

if "Product" in df.columns:
    print("\n--- TOP PRODUCTS ---")
    print(df["Product"].value_counts().head(10))

    df["Product"].value_counts().head(10).plot(
        kind="bar", title="Top 10 Products"
    )
    plt.xlabel("Product")
    plt.ylabel("Number of Orders")
    plt.tight_layout()
    plt.savefig("top_products.png")
    plt.close()

if "Date" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    valid_dates = df.dropna(subset=["Date"])

    if not valid_dates.empty:
        monthly_orders = (
            valid_dates.set_index("Date")
            .resample("ME")
            .size()
        )

        print("\n--- MONTHLY ORDER COUNTS ---")
        print(monthly_orders)

        monthly_orders.plot(
            kind="line", marker="o", title="Monthly Order Trend"
        )
        plt.xlabel("Month")
        plt.ylabel("Number of Orders")
        plt.tight_layout()
        plt.savefig("monthly_trend.png")
        plt.close()


# 8. Identify and inspect potential outliers using IQR
print("\n--- POTENTIAL NUMERICAL OUTLIERS ---")

numeric_df = df.select_dtypes(include="number")

for column in numeric_df.columns:
    values = numeric_df[column].dropna()

    if values.empty:
        continue

    q1 = values.quantile(0.25)
    q3 = values.quantile(0.75)
    iqr = q3 - q1

    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr

    mask = (df[column] < lower) | (df[column] > upper)
    outliers = df.loc[mask, ["OrderID", column]]

    print(f"\n{column}: {len(outliers)} potential outliers")
    print(f"Lower boundary: {lower:.2f}")
    print(f"Upper boundary: {upper:.2f}")

    if not outliers.empty:
        print(outliers.to_string(index=False))

numeric_df = df.select_dtypes(include="number")

for column in numeric_df.columns:
    values = numeric_df[column].dropna()

    if values.empty:
        continue

    q1 = values.quantile(0.25)
    q3 = values.quantile(0.75)
    iqr = q3 - q1

    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    outliers = values[(values < lower) | (values > upper)]

    print(
        f"{column}: {len(outliers)} potential outliers "
        f"(lower={lower:.2f}, upper={upper:.2f})"
    )

df.describe(include="all").to_csv("eda_summary.csv")

print("\nEDA analysis completed!")
print("Generated: eda_summary.csv")
print("Charts are saved as PNG files when applicable.")

# 10. Save key observations for the project report

from pathlib import Path

report = []

report.append("DECODELABS PROJECT 2: EDA FINDINGS")
report.append("=" * 40)
report.append(f"Dataset size: {df.shape[0]} rows and {df.shape[1]} columns")
report.append(f"Duplicate rows: {df.duplicated().sum()}")

report.append("\nMissing values:")
for column, count in df.isnull().sum().items():
    if count > 0:
        report.append(f"- {column}: {count} missing values")

report.append("\nNumerical statistics:")
for column in ["Quantity", "UnitPrice", "ItemsInCart", "TotalPrice"]:
    if column in df.columns:
        report.append(
            f"- {column}: mean={df[column].mean():.2f}, "
            f"median={df[column].median():.2f}, "
            f"count={df[column].count()}"
        )

report.append("\nOrder status counts:")
report.extend(
    f"- {status}: {count}"
    for status, count in df["OrderStatus"].value_counts().items()
)

report.append("\nMost frequent products:")
report.extend(
    f"- {product}: {count}"
    for product, count in df["Product"].value_counts().head(3).items()
)

q1 = df["TotalPrice"].quantile(0.25)
q3 = df["TotalPrice"].quantile(0.75)
iqr = q3 - q1
upper = q3 + 1.5 * iqr
outlier_count = (
    (df["TotalPrice"] < q1 - 1.5 * iqr)
    | (df["TotalPrice"] > upper)
).sum()

report.append(
    f"\nPotential TotalPrice outliers: {outlier_count}"
)
report.append(f"IQR upper boundary: {upper:.2f}")
report.append(
    "\nNote: Potential outliers require investigation; "
    "they are not automatically data errors."
)

Path("eda_findings.txt").write_text(
    "\n".join(report), encoding="utf-8"
)

print("\nFindings report saved as eda_findings.txt")

