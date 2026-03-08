import pandas as pd
import numpy as np

data = {
    'A':[1,2,3,4,5],
    'B':[2,4,6,8,10],
    'C':[5,3,6,2,1],
    'D':[10,20,30,40,50]
}
df=pd.DataFrame(data)
print("Original Data:\n",df)
corr_matrix = df.corr().abs()
print("\nCorrelation Matrix:\n",corr_matrix)

upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape),k=1).astype(bool))
to_drop = [column for column in upper.columns if any(upper[column]>0.9)]
print('Dropping the column:\n',to_drop)

df_reduced = df.drop(columns = to_drop)
print("reduced columns:\n",df_reduced)


df_reduced.to_csv('reduced_data.csv',index=False)
df_new = pd.read_csv("reduced_data.csv")
print('\n Reduced Data:\n', df_new)
