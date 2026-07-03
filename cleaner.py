import os

def clean_dataset(df):

    os.makedirs("reports", exist_ok=True)

    cleaned = df.copy()

    cleaned = cleaned.drop_duplicates()

    cleaned = cleaned.fillna("Unknown")

    cleaned.to_csv(
        "reports/cleaned_dataset.csv",
        index=False
    )

    print("✅ Clean Dataset Saved")

    return cleaned