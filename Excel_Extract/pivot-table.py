import pandas as pd

df = pd.read_excel(r"C:\Users\Jain\Downloads\supermarket_sales.xlsx")# file path 
print(df)

#[] one column select and [[]] double more columns select
df = df[['Gender','Product line','Total']] 


pivot_table = df.pivot_table(index = 'Gender', columns = 'Product line',values='Total',
               aggfunc='sum').round(0)
pivot_table.to_excel('pivot_table.xlsx','Report',startrow=4)