import pandas as pd


def check_completeness(df):
    """Checks for missing values"""
    missing_values = df.isnull().sum()
    print("Completeness check - Missing values per column:\n", missing_values)


def check_uniqueness(df):
    """Checks for duplicate rows in the dataset."""
    duplicates = df.duplicated().sum()
    print(f"Uniqueness Check - Number of duplicate rows: {duplicates}")


def check_validity(df, column, min_value=None, max_value=None):
    """Checks for invalid entries in a specific column based on min/max values"""
    if column in df.columns:
        invalid_entries = df[(df[column] < min_value) | (df[column] > max_value)]
        print(f"Validity Check - Invalid Entries in '{column}': \n{invalid_entries}")
    else:
        print(f"Column '{column}' not found in the dataset")
