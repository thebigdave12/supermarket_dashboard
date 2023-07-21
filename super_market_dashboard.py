import streamlit as st;
import pandas as pd;
import numpy as np;
import seaborn as sns;
import matplotlib.pyplot as plt 


st.title('Supermarket Dashboard')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv('supermarket.csv', nrows=nrows)
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Done! (using st.cache_data)')

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.dataframe(data)

st.header("Overarching Store Data")

with st.expander("Total Stores:"):
    total_stores= data.store_id.count()
    st.write(f'{total_stores}')
with st.expander("Total Sales:"):
    total_sales = data.store_sales.sum()
    st.write(f'$ {total_sales}')
with st.expander("Total Daily Customers:"):
    total_daily_customers = data.daily_customer_count.sum()
    st.write(f'{total_daily_customers}')
with st.expander("Current Available Inventory:"):
    total_ava_inventory = data.items_available.sum()
    st.write(f'{total_ava_inventory}')
with st.expander("Average Sales Per Store:"):
    avg_store_sales = round(data.store_sales.sum() / data.store_id.count())
    st.write(f'$ {avg_store_sales}')
with st.expander("Average Daily Customers Per Store:"):
    avg_daily_customers = round(data.daily_customer_count.sum() / data.store_id.count())
    st.write(f'{avg_daily_customers}')



st.header("Top 5 Stores vs Bottom 5 Stores")
sorted_df = data.sort_values(by='store_sales', ascending=False)
top_5_stores = sorted_df.nlargest(5, 'store_sales')
bottom_5_stores = sorted_df.nsmallest(5, 'store_sales')
sales = data["store_sales"]

show_top = st.checkbox('Show Top 5 Highest Selling Stores')

if show_top:
    st.bar_chart(data=top_5_stores, x="store_id", y="store_sales")
    col1, col2, col3 = st.columns(3)
    col1.metric("Highest Selling Store", "$116,320", "9.6% than next closest")
    col2.metric("Average Sales per Top 5 Store", "$105,704", "179% than avg store")
    col3.metric("Sales Above Bottom 5 Stores", "$437,990", "5.9x more in sales")
show_bottom = st.checkbox('Show Bottom 5 Lowest Selling Stores')
if show_bottom:
    st.bar_chart(data=bottom_5_stores, x="store_id", y="store_sales")
    col1, col2, col3 = st.columns(3)
    col1.metric("Lowest Selling Store", "$14,920", "-8.9% than next closest")
    col2.metric("Average Sales per Bottom 5 Store", "$18,106", "-322% than avg store")
    col3.metric("Sales Below Bottom 5 Stores", "$-437,990", "-5.9x less in sales")
print(data.store_sales.mean())
print(top_5_stores.store_sales.mean())
print(bottom_5_stores.store_sales.mean())

print(top_5_stores.store_sales.sum())
print(bottom_5_stores.store_sales.sum())