import pandas as pd
import numpy as np


data={
    'Age':[25,32,47,51,62],
    'salary':[50000,60000,80000,90000,120000],
    'Dept':['HR','IT','IT','HR','Finance'],
    'Experience':[2,5,20,22,30],
    'city':['NY','LA','LA','NY','Chicago']
}


df=pd.DataFrame(data)


print("Original DataFrame:\n",df)


# Encoding categorical variables
df_encoded=pd.get_dummies(df, drop_first=True)


print("\nEncoded DataFrame:\n",df_encoded)


# Correlation matrix
corr_matrix=df_encoded.corr().abs()


print("\nCorrelation Matrix:\n",corr_matrix)


# Upper triangle to avoid self correlation
upper=corr_matrix.where(np.triu(np.ones(corr_matrix.shape),k=1).astype(bool))


# Find highly correlated columns
to_drop=[column for column in upper.columns if any(upper[column]>0.9)]


print("\nColumns to drop due to high correlation:",to_drop)


# Drop them
df_reduced=df_encoded.drop(columns=to_drop)


print("\nReduced DataFrame:\n",df_reduced)