import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

# Load data
df = pd.read_csv('housing_data.csv')

# Fill missing values
median_bedrooms = df['total_bedrooms'].median()
df['total_bedrooms'] = df['total_bedrooms'].fillna(median_bedrooms)

# Create new features
df['rooms_per_house'] = df['total_rooms'] / df['households']
df['bedrooms_ratio'] = df['total_bedrooms'] / df['total_rooms']
df['people_per_house'] = df['population'] / df['households']

# Create income category for stratified split
df['income_cat'] = pd.cut(df['median_income'],
                          bins=[0., 1.5, 3.0, 4.5, 6., np.inf],
                          labels=[1, 2, 3, 4, 5])

# Stratified split
split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_index, test_index in split.split(df, df['income_cat']):
    strat_train_set = df.loc[train_index]
    strat_test_set = df.loc[test_index]

# Remove income_cat
for set_ in (strat_train_set, strat_test_set):
    set_.drop('income_cat', axis=1, inplace=True)

# Separate X and y
X_train = strat_train_set.drop('median_house_value', axis=1)
y_train = strat_train_set['median_house_value'].copy()

print("=" * 60)
print("PREPROCESSING PIPELINE TEST")
print("=" * 60)
print(f"\nTraining set size: {len(strat_train_set)}")
print(f"Test set size: {len(strat_test_set)}")
print(f"\nX_train shape: {X_train.shape}")
print(f"y_train shape: {y_train.shape}")

# Create pipelines
num_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('std_scaler', StandardScaler())
])

cat_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder())
])

# Identify columns
num_attribs = X_train.select_dtypes(include=[np.number]).columns.tolist()
cat_attribs = X_train.select_dtypes(include=['object']).columns.tolist()

print(f"\nNumerical columns ({len(num_attribs)}): {num_attribs}")
print(f"Categorical columns ({len(cat_attribs)}): {cat_attribs}")

# Create ColumnTransformer
preprocessing = ColumnTransformer([
    ('num', num_pipeline, num_attribs),
    ('cat', cat_pipeline, cat_attribs)
])

# Fit and transform
X_train_prepared = preprocessing.fit_transform(X_train)

print("\n" + "=" * 60)
print("TRANSFORMATION RESULTS")
print("=" * 60)
print(f"\nOriginal X_train shape: {X_train.shape}")
print(f"Transformed X_train_prepared shape: {X_train_prepared.shape}")
print(f"X_train_prepared type: {type(X_train_prepared)}")

# Calculate number of features
num_features = len(num_attribs)
cat_features = len(preprocessing.named_transformers_['cat'].named_steps['onehot'].get_feature_names_out())
total_features = num_features + cat_features

print(f"\nFeature breakdown:")
print(f"  - Numerical features: {num_features}")
print(f"  - Categorical features (after OneHot): {cat_features}")
print(f"  - Total features: {total_features}")

print("\n" + "=" * 60)
print("SUCCESS! Pipeline is working correctly.")
print("=" * 60)
