import os
import pandas as pd
# Analyzer Functions
from analyzer import (
    dataset_summary,
    check_missing_values,
    check_duplicates,
    check_empty_columns,
    column_statistics,
    detect_outliers,
    calculate_quality_score
)

# Visualization Functions
from visualization import (
    missing_value_chart,
    numeric_histograms,
    numeric_boxplots
)

# PDF Report
from report import generate_report

# Cleaner
from cleaner import clean_dataset

# Logger
from logger import log
from excel_report import generate_excel_report
from dashboard import generate_dashboard



# =====================================================
# MENU FUNCTION
# =====================================================

def menu():

    print("\n" + "=" * 60)
    print("               MAIN MENU")
    print("=" * 60)
    print("1. Dataset Summary")
    print("2. Missing Value Analysis")
    print("3. Duplicate Analysis")
    print("4. Column Statistics")
    print("5. Outlier Detection")
    print("6. Data Quality Score")
    print("7. Generate Charts")
    print("8. Generate PDF Report")
    print("9. Clean Dataset")
    print("10. Run Complete Analysis")
    print("11. Exit")


# =====================================================
# APPLICATION START
# =====================================================

print("=" * 60)
print("      UNIVERSAL CSV DATA QUALITY ANALYZER")
print("=" * 60)

log("Application Started")


# =====================================================
# LOAD DATASET
# =====================================================

folder = "datasets"

files = [f for f in os.listdir(folder) if f.endswith(".csv")]

if len(files) == 0:
    print("\n❌ No CSV files found in the datasets folder.")
    exit()

print("\nAvailable Datasets:\n")

for i, file in enumerate(files, start=1):
    print(f"{i}. {file}")

while True:

    try:

        dataset_choice = int(input("\nSelect Dataset Number: "))

        if 1 <= dataset_choice <= len(files):
            break

        else:
            print("❌ Invalid Choice. Try Again.")

    except ValueError:

        print("❌ Please enter a valid number.")

file_path = os.path.join(folder, files[dataset_choice - 1])

try:

    df = pd.read_csv(file_path)

    print("\n✅ Dataset Loaded Successfully!")

    log(f"Dataset Loaded: {files[dataset_choice - 1]}")

except Exception as e:

    print("\n❌ Error Loading Dataset")
    print(e)

    log(f"Dataset Loading Failed: {e}")

    exit()


# =====================================================
# MAIN MENU LOOP
# =====================================================

while True:

    menu()

    choice = input("\nEnter Choice : ")

    if choice == "1":

        dataset_summary(df)

    elif choice == "2":

        check_missing_values(df)

    elif choice == "3":

        check_duplicates(df)

    elif choice == "4":

        column_statistics(df)

    elif choice == "5":

        detect_outliers(df)

    elif choice == "6":

        score = calculate_quality_score(df)

    elif choice == "7":

        missing_value_chart(df)
        numeric_histograms(df)
        numeric_boxplots(df)

        print("\n✅ Charts Generated Successfully")

    elif choice == "8":
        try:
            score = calculate_quality_score(df)
            # Generate Charts First
            missing_value_chart(df)
            numeric_histograms(df)
            numeric_boxplots(df)
            generate_report( df, score, os.path.basename(file_path))
            generate_excel_report(df,score,os.path.basename(file_path))
            generate_dashboard(df, score, os.path.basename(file_path))
            print("✅ PDF, Excel & Dashboard Generated Successfully!")
            log("PDF Report Generated")
            log("Excel Report Generated")
            print("\n✅ PDF & excel Reports are Generated Successfully")
        except Exception as e:
            print("\nError GENERATING PDF")
            print(e)
    
    

    elif choice == "9":

        clean_dataset(df)

        print("\n✅ Clean Dataset Generated Successfully")

    elif choice == "10":

        dataset_summary(df)

        check_missing_values(df)

        check_duplicates(df)

        check_empty_columns(df)

        column_statistics(df)

        detect_outliers(df)

        score = calculate_quality_score(df)

        missing_value_chart(df)

        numeric_histograms(df)

        numeric_boxplots(df)

        generate_report(df,score,os.path.basename(file_path))
        generate_excel_report(df,score,os.path.basename(file_path))

        clean_dataset(df)

        print("\n🎉 Complete Analysis Finished Successfully!")

    elif choice == "11":

        print("\n👋 Thank You For Using Universal CSV Data Quality Analyzer!")

        log("Application Closed")

        break

    else:

        print("\n❌ Invalid Choice. Please Try Again.")