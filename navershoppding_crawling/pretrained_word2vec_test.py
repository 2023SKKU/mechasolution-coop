import pandas as pd

df = pd.read_csv('ns_reviewss2.csv')

df = df[df['product_category'] == '역류방지쿠션']
print(len(df.index))
df_seje = df[df['product_category'] == '역류방지쿠션']
print(df_seje['productName'].head(10))
p_li = df_seje.groupby('productName').count().index.to_list()
print(p_li)