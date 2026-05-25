import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Đọc toàn bộ dataset (chúng ta đã giả lập đọc 10 dòng ở đoạn hội thoại trước,
# giờ chạy logic đó trên TOÀN BỘ dữ liệu)
df = pd.read_csv('MDS301/Learning/House/housing_data.csv')

# 1. Clean data: Xử lý giá trị thiếu ở cột total_bedrooms bằng median trên toàn bộ data
median_bedrooms = df['total_bedrooms'].median()
df['total_bedrooms'] = df['total_bedrooms'].fillna(median_bedrooms)
print("Missing values after clean (ALL rows):\n", df.isnull().sum())

# 2. Scatter plot: median_income vs median_house_value để tìm outliers
plt.figure(figsize=(10, 6))
sns.scatterplot(x='median_income', y='median_house_value', data=df, alpha=0.3)
plt.title('Scatter plot: Median Income vs Median House Value (ALL rows)')
plt.savefig('MDS301/Learning/House/scatter_plot_all.png')
print("\nSaved scatter plot to MDS301/Learning/House/scatter_plot_all.png")

# 3. Mối tương quan giữa các features
correlation_matrix = df.select_dtypes(include=[np.number]).corr()
print("\nCorrelation matrix (ALL rows):")
print(correlation_matrix)
