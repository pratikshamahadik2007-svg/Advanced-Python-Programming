import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore

# 1. Load dataset
df = pd.read_csv("customer_churn.csv")

# Display dataset
print(df.head())
print(df.info())

# Select numerical columns
num_cols = df.select_dtypes(include=['number']).columns

# 2. Descriptive Statistics
print("\nDescriptive Statistics:")
print(df[num_cols].describe())

for col in num_cols:
    print("\nColumn:", col)
    print("Mean:", df[col].mean())
    print("Median:", df[col].median())
    print("Mode:", df[col].mode()[0])
    print("Standard Deviation:", df[col].std())
    print("Variance:", df[col].var())
    print("Minimum:", df[col].min())
    print("Maximum:", df[col].max())
    print("Quantiles:", df[col].quantile([0.25, 0.5, 0.75]))

# 3. Data Visualization

# Histogram
df[num_cols].hist(figsize=(10, 8))
plt.show()

# Box Plot
for col in num_cols:
    sns.boxplot(y=df[col])
    plt.title("Box Plot of " + col)
    plt.show()

# Scatter Plot
if len(num_cols) >= 2:
    plt.scatter(df[num_cols[0]], df[num_cols[1]])
    plt.xlabel(num_cols[0])
    plt.ylabel(num_cols[1])
    plt.title("Scatter Plot")
    plt.show()

# Correlation Heatmap
sns.heatmap(df[num_cols].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

# 4. Handling Missing Data

print("\nMissing Values:")
print(df.isnull().sum())

# Fill numerical missing values with mean
df[num_cols] = df[num_cols].fillna(df[num_cols].mean())

# Fill categorical missing values with mode
for col in df.select_dtypes(include=['object']).columns:
    if df[col].isnull().any():
        df[col] = df[col].fillna(df[col].mode()[0])

print("\nAfter Handling Missing Values:")
print(df.isnull().sum())

# 5. Detecting Outliers using Z-score

z_scores = df[num_cols].apply(zscore)

print("\nOutliers:")
print(df[(z_scores.abs() > 3).any(axis=1)])

# 6. Removing Outliers
df = df[(z_scores.abs() <= 3).all(axis=1)]

print("\nDataset After Removing Outliers:")
print(df)

# 7. Verify Cleaned Dataset
print("\nRemaining Missing Values:")
print(df.isnull().sum())

# 8. Save Cleaned Dataset
df.to_csv("cleaned_customer_churn.csv", index=False)

print("\nCleaned Dataset Saved Successfully!")