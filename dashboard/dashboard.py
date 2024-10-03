import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
from PIL import Image

def create_product_sell_df(df):
    product_sell_df = df.groupby('product_category_name_english')['customer_id'].nunique().reset_index().sort_values(by='customer_id', ascending=False)
    return product_sell_df

accepted_time = pd.read_csv("../data/accepted_time.csv")
delivery_time = pd.read_csv("../data/delivery_time.csv")
geolocation_lat = pd.read_csv("../data/geolocation_lat.csv")
geolocation_lng = pd.read_csv("../data/geolocation_lng.csv")
order_payments_dataset = pd.read_csv("../data/order_payments_dataset.csv")
product_sell = pd.read_csv("../data/product_sell.csv")

st.header('Garuda Toserba :sparkles:')

with st.sidebar:

    st.title("Bagas Winerang")
    
    st.image("../data/toko.png")\


##### Sales Analysis #####
st.header("Sales Analysis of Product Categories")

# Group by product category and count unique customers
product_counts = product_sell.groupby('product_category_name_english')['customer_id'].nunique().sort_values(ascending=False)

# Select top 5 and bottom 5 products
top_5_products = product_counts.head(5).reset_index()
bottom_5_products = product_counts.tail(5).reset_index()

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))

# Plot top 5 products on the left (horizontal bar plot)
sns.barplot(x=top_5_products['customer_id'], y=top_5_products['product_category_name_english'], ax=ax1, color='blue')
ax1.set_xlabel('Number of Products Sold')
ax1.set_ylabel('Product Category')
ax1.set_title('Top 5 Best-Selling Products')

# Plot bottom 5 products on the right (horizontal bar plot)
sns.barplot(x=bottom_5_products['customer_id'], y=bottom_5_products['product_category_name_english'], ax=ax2, color='red')
ax2.set_xlabel('Number of Products Sold')
ax2.set_ylabel('Product Category')
ax2.set_title('Bottom 5 Least-Selling Products')

# Adjust the layout with space between the plots
plt.subplots_adjust(wspace=0.8)  # Adjust the space between the subplots

# Display the plot in Streamlit
st.pyplot(fig)

###### Acceptance and Delivery ######

st.header("Order Acceptance and Delivery Analysis")

accepted_times = accepted_time['accepted_time']
delivery_times = delivery_time['delivery_time']

colors = ["#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

# Create a figure with two subplots
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# Plot for accepted times
sns.histplot(accepted_time, bins=7, color=colors[0], ax=axs[0])
axs[0].set_xlabel('Order Acceptance Time (days)')
axs[0].set_ylabel('Frequency')
axs[0].set_title('Distribution of Order Acceptance Time')

# Plot for delivery times
sns.histplot(delivery_time, bins=20, color=colors[0], ax=axs[1])
axs[1].set_xlabel('Order Delivery Time (days)')
axs[1].set_ylabel('Frequency')
axs[1].set_title('Distribution of Order Delivery Time')

# Adjust layout and add space between subplots
plt.tight_layout()
plt.subplots_adjust(wspace=0.3)  # Adjust the width space between the subplots

# Display the plot in Streamlit
st.pyplot(fig)

####### Payment Type #######

st.header("Analysis of Payment Methods Used by Customers")

payment_type_counts = order_payments_dataset['payment_type'].value_counts()

# Create a bar plot
plt.figure(figsize=(10, 6))
sns.barplot(x=payment_type_counts.index, y=payment_type_counts.values, palette="viridis")
plt.xlabel('Payment Method')
plt.ylabel('Number of Transactions')
plt.title('Payment Methods Used by Customers')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.tight_layout()

# Display the plot in Streamlit
st.pyplot(plt)

####### Geographical ########

# Add a header in Streamlit
st.header('Distribution of Geolocation of Sellers and Customers in São Paulo')

# Load geolocation data from CSV files
geolocation_lat = pd.read_csv("../data/geolocation_lat.csv")
geolocation_lng = pd.read_csv("../data/geolocation_lng.csv")

latitudes = geolocation_lat['geolocation_lat']  # Replace 'latitude' with your actual column name
longitudes = geolocation_lng['geolocation_lng']  # Replace 'longitude' with your actual column name

# Create the scatter plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(longitudes, latitudes, color='blue', marker='o', s=0.5)  # Adjust 's' for size
ax.set_title('Geolocation Data of São Paulo')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.grid()

# Display the plot in Streamlit
st.pyplot(fig)