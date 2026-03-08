import pandas as pd

# Create unclean dataset
data = [
    {"id":1,"name":" akk ","age":"25","join":"2020-01-15","salary":"$3,500","dept":"HR","active":"Yes"},
    {"id":2,"name":"saum ","age":"thirty","join":"15/02/2019","salary":"3500","dept":"Human Resources","active":"Y"},
    {"id":3,"name":"joe","age":"","join":"2018/03/01","salary":"N/A","dept":"R&D","active":"no"},
]

df = pd.DataFrame(data)

# Clean text column
df['name'] = df['name'].str.strip().str.title()

# Convert age column to numeric
df['age'] = pd.to_numeric(df['age'], errors='coerce').fillna(30)

# Clean salary column
df['salary'] = df['salary'].str.replace('$','').str.replace(',','')
df['salary'] = pd.to_numeric(df['salary'], errors='coerce').fillna(0)

# Convert join column to date
df['join'] = pd.to_datetime(df['join'], errors='coerce')

# Standardize department names
df['dept'] = df['dept'].replace({'HR':'Human Resources'})

# Convert active column to boolean
df['active'] = df['active'].replace({'Yes':True,'Y':True,'no':False})

# Remove duplicate rows
df = df.drop_duplicates()

print(df)

