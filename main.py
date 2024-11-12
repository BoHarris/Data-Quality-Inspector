import pandas as pd
from sklearn.impute import SimpleImputer, KNNImputer
from data_quality.data_quality import (
    check_completeness,
    check_uniqueness,
    check_validity,
)

from data_quality.handle_missing_data import (
    drop_missing_rows,
    fill_missing_with_mean,
    analyze_missing_mattern,
)


def main():
    # load the dataset
    df = pd.read_csv("data/dataset_missing.csv")

    # Data quality check
    print("Running Data Quality Checks...")

    # Check Completeness
    check_completeness(df)

    # Check Uniqueness
    check_uniqueness(df)

    # Check Validity
    check_validity(df, column="Age", min_value=0, max_value=120)
    print("data Quality Checks completed.\n")

    # Handle missing data
    df = drop_missing_rows(df)
    fill_missing_with_mean(df, "Age")
    missing_summary = analyze_missing_mattern(df)
    print(missing_summary)

    # Proceed with further data processing or model training
    # (e.g., feature engineering, model training, evaluation, etc)


if __name__ == "__main__":
    main()
