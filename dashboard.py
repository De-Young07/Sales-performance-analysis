import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load data
@st.cache
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def kpi_metrics(df):
    total_sales = df['Sales'].sum()
    total_profit = df['Profit'].sum()
    avg_discount = df['Discount'].mean()
    st.metric('Total Sales', f'${total_sales:,.2f}')
    st.metric('Total Profit', f'${total_profit:,.2f}')
    st.metric('Average Discount', f'{avg_discount:.2%}')

# Sales trends
def sales_trends(df):
    sales_by_year = df.groupby('Year')['Sales'].sum().reset_index()
    fig = px.line(sales_by_year, x='Year', y='Sales', title='Sales Trends Over Years')
    st.plotly_chart(fig)

# Category performance
def category_performance(df):
    category_sales = df.groupby('Category')['Sales'].sum().reset_index()
    fig = px.bar(category_sales, x='Category', y='Sales', title='Sales by Category')
    st.plotly_chart(fig)

# Geographic analysis
def geographic_analysis(df):
    geo_sales = df.groupby('Region')['Sales'].sum().reset_index()
    fig = px.choropleth(geo_sales, locations='Region', locationmode='USA-states', color='Sales', title='Sales by Region')
    st.plotly_chart(fig)

# Product performance
def product_performance(df):
    product_sales = df.groupby('Product')['Sales'].sum().reset_index()
    fig = px.pie(product_sales, names='Product', values='Sales', title='Product Performance')
    st.plotly_chart(fig)

# Discount analysis
def discount_analysis(df):
    discount_sales = df.groupby('Discount')['Sales'].sum().reset_index()
    fig = px.bar(discount_sales, x='Discount', y='Sales', title='Sales by Discount Rate')
    st.plotly_chart(fig)

# Shipping analysis
def shipping_analysis(df):
    shipping_data = df.groupby('Shipping_Mode')['Sales'].sum().reset_index()
    fig = px.bar(shipping_data, x='Shipping_Mode', y='Sales', title='Sales by Shipping Mode')
    st.plotly_chart(fig)

# Main app
def main():
    st.title('Sales Performance Dashboard')
    df = load_data('sales_data.csv')

    # Filters
    region = st.sidebar.multiselect('Select Region', options=df['Region'].unique())
    segment = st.sidebar.multiselect('Select Segment', options=df['Segment'].unique())
    year = st.sidebar.multiselect('Select Year', options=df['Year'].unique())

    if region:
        df = df[df['Region'].isin(region)]
    if segment:
        df = df[df['Segment'].isin(segment)]
    if year:
        df = df[df['Year'].isin(year)]

    kpi_metrics(df)
    sales_trends(df)
    category_performance(df)
    geographic_analysis(df)
    product_performance(df)
    discount_analysis(df)
    shipping_analysis(df)

if __name__ == '__main__':
    main()