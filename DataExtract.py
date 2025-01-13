import zipfile
import pandas as pd
import mysql.connector


zip_ref = zipfile.ZipFile("orders.csv.zip") # To Unzip the zip file
zip_ref.extractall()
zip_ref.close

data = pd.read_csv("C:/Users/Vinoth/DBConnect/orders.csv") # Reading CSV file and storing to data varaiable
#print(data)

df = pd.DataFrame(data)
#print(df)
df.columns= df.columns.str.lower()

#print(df)
#df1 = df.dtypes
#print(df1)

df.columns = df.columns.str.replace(" ","_")   # Formatting the column name with "_"

df['discount'] = df['list_price'] * df['discount_percent'] *.01  # inserting 3 new columns here

df['sale_price'] = df['list_price'] - df['discount']

df['profit'] = df['sale_price']- df['cost_price']

#print(df.columns)
##print(df)

df_order1= df.iloc[:,:10]   # To select all rows and cols till 10th index
df_order2 = df.iloc[:, [0] + list(range(10,19))]  # To select all rows and required cols by its indexes.
##df_order2['order_id']= df_order1['order_id']

print(df_order1) 
print(df_order2)

conn = mysql.connector.connect(
    host = "localhost",
    user ="root",
    password ="123@root",
    database = "retail_orders"
)
if conn.is_connected():
    print("Connection success")

cursor = conn.cursor()

#cursor.execute("select * from retail_orders.df1_order;")
#cursor.execute("select * from retail_orders.df2_order;")

"""for i, row in df_order1.iterrows():
    cursor.execute("INSERT INTO df1_order (order_id, order_date, ship_mode,segment,country,city,state,postal_code,region,category)"
    " VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(row['order_id'], row['order_date'], row['ship_mode'],row['segment'],row['country'],row['city'],row['state'],row['postal_code'],
     row['region'],row['category']))

conn.commit()

for df2, row in df_order2.iterrows():
    cursor.execute("INSERT INTO df2_order (order_id,sub_category, product_id,cost_price,list_price,quantity,discount_percent,discount,sale_price,profit)"
    " VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(row['order_id'], row['sub_category'], row['product_id'],row['cost_price'],row['list_price'],row['quantity'],row['discount_percent'],row['discount'],
     row['sale_price'],row['profit']))

conn.commit()

if(conn._execute_query):
    print("Inserted")
conn.close()"""

