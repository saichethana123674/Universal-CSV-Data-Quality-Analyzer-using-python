import os
import matplotlib.pyplot as plt


# Create charts folder automatically
os.makedirs("charts", exist_ok=True)


# =====================================================
# Missing Value Bar Chart
# =====================================================

def missing_value_chart(df):

    missing = df.isnull().sum()

    plt.figure(figsize=(10,5))

    plt.bar(missing.index, missing.values)

    plt.title("Missing Values")

    plt.xlabel("Columns")

    plt.ylabel("Missing Count")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig("charts/missing_values.png")

    plt.close()

    print("✓ Missing Value Chart Generated")


# =====================================================
# Histogram for ALL Numeric Columns
# =====================================================

def numeric_histograms(df):

    numeric_columns = df.select_dtypes(include="number").columns

    if len(numeric_columns)==0:
        return

    for column in numeric_columns:

        plt.figure(figsize=(7,4))

        plt.hist(df[column].dropna(), bins=20)

        plt.title(f"{column} Distribution")

        plt.xlabel(column)

        plt.ylabel("Frequency")

        plt.tight_layout()

        filename = f"charts/{column}_histogram.png"

        plt.savefig(filename)

        plt.close()

        print(f"✓ Histogram Created : {column}")


# =====================================================
# Box Plot for ALL Numeric Columns
# =====================================================

def numeric_boxplots(df):

    numeric_columns = df.select_dtypes(include="number").columns

    if len(numeric_columns)==0:
        return

    for column in numeric_columns:

        plt.figure(figsize=(5,6))

        plt.boxplot(df[column].dropna())

        plt.title(f"{column} Box Plot")

        plt.ylabel(column)

        plt.tight_layout()

        filename = f"charts/{column}_boxplot.png"

        plt.savefig(filename)

        plt.close()

        print(f"✓ Box Plot Created : {column}")