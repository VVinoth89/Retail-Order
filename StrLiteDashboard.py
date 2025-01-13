import streamlit as st
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.stackplot as slt

st.markdown("""
    <h1 style="font-family: 'Comic Sans MS'; color: blue;, ">Welcome to Guvi Dashboard</h1>
    <h2 style="font-family: 'Times New Roman'; color: Yellow;">Reatil Order Analysis </h2>
    """, unsafe_allow_html=True)

#st.markdown(""" <style>
 #       body { background-color:#ffcccb;  }
  #          </style>
   #         """, unsafe_allow_html=True)

#st.write("Reatil Order Analysis")
SelectedItem = st.selectbox("Select a Query", ["1.Top 10 highest revenue generating products",
                "2.Top 5 cities with the highest profit margins",
                "3.Calculate the total discount given for each category",
                "4.The average sale price per product category",
                "5.Region with the highest average sale price",
                "6.The total profit per category",
                "7.The top 3 segments with the highest quantity of orders",
                "8.Determine the average discount percentage given per region",
                "9.Product category with the highest total profit",
                "10.Calculate the total revenue generated per year",
                "11.Find the Least selling products",
                "12.The product with the highest price",
                "13.Best performing products",
                "14.Region wise best revenue generating products",
                "15.Month and Year wise sales camparision",
                "16.Category Performence metrics",
                "17.Find the Regional Sales analysis by month",
                "18.Calculate the total sales in a year by product" ,
                "19.List the Products with sales more than 20,000 ",
                "20.Revenue from discounted sales"              
                ])

conn = mysql.connector.connect(
    host = "localhost",
    user ="root",
    password ="123@root",
    database = "retail_orders"
)
cursor = conn.cursor()

if (SelectedItem =="1.Top 10 highest revenue generating products"):
    st.write("10 Highest Revenue Generating Products")
    Sqlquery = "Select product_id,sub_category,sale_price from df2_order ORDER BY sale_price DESC LIMIT 10;"
    cursor.execute(Sqlquery)
    Table1 = cursor.fetchall()
    info = pd.DataFrame(Table1, columns=['product_id','Sub_category','Proft_Margin'])
    st.dataframe(info)

    # To Create Bar chart for above query
    df= pd.read_sql_query(Sqlquery,conn) # Reads query and copy to dataframe
    conn.close()

    plt.figure(figsize=(9,5))
    plt.bar(df['sub_category'],df['sale_price'])
    
    # Add title and labels
    plt.title('Highest Revenue Generating Products')
    plt.xlabel('Product')
    plt.ylabel('sale_price')
    st.pyplot(plt)

elif (SelectedItem == "2.Top 5 cities with the highest profit margins"):
    st.write("Top 5 Cities with Highest Profits")
    Sqlquery = ''' SELECT df1_order.order_id , df1_order.city, df2_order.profit FROM df2_order 
                 INNER JOIN df1_order
                 ON df1_order.order_id = df2_order.order_id  
                 ORDER BY df2_order.profit DESC LIMIT 5;'''
    cursor.execute(Sqlquery)
    Table1 = cursor.fetchall()
    info = pd.DataFrame(Table1, columns=['Order ID','City','Proft_Margin'])
    st.dataframe(info)

    df= pd.read_sql_query(Sqlquery,conn) # Reads query and copy to dataframe
    conn.close()

    plt.figure(figsize=(9,5))
    plt.bar(df['city'],df['profit'])
    
    # Add title and labels
    plt.title('Top 5 City Profit')
    plt.xlabel('City')
    plt.ylabel('Profit Margin')
    st.pyplot(plt)
    
elif(SelectedItem == "3.Calculate the total discount given for each category"):
    st.write("Total Discount given for each category")
    Sqlquery = '''SELECT category, SUM(discount) AS total_discount
                  FROM df2_order
                  INNER JOIN  df1_order ON df2_order.order_id = df1_order.order_id group by df1_order.category 
                  ORDER BY total_discount desc'''
    cursor.execute(Sqlquery)
    Table1 = cursor.fetchall()
    info = pd.DataFrame(Table1, columns=['Category','Total Discount'])
    st.dataframe(info)

    df= pd.read_sql_query(Sqlquery,conn) # Reads query and copy to dataframe
    conn.close()

    plt.figure(figsize=(9,5))
    plt.bar(df['category'],df['total_discount'])
    
    # Add title and labels
    plt.title('Toatl Discount for Each Category')
    plt.xlabel('Category')
    plt.ylabel('Discount')
    st.pyplot(plt)

elif(SelectedItem == "4.The average sale price per product category"):
    st.write("Average sale price per product category")
    Sqlquery = '''SELECT category, avg(sale_price) AS Avg_Sale_Price
                  FROM df2_order
                  INNER JOIN  df1_order ON df2_order.order_id = df1_order.order_id group by df1_order.category 
                  order by Avg_Sale_Price desc;  '''
    cursor.execute(Sqlquery)
    Table1 = cursor.fetchall()
    info = pd.DataFrame(Table1, columns=['Category','Average Sale Price'])
    st.dataframe(info)

    df= pd.read_sql_query(Sqlquery,conn) # Reads query and copy to dataframe
    conn.close()

    plt.figure(figsize=(9,5))
    plt.bar(df['category'],df['Avg_Sale_Price'])
    
    # Add title and labels
    plt.title('Average Sale Price for Category')
    plt.xlabel('Category')
    plt.ylabel('Sales Price')
    st.pyplot(plt)

elif(SelectedItem == "5.Region with the highest average sale price"):
    st.write("Region with the highest average sale price")
    Sqlquery ='''SELECT region, avg(sale_price) AS Avg_Sale_Price
                 FROM df2_order
                 INNER JOIN  df1_order ON df2_order.order_id = df1_order.order_id group by df1_order.region 
                 order by Avg_Sale_Price desc;'''  
    cursor.execute(Sqlquery)
    Table1 = cursor.fetchall()
    info = pd.DataFrame(Table1, columns=['Region','Highest Average Sale Price'])
    st.dataframe(info)

    df= pd.read_sql_query(Sqlquery,conn) # Reads query and copy to dataframe
    conn.close()

    plt.figure(figsize=(9,5))
    plt.bar(df['region'],df['Avg_Sale_Price'])
    
    # Add title and labels
    plt.title('Region with Average Sales Price')
    plt.xlabel('Region')
    plt.ylabel('Sales Price')
    st.pyplot(plt)
    
elif(SelectedItem == "6.The total profit per category"):
    st.write("The total profit per category")
    Sqlquery ='''SELECT category, SUM(profit) AS total_profit
                 FROM df2_order
                 INNER JOIN  df1_order ON df2_order.order_id = df1_order.order_id group by df1_order.category 
                 order by total_profit desc;'''
    cursor.execute(Sqlquery)
    Table1 = cursor.fetchall()
    info = pd.DataFrame(Table1, columns=['Category','Total Profit'])
    st.dataframe(info)

    df= pd.read_sql_query(Sqlquery,conn) # Reads query and copy to dataframe
    conn.close()

    plt.figure(figsize=(9,5))
    plt.bar(df['category'],df['total_profit'])
    
    # Add title and labels
    plt.title('Toatl Profit Category')
    plt.xlabel('Category')
    plt.ylabel('Total Profit')
    st.pyplot(plt)

elif(SelectedItem =="7.The top 3 segments with the highest quantity of orders"):
    st.write("Top 3 segments with the highest quantity of orders")
    Sqlquery = '''SELECT segment, SUM(quantity) as Highest_quantity
                  FROM df1_order JOIN df2_order ON df1_order.order_id = df2_order.order_id group by segment
                  ORDER BY Highest_quantity desc;'''
    cursor.execute(Sqlquery)
    Table1 = cursor.fetchall()
    info = pd.DataFrame(Table1, columns=['Segment','High Quantity'])
    st.dataframe(info)

    df= pd.read_sql_query(Sqlquery,conn) # Reads query and copy to dataframe
    conn.close()

    plt.figure(figsize=(9,5))
    #plt.bar(df['segment'],df['Highest_quantity'],width= 0.3,bottom= 0.9)
    plt.scatter(df['segment'],df['Highest_quantity'])
    #plt.stackplot
    
    # Add title and labels
    plt.title('Toatl Profit Category')
    plt.xlabel('Segment')
    plt.ylabel('High Quantity')
    plt.legend(loc= 'upper left')
    st.pyplot(plt)

elif(SelectedItem =="8.Determine the average discount percentage given per region"):
    st.write("Average discount percentage given per region")
    Sqlquery = '''SELECT region, avg(discount_percent) as avg_dics
                  FROM df1_order
                  JOIN df2_order ON df1_order.order_id = df2_order.order_id group by region
                  ORDER BY avg_dics desc ;'''
    cursor.execute(Sqlquery)
    Table1 = cursor.fetchall()
    info = pd.DataFrame(Table1, columns=['Region','Average Dicount Percenr'])
    st.dataframe(info)

    df= pd.read_sql_query(Sqlquery,conn) # Reads query and copy to dataframe
    conn.close()

    plt.figure(figsize=(9,5))
    plt.bar(df['region'],df['avg_dics'],width= 0.3,bottom= 0.9)
    #plt.scatter(df['region'],df['avg_dics'])
    #plt.stackplot
    
    # Add title and labels
    plt.title('Average Discount Per Region')
    plt.xlabel('Region')
    plt.ylabel('Average Discount')
    plt.legend(loc= 'upper left')
    st.pyplot(plt)

elif(SelectedItem == "9.Product category with the highest total profit"):
    st.write("Product category with the highest total profit")
    Sqlquery =''' SELECT category, sum(profit) as total_profit
                  FROM df1_order
                  JOIN df2_order ON df1_order.order_id = df2_order.order_id group by category
                  ORDER BY total_profit desc limit 1 ;'''
    cursor.execute(Sqlquery)
    Table1 = cursor.fetchall()
    info = pd.DataFrame(Table1, columns=['Cetagory','Total Profit'])
    st.dataframe(info)

    df= pd.read_sql_query(Sqlquery,conn) # Reads query and copy to dataframe
    conn.close()

    plt.figure(figsize=(9,5))
    plt.bar(df['category'],df['total_profit'],width= 0.3,bottom= 0.9)
    #plt.scatter(df['region'],df['avg_dics'])
    #plt.stackplot
    
    # Add title and labels
    plt.title('Category with Highest Profit')
    plt.xlabel('Category')
    plt.ylabel('Total Profit')
    st.pyplot(plt)

elif(SelectedItem == "10.Calculate the total revenue generated per year"):
    st.write("Total revenue generated per year")
    Sqlquery = ''' SELECT year(order_date) as Year, sum(sale_price) as total_revenue
                   FROM df1_order
                   JOIN df2_order ON df1_order.order_id = df2_order.order_id group by Year
                   ORDER BY total_revenue desc;'''
    cursor.execute(Sqlquery)
    Table1 = cursor.fetchall()
    info = pd.DataFrame(Table1, columns=['Year','Total Revenue'])
    st.dataframe(info)

    
    df= pd.read_sql_query(Sqlquery,conn) # Reads query and copy to dataframe
    conn.close()

    plt.figure(figsize=(9,5))
    plt.bar(df['Year'],df['total_revenue'],width= 0.4,bottom= 0.9)
        
    # Add title and labels
    plt.title('Total Revenue per Year')
    plt.xlabel('Year')
    plt.ylabel('Total Revenue')
    st.pyplot(plt)

elif(SelectedItem== "11.Find the Least selling products"):
    st.write("The Least selling Products")
    Sqlquery = ''' SELECT sub_category, sum(quantity) as  total_quantity FROM df2_order
                   JOIN df1_order ON df2_order.order_id = df1_order.order_id group by sub_category
                   ORDER BY total_quantity asc limit 5;'''
    cursor.execute(Sqlquery)
    Table1 = cursor.fetchall()
    info = pd.DataFrame(Table1, columns=['Sub-Category','Quantity'])
    st.dataframe(info)

    
    df= pd.read_sql_query(Sqlquery,conn) # Reads query and copy to dataframe
    conn.close()

    plt.figure(figsize=(9,5))
    plt.bar(df['sub_category'],df['total_quantity'],width= 0.4,bottom= 0.9)
        
    # Add title and labels
    plt.title('Least Selling Product')
    plt.xlabel('Sub Category')
    plt.ylabel('Total Quantity')
    st.pyplot(plt)

elif(SelectedItem == "12.The product with the highest price"):
    st.write("The product with highest price")
    Sqlquery = "select sub_category, cost_price from df2_order order by cost_price desc limit 10;"
    cursor.execute(Sqlquery)
    Table1 = cursor.fetchall()
    info = pd.DataFrame(Table1, columns=['Sub-Category','Cost Price'])
    st.dataframe(info)
    
    df= pd.read_sql_query(Sqlquery,conn) # Reads query and copy to dataframe
    conn.close()

    plt.figure(figsize=(9,5))
    plt.bar(df['sub_category'],df['cost_price'],width= 0.4,bottom= 0.9)
        
    # Add title and labels
    plt.title('Least Selling Product')
    plt.xlabel('Sub Category')
    plt.ylabel('Price')
    st.pyplot(plt)

elif(SelectedItem == "13.Best performing products"):
    st.write("Best performing productas")
    Sqlquery = ''' SELECT category, product_id, sum(sale_price) as  total_revenue
                   FROM df2_order
                   JOIN df1_order ON df2_order.order_id = df1_order.order_id group by category,product_id
                   ORDER BY total_revenue desc limit 10;'''
    cursor.execute(Sqlquery)
    Table1 = cursor.fetchall()
    info = pd.DataFrame(Table1, columns=['Category','Prodcut ID', 'Total Revenue'])
    st.dataframe(info)
    
    df= pd.read_sql_query(Sqlquery,conn) # Reads query and copy to dataframe
    conn.close()

    plt.figure(figsize=(9,5))
    plt.bar(df['category'],df['total_revenue'],width= 0.4,bottom= 0.9)
        
    # Add title and labels
    plt.title('Best Performing Product')
    plt.xlabel('Category')
    plt.ylabel('Total Revenue')
    st.pyplot(plt)

elif(SelectedItem == "14.Region wise best revenue generating products"):
    st.write("Region wise best revenu generating products")
    Sqlquery = ''' SELECT region, category, sum(profit) as  total_profit
                   FROM df2_order
                   JOIN df1_order ON df2_order.order_id = df1_order.order_id group by category,region
                   ORDER BY total_profit desc;'''
    cursor.execute(Sqlquery)
    Table1 = cursor.fetchall()
    info = pd.DataFrame(Table1, columns=['Region','Category', 'Total Revenue'])
    st.dataframe(info)
    
    df= pd.read_sql_query(Sqlquery,conn) # Reads query and copy to dataframe
    conn.close()

    plt.figure(figsize=(9,5))
    plt.bar(df['category'],df['total_profit'],width= 0.4,bottom= 0.9)
        
    # Add title and labels
    plt.title('Best Revenue Product')
    plt.xlabel('Category')
    plt.ylabel('Total Revenu')
    st.pyplot(plt)

elif(SelectedItem == "15.Month and Year wise sales camparision"):
    st.write("Year and Month wise Sales comparision")
    Sqlquery = ''' SELECT month(order_date) as Month,
                   year(order_date) as year, sum(sale_price) as  total_sales
                   FROM df2_order
                   JOIN df1_order ON df2_order.order_id = df1_order.order_id group by Month,year
                   ORDER BY month, year desc;'''
    cursor.execute(Sqlquery)
    Table1 = cursor.fetchall()
    info = pd.DataFrame(Table1, columns=['Month','Year', 'Total Sales'])
    st.dataframe(info)

    df= pd.read_sql_query(Sqlquery,conn) # Reads query and copy to dataframe
    conn.close()

    plt.figure(figsize=(9,5))
    plt.bar(df['year'],df['total_sales'],width= 0.4,bottom= 0.9)
        
    # Add title and labels
    plt.title('Best Revenue Product')
    plt.xlabel('Year')
    plt.ylabel('Total Revenu')
    st.pyplot(plt)

elif(SelectedItem == "16.Category Performence metrics"):
    st.write("Category Performence Metrics")
    Sqlquery = ''' SELECT category, sum(quantity)as total_quantity, sum(sale_price) as total_revenue,
               avg(profit) as Avg_profit FROM df2_order
               JOIN df1_order ON df2_order.order_id = df1_order.order_id group by category
               ORDER BY total_revenue desc;'''
    cursor.execute(Sqlquery)
    Table1 = cursor.fetchall()
    info = pd.DataFrame(Table1, columns=['Category','Total Revenue', 'Average Profit'])
    st.dataframe(info)
    
    df= pd.read_sql_query(Sqlquery,conn) # Reads query and copy to dataframe
    conn.close()

    plt.figure(figsize=(9,5))
    plt.bar(df['category'],df['total_revenue'],width= 0.4,bottom= 0.9)
        
    # Add title and labels
    plt.title('Category Performence')
    plt.xlabel('Category')
    plt.ylabel('Total Revenue')
    st.pyplot(plt)

elif(SelectedItem == "17.Find the Regional Sales analysis by month"):
    st.write("Monthly Sales analysis from regions")
    Sqlquery = ''' SELECT month(order_date) AS month, region, sum(sale_price) as total_sales FROM df2_order
                   JOIN df1_order ON df2_order.order_id = df1_order.order_id group by month, region
                   ORDER BY month, total_sales desc;'''
    cursor.execute(Sqlquery)
    Table1 = cursor.fetchall()
    info = pd.DataFrame(Table1, columns=['Month','Region', 'Total Sales'])
    st.dataframe(info)
    
    df= pd.read_sql_query(Sqlquery,conn) # Reads query and copy to dataframe
    conn.close()

    plt.figure(figsize=(9,5))
    plt.bar(df['month'],df['total_sales'],width= 0.4,bottom= 0.9)
        
    # Add title and labels
    plt.title('Sales Analysis by Month')
    plt.xlabel('Month')
    plt.ylabel('Total Revenue')
    st.pyplot(plt)

elif(SelectedItem == "18.Calculate the total sales in a year by product"):
    st.write("Year on Year Total sales of product")
    Sqlquery = '''SELECT year(order_date) AS YEAR, sub_category, category, sum(sale_price) as total_sales FROM df2_order
                  JOIN df1_order ON df2_order.order_id = df1_order.order_id group by year, sub_category,category
                  ORDER BY year, total_sales desc;'''
    cursor.execute(Sqlquery)
    Table1 = cursor.fetchall()
    info = pd.DataFrame(Table1, columns=['Year','Category','Product Name','Total Sales'])
    st.dataframe(info)
    
    df= pd.read_sql_query(Sqlquery,conn) # Reads query and copy to dataframe
    conn.close()

    plt.figure(figsize=(9,5))
    plt.bar(df['YEAR'],df['total_sales'],width= 0.4,bottom= 0.9)
        
    # Add title and labels
    plt.title('Sales Analysis by Product')
    plt.xlabel('Year')
    plt.ylabel('Total Revenue')
    st.pyplot(plt)

elif(SelectedItem == "19.List the Products with sales more than 20,000 "):
    st.write("Products with sales more than 20,000 from region")
    Sqlquery = ''' SELECT  product_id, region,sum(sale_price) as total_sales FROM df2_order
                   RIGHT JOIN  df1_order ON df2_order.order_id = df1_order.order_id group by product_id, region
                   HAVING sum(sale_price) > 10000
                   ORDER BY total_sales desc;'''
    cursor.execute(Sqlquery)
    Table1 = cursor.fetchall()
    info = pd.DataFrame(Table1, columns=['Product ID','Region','Total Sales'])
    st.dataframe(info)
elif(SelectedItem == "20.Revenue from discounted sales"):
    st.write("Revenue from dicounted sales")
    Sqlquery = ''' SELECT sub_category, case when discount_percent > 0 then 'discounted'
	               else 'Not-Discounted'
	               end as sale_type, sum(sale_price) as total_revenue from df2_order group by sub_category, sale_type;'''
    cursor.execute(Sqlquery)
    Table1 = cursor.fetchall()
    info = pd.DataFrame(Table1, columns=['Product','Sales type','Total Revenue'])
    st.dataframe(info)
