import pandas as pd

# Load dataset
data = pd.read_csv("dataset.csv")

# Display first 5 rows
print("First 5 rows:")
print(data.head())

# Display dataset information
print("\nDataset shape:")
print(data.shape)

# Display career categories
print("\nCareer categories:")
print(data["career"].value_counts())

# Check missing values
print("\nMissing values:")
print(data.isnull().sum())