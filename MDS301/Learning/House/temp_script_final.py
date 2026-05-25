import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import scatter_matrix

# Read Data
df = pd.read_csv('MDS301/Learning/House/housing_data.csv')
median_bedrooms_all = df['total_bedrooms'].median()
df['total_bedrooms'] = df['total_bedrooms'].fillna(median_bedrooms_all)

# 1. Scatter plot latitude vs longitude
plt.figure(figsize=(10, 7))
scatter = plt.scatter(x=df['longitude'], y=df['latitude'], 
            alpha=0.4, 
            s=df['population']/100, label='population', 
            c=df['median_house_value'], cmap=plt.get_cmap('jet'))
plt.title("California Housing Prices: Location, Population, and Value")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.colorbar(scatter, label='Median House Value')
plt.legend()
plt.savefig('MDS301/Learning/House/lat_lon_scatter.png')

# 2. Correlation matrix for median_house_value
corr_matrix = df.corr(numeric_only=True)
corr_with_target = corr_matrix['median_house_value'].sort_values(ascending=False)
print("Correlation truoc khi them feature:\n", corr_with_target)

# 3. Create 3 new features
df['rooms_per_house'] = df['total_rooms'] / df['households']
df['bedrooms_ratio'] = df['total_bedrooms'] / df['total_rooms']
df['people_per_house'] = df['population'] / df['households']

# 4. Recalculate correlation
new_corr_matrix = df.corr(numeric_only=True)
new_corr_with_target = new_corr_matrix['median_house_value'].sort_values(ascending=False)
print("\nCorrelation sau khi them feature:\n", new_corr_with_target)

# 5. Scatter matrix top 4
top_4_attributes = new_corr_with_target.abs().sort_values(ascending=False).head(4).index.tolist()
print("\nTop 4 features to plot:", top_4_attributes)

scatter_matrix(df[top_4_attributes], figsize=(12, 8))
plt.savefig('MDS301/Learning/House/scatter_matrix_top4.png')
