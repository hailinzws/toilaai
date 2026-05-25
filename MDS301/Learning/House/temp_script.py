import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Read first 10 rows
df = pd.read_csv('MDS301/Learning/House/housing_data.csv', nrows=10)

# Clean data: fillna
median_bedrooms = df['total_bedrooms'].median()
df['total_bedrooms'] = df['total_bedrooms'].fillna(median_bedrooms)
print("Missing values after clean:\n", df.isnull().sum())

# Scatter plot
plt.figure(figsize=(8, 5))
sns.scatterplot(x='median_income', y='median_house_value', data=df)
plt.title('Scatter plot: Median Income vs Median House Value (First 10 rows)')
plt.savefig('MDS301/Learning/House/scatter_plot.png')
print("\nSaved scatter plot to MDS301/Learning/House/scatter_plot.png")

# Correlation
correlation_matrix = df.select_dtypes(include=[np.number]).corr()
print("\nCorrelation matrix:")
print(correlation_matrix)
