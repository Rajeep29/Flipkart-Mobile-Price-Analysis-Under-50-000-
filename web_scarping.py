import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

Product_name=[]
Price=[]
Description=[]
Reviews=[]

for i in range(2,12):
    url="https://www.flipkart.com/search?q=mobiles+under+50000&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_1_3_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_1_3_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=mobiles+under+50000&requestId=e6633f17-9a2d-4be6-9efa-d86238c8287c&as-searchtext=mob&page="+str(i)
    response=requests.get(url,headers=headers)
    soup=BeautifulSoup(response.content,"html.parser")
    
    products = soup.find_all("div", class_="nZIRY7")

    for product in products:
       product_name=product.find("div",class_="RG5Slk")
       Product_name.append(product_name.text.strip() if product_name else None)
       
       price = product.find("div", class_="hZ3P6w DeU9vF")
       Price.append(price.text.strip() if price else None)
       
       desc=product.find("ul",class_="HwRTzP")
       Description.append(desc.text.strip() if desc else None)
       
       reviews=product.find("span",class_="CjyrHS")
       Reviews.append(reviews.text.strip() if reviews else None)

df = pd.DataFrame({
    "product_name": Product_name,
    "price": Price,
    "description": Description,
    "reviews": Reviews
})
# print(df)
       
   
print(df.drop_duplicates(inplace=True))
df["price"]=df["price"].str.replace("₹","").str.replace(",","").astype(int)
# print(df["price"])
df["reviews"]=df["reviews"].astype(float)
# print(df["reviews"])

# print(df.isnull().sum())

df["reviews"]=df["reviews"].fillna(df["reviews"].median())
# print(df["reviews"].unique())

df["brand"]=df["product_name"].str.split().str[0]
# print(df["brand"])

#                         Top Brands by Count
# print(df["brand"].value_counts().head(10))



#                         Average Price by Brand
# print(df.groupby("brand")["price"].mean().sort_values())



#                Best Phones Under ₹50K (High Rating + Low Price)
# print(df.sort_values(["reviews","price"],ascending=[False,True]).head(10))


# Visualisation

plt.figure(figsize=(10,5))
sns.barplot(x=df['brand'].value_counts().head(10).index,
            y=df['brand'].value_counts().head(10).values)
plt.xticks(rotation=45)
plt.title("Top 10 Mobile Brands on Flipkart")
plt.show()

df.to_csv("C:/Users/rahul/OneDrive/Desktop/data py/mobiles.csv",index=False)  
