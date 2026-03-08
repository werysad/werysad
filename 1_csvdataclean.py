import pandas as pd
#add csv here
df = pd.read_csv('laptopData.csv')
print(df.head())
df['Company'] = df['Company'].str.strip().str.title()
df['Ram'] = pd.to_numeric(df['Ram'].str.replace('GB',''), errors='coerce')
df['Inches'] = pd.to_numeric(df['Inches'], errors='coerce')
df['Weight'] = pd.to_numeric(df['Weight'].str.replace('kg',''), errors='coerce')
df['Price'] = pd.to_numeric(df['Price'].str.replace(r'[^0-9.]','', regex=True), errors='coerce')

# # Convert join column to date
# df['join'] = pd.to_datetime(df['join'], errors='coerce')
# # Standardize department names
# df['dept'] = df['dept'].replace({'HR':'Human Resources'})
# # Convert active column to boolean
# df['active'] = df['active'].replace({'Yes':True,'Y':True,'no':False})

df.to_csv('laptopData_cleaned.csv', index=False)
print(df.head())

