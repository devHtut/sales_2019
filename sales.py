import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.set_page_config(page_title = 'My Sales Dashboard', page_icon = ':bar-chart:', layout = 'wide')

df = pd.read_csv('all_df.csv')

st.sidebar.header("Please Filter Here")

my_select_product = st.sidebar.multiselect(
    'Select Product', 
    options = df['Product'].unique(), default = df['Product'].unique()[:5]
)

my_select_city = st.sidebar.multiselect(
    'Select City', 
    options = df['City'].unique(), default = df['City'].unique()[:5]
)

my_select_month = st.sidebar.multiselect(
    'Select Month', 
    options = df['Month'].unique(), default = df['Month'].unique()[:5]
)

st.title('My Sales Dashboard 2019')

st.markdown('##')

total_sales = df['Total'].sum()

no_of_unique_product = df['Product'].nunique()

left_col, right_col = st.columns(2)

with left_col:
    st.subheader('Total Sales')
    st.subheader(f'US $ {total_sales}')

with right_col:
    st.subheader('No. of Product')
    st.subheader(f'{no_of_unique_product}')

a, b, c = st.columns(3)

df_select = df.query("Product == @my_select_product and City == @my_select_city and Month == @my_select_month")

sales_by_product = df_select.groupby('Product')['Total'].sum().sort_values()

fig_sales_by_product = px.bar(sales_by_product, 
       x = sales_by_product.values, 
       y = sales_by_product.index,
       orientation = 'h',
       title = 'Total Sales by Product')

a.plotly_chart(fig_sales_by_product, use_container_width = True)

fig_sales_by_city = px.pie(
    df_select,
    values = 'Total',
    names = 'City',
    title = 'Total Sales by City'
)

b.plotly_chart(fig_sales_by_city, use_container_width = True)

sales_by_month = df_select.groupby('Month')['Total'].sum().sort_values()

fig_sales_by_month = px.bar(sales_by_month, 
       x = sales_by_month.values, 
       y = sales_by_month.index,
       orientation = 'h',
       title = 'Total Sales by Month')

c.plotly_chart(fig_sales_by_month, use_container_width = True)

d, e = st.columns(2)

fig_sales_by_month_line = px.line(sales_by_month, 
       x = sales_by_month.values, 
       y = sales_by_month.index,
       orientation = 'h',
       title = 'Total Sales by Month')

d.plotly_chart(fig_sales_by_month_line, use_container_width = True)

fig_sales_by_scatter = px.scatter(
    df,
    y = 'QuantityOrdered',
    x = 'Total',
    title = 'Total Sales by ItemAmount'
)

e.plotly_chart(fig_sales_by_scatter, use_container_width = True)