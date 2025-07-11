import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('organizations-100.csv')

# Fill missing values
for col in df.columns:
    if df[col].isnull().sum() > 0:
        if df[col].dtype == 'object':
            df[col].fillna(df[col].mode()[0], inplace=True)
        else:
            df[col].fillna(df[col].median(), inplace=True)

# Drop unwanted columns
df.drop(columns=['Name', 'Description', 'Internal ID', 'EAN'], errors='ignore', inplace=True)

# One-hot encode categorical columns
df = pd.get_dummies(df, drop_first=True)

# Standardize numerical columns
num_cols = df.select_dtypes(include=['int64', 'float64']).columns
df[num_cols] = (df[num_cols] - df[num_cols].mean()) / df[num_cols].std()

# Correlation heatmap
top_corr = df[df.var().sort_values(ascending=False).head(10).index].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(top_corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
