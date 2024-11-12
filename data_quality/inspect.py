def check_missing_values(data):
    """Check for missing values in the dataset and print the result"""
    missing = data.isnull().sum()
    print("Missing values per column:")
    print(missing)
    return missing
