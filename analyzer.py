import pandas as pd


# =====================================================
# DATASET SUMMARY
# =====================================================

def dataset_summary(df):

    print("\n" + "=" * 60)
    print("                 DATASET SUMMARY")
    print("=" * 60)

    print(f"Rows             : {df.shape[0]}")
    print(f"Columns          : {df.shape[1]}")
    print(f"Memory Usage     : {df.memory_usage(deep=True).sum()/1024:.2f} KB")

    print("\nColumn Names")

    for i, column in enumerate(df.columns, start=1):
        print(f"{i}. {column}")

    print("\nData Types")
    print(df.dtypes)

    numeric_columns = list(df.select_dtypes(include="number").columns)
    text_columns = list(df.select_dtypes(include="object").columns)

    print("\nNumeric Columns :", numeric_columns)
    print("Text Columns    :", text_columns)

    return {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "numeric_columns": numeric_columns,
        "text_columns": text_columns
    }


# =====================================================
# MISSING VALUES
# =====================================================

def check_missing_values(df):

    print("\n" + "=" * 60)
    print("             MISSING VALUE ANALYSIS")
    print("=" * 60)

    missing = df.isnull().sum()

    result = []

    print(f"\n{'Column':<25}{'Missing':<15}{'Percentage'}")
    print("-" * 60)

    for column in df.columns:

        count = missing[column]

        percentage = (count / len(df)) * 100

        print(f"{column:<25}{count:<15}{percentage:.2f}%")

        result.append({
            "column": column,
            "missing": int(count),
            "percentage": round(percentage, 2)
        })

    return result


# =====================================================
# DUPLICATES
# =====================================================

def check_duplicates(df):

    print("\n" + "=" * 60)
    print("              DUPLICATE ANALYSIS")
    print("=" * 60)

    duplicate_rows = df.duplicated().sum()

    print(f"\nDuplicate Rows : {duplicate_rows}")

    return duplicate_rows


# =====================================================
# EMPTY COLUMNS
# =====================================================

def check_empty_columns(df):

    print("\n" + "=" * 60)
    print("            EMPTY COLUMN ANALYSIS")
    print("=" * 60)

    empty_columns = []

    for column in df.columns:

        if df[column].isnull().all():

            empty_columns.append(column)

    if len(empty_columns) == 0:

        print("\nNo Empty Columns Found.")

    else:

        print("\nEmpty Columns")

        for column in empty_columns:

            print(column)

    return empty_columns


# =====================================================
# COLUMN STATISTICS
# =====================================================

def column_statistics(df):

    print("\n" + "=" * 60)
    print("             COLUMN STATISTICS")
    print("=" * 60)

    numeric_columns = df.select_dtypes(include="number").columns

    statistics = {}

    for column in numeric_columns:

        statistics[column] = {

            "minimum": df[column].min(),

            "maximum": df[column].max(),

            "mean": round(df[column].mean(), 2),

            "median": df[column].median(),

            "missing": int(df[column].isnull().sum())

        }

        print("\n" + "-" * 50)

        print(f"Column  : {column}")

        print(f"Minimum : {statistics[column]['minimum']}")

        print(f"Maximum : {statistics[column]['maximum']}")

        print(f"Mean    : {statistics[column]['mean']}")

        print(f"Median  : {statistics[column]['median']}")

        print(f"Missing : {statistics[column]['missing']}")

    return statistics


# =====================================================
# OUTLIER DETECTION
# =====================================================

def detect_outliers(df):

    print("\n" + "=" * 60)
    print("              OUTLIER ANALYSIS")
    print("=" * 60)

    numeric_columns = df.select_dtypes(include="number").columns

    outlier_summary = {}

    for column in numeric_columns:

        Q1 = df[column].quantile(0.25)

        Q3 = df[column].quantile(0.75)

        IQR = Q3 - Q1

        lower = Q1 - 1.5 * IQR

        upper = Q3 + 1.5 * IQR

        outliers = df[(df[column] < lower) | (df[column] > upper)]

        outlier_summary[column] = len(outliers)

        print(f"\n{column:<20} : {len(outliers)}")

    return outlier_summary


# =====================================================
# DATA QUALITY SCORE
# =====================================================

def calculate_quality_score(df):

    print("\n" + "=" * 60)
    print("             DATA QUALITY SCORE")
    print("=" * 60)

    total_cells = df.shape[0] * df.shape[1]

    missing = df.isnull().sum().sum()

    duplicates = df.duplicated().sum()

    empty_columns = len(df.columns[df.isnull().all()])

    missing_score = ((total_cells - missing) / total_cells) * 100

    duplicate_score = ((len(df) - duplicates) / len(df)) * 100

    empty_column_score = ((df.shape[1] - empty_columns) / df.shape[1]) * 100

    overall_score = round(
        (missing_score + duplicate_score + empty_column_score) / 3,
        2
    )

    print(f"Completeness Score : {missing_score:.2f}")

    print(f"Uniqueness Score   : {duplicate_score:.2f}")

    print(f"Structure Score    : {empty_column_score:.2f}")

    print(f"\nOverall Score      : {overall_score}/100")

    if overall_score >= 90:
        print("Dataset Status     : Excellent ✅")

    elif overall_score >= 75:
        print("Dataset Status     : Good 🟢")

    elif overall_score >= 50:
        print("Dataset Status     : Average 🟡")

    else:
        print("Dataset Status     : Poor 🔴")

    return overall_score