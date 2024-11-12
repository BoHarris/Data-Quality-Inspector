import pandas as pd
import numpy as np


def drop_missing_rows(df):
    """Drop reows with any missing values"""
    return df.dropna()


def fill_missing_with_mean(df, column):
    """Fill missing values in a specific field column with the mean of that column"""
    mean_value = df[column].mean()
    df.fillna({column: mean_value}, inplace=True)
    return df


def analyze_missing_mattern(df):
    """Analyze the pattern of missing data"""
    # Code to determine the pattern of the missing data
    missing_data_summary = df.isnull().sum()
    return missing_data_summary
