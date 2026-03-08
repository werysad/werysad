from sklearn.datasets import load_iris
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = load_iris()

df = pd.DataFrame(data.data, columns=data.feature_names)

print("Original DataFrame:\n", df)

# Encoding
df_encoded = pd.get_dummies(df, drop_first=True)

print("\nEncoded DataFrame:\n", df_encoded)

# Correlation matrix
corr_matrix = df_encoded.corr().abs()

print("\nCorrelation Matrix:\n", corr_matrix)

# Heatmap visualization
plt.figure(figsize=(6,4))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# Upper triangle to avoid self correlation
upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))

# Find highly correlated columns
to_drop = [column for column in upper.columns if any(upper[column] > 0.9)]

print("\nColumns to drop due to high correlation:", to_drop)

# Remove highly correlated columns
df_reduced = df_encoded.drop(columns=to_drop)

print("\nReduced DataFrame:\n", df_reduced.head())