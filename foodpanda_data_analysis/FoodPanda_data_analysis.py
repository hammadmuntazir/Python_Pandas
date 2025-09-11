import pandas as pd
import numpy as np

df=pd.read_csv('Foodpanda Analysis Dataset.csv')
# print(df)
     
         ### How many rows and columns are in the dataset?
# print(df.describe)
## [6000 rows x 20 columns]>

         ### What are the data types of each column?

# print(df.info())

## Data columns (total 20 columns):
# #  #   Column           Non-Null Count  Dtype
# # ---  ------           --------------  -----
# #  0   customer_id      6000 non-null   object
# #  1   gender           6000 non-null   object
# #  2   age              6000 non-null   object
# #  3   city             6000 non-null   object
# #  4   signup_date      6000 non-null   object
# #  5   order_id         6000 non-null   object
# #  6   order_date       6000 non-null   object
# #  7   restaurant_name  6000 non-null   object
# #  8   dish_name        6000 non-null   object
# #  9   category         6000 non-null   object
# #  10  quantity         6000 non-null   int64
# #  11  price            6000 non-null   float64
# #  12  payment_method   6000 non-null   object
# #  13  order_frequency  6000 non-null   int64
# #  14  last_order_date  6000 non-null   object
# #  15  loyalty_points   6000 non-null   int64
# #  16  churned          6000 non-null   object
# #  17  rating           6000 non-null   int64
# #  18  rating_date      6000 non-null   object
# #  19  delivery_status  6000 non-null   object
# # dtypes: float64(1), int64(4), object(15)


            ###Display the first 5 and last 5 rows.
# print(df.head(5).to_string())

## First 5 rows

##   customer_id  gender     age      city signup_date order_id order_date restaurant_name dish_name category  quantity    price payment_method  order_frequency last_order_date  loyalty_points   churned  rating rating_date delivery_status
## 0       C5663    Male   Adult  Peshawar   1/14/2024    O9663  8/23/2023      McDonald's    Burger  Italian         5  1478.27           Cash               38       7/19/2025             238    Active       3  10/14/2024       Cancelled
## 1       C2831    Male   Adult    Multan    7/7/2024    O6831  8/23/2023             KFC    Burger  Italian         3   956.04         Wallet               24      11/25/2024              81    Active       2   8/21/2025         Delayed
## 2       C2851   Other  Senior    Multan   6/20/2025    O6851  8/23/2023       Pizza Hut     Fries  Italian         2   882.51           Cash               42       5/10/2025              82  Inactive       3   9/19/2024         Delayed
## 3       C1694  Female  Senior  Peshawar    9/5/2023    O5694  8/23/2023          Subway     Pizza  Dessert         4   231.30           Card               27       7/24/2025              45  Inactive       2   6/29/2025         Delayed
## 4       C4339   Other  Senior    Lahore  12/29/2023    O8339  8/24/2023             KFC  Sandwich  Dessert         1  1156.69           Cash               35      12/21/2024             418  Inactive       3    3/6/2025       Cancelled

  ##last 5 rows
# print(df.tail(5).to_string()) 

##    customer_id  gender       age       city signup_date order_id order_date restaurant_name dish_name   category  quantity    price payment_method  order_frequency last_order_date  loyalty_points   churned  rating rating_date delivery_status
## 5995       C6849    Male     Adult     Multan  11/25/2024   O10849  8/22/2025       Pizza Hut    Burger    Italian         4   875.71           Cash               28      11/29/2024             166    Active       5  12/30/2024       Cancelled
## 5996       C3787  Female     Adult  Islamabad   1/28/2025    O7787  8/22/2025             KFC     Pizza    Italian         5  1118.26           Cash               12        6/8/2025             193  Inactive       3    2/9/2025         Delayed
## 5997       C2841   Other  Teenager  Islamabad  10/19/2023    O6841  8/22/2025             KFC  Sandwich    Italian         4  1005.83           Card               31      12/30/2024             278    Active       4   3/23/2025       Cancelled
## 5998       C1624    Male     Adult  Islamabad   6/17/2024    O5624  8/22/2025             KFC     Fries  Fast Food         4  1226.10           Card               37      12/27/2024              55  Inactive       2   3/15/2025       Delivered
## 5999       C2068  Female     Adult     Multan   3/15/2025    O6068  8/22/2025     Burger King     Fries  Fast Food         3  1131.27           Card                2       6/13/2025              41  Inactive       1   7/15/2025         Delayed

              ####   2. Customer Demographics
###  How many unique customers are there?
unique_customer=df['customer_id'].nunique()
print(f'number of unique customers are : {unique_customer}')

##What is the distribution of gender?
print(df['gender'].value_counts())
        # gender
        # Female    2018
        # Male      2017
        # Other     1965
        # Name: count

# #What is the distribution of age groups?
print(df['age'].value_counts())

# age
# Teenager    2062
# Adult       1984
# Senior      1954
# Name: count

## Which city has the most customers?
print(df.groupby('city')['customer_id'].count().idxmax())
# Multan


           #### 3. Order Analysis
##How many orders were placed in total?
total_orders = df['order_id'].nunique()
print(f"Total orders placed: {total_orders}")
## Which restaurant has the most orders?
restaurant_orders = df['restaurant_name'].value_counts()
most_orders_restaurant = restaurant_orders.idxmax()
print(f"{most_orders_restaurant} has the most orders: {restaurant_orders.max()}")
# Subway restaurant has most orders

   ##  What is the most popular dish?
most_popular_dish = df['dish_name'].value_counts().idxmax()
dish_count = df['dish_name'].value_counts().max()
print(f"'{most_popular_dish}' is the most popular dish with {dish_count} orders")
# Pasta is most popular dish

   ## What is the most popular food category?
most_popular_category = df['category'].value_counts().idxmax()
category_count = df['category'].value_counts().max()
print(f"'{most_popular_category}' is the most popular category with {category_count} orders")
# Italian

               #### 4. Financial Analysis 💰
##What is the total revenue generated?
total_revenue=df['price'].sum()
print(f'Total Revenue Generated is : {total_revenue}pkr')
# Total Revenue Generated is : 4803149.279999999pkr

##What is the average order value?
average_order_value = df['price'].mean()
print(f"Average order value: {average_order_value:.2f} pkr")
##Which payment method is most used?
payment_method_counts = df['payment_method'].value_counts()
most_used_payment = payment_method_counts.idxmax()
print(f"'{most_used_payment}' is the most used payment method: {payment_method_counts.max()} times")
