import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from config import get_theme_colors

def render_monthly_sales(df):
    """Render monthly sales bar chart"""
    monthly_sales = df.groupby("mes")["ventas_total"].sum().reset_index()
    
    fig = px.bar(
        monthly_sales, x="mes", y="ventas_total",
        title="📅 Monthly Sales Trend",
        color="ventas_total",
        color_continuous_scale="Viridis",
        labels={"ventas_total": "Sales ($)", "mes": "Month"}
    )
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

def render_regional_sales(df):
    """Render regional sales pie chart"""
    regional_sales = df.groupby("region")["ventas_total"].sum().reset_index()
    
    fig = px.pie(
        regional_sales, values="ventas_total", names="region",
        title="🌎 Sales by Region",
        hole=0.4
    )
    st.plotly_chart(fig, use_container_width=True)

def render_product_sales(df):
    """Render horizontal product sales bar chart"""
    product_sales = df.groupby("producto")["ventas_total"].sum().sort_values(ascending=True).reset_index()
    
    fig = px.bar(
        product_sales, x="ventas_total", y="producto",
        orientation="h",
        title="🛍️ Sales by Product",
        color="ventas_total",
        color_continuous_scale="Blues",
        labels={"ventas_total": "Sales ($)", "producto": ""}
    )
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

def render_salesperson_performance(df):
    """Render salesperson performance comparison chart"""
    salesperson_ranking = df.groupby("vendedor").agg(
        sales=("ventas_total", "sum"),
        profit=("ganancia", "sum")
    ).reset_index().sort_values("sales", ascending=False)
    
    colors = get_theme_colors()
    fig = px.bar(
        salesperson_ranking, x="vendedor", y=["sales", "profit"],
        title="👤 Sales vs Profit by Salesperson",
        barmode="group",
        labels={"value": "$", "vendedor": ""},
        color_discrete_map={"sales": colors['primary'], "profit": colors['secondary']}
    )
    st.plotly_chart(fig, use_container_width=True)

def render_channel_sales(df):
    """Render sales channel pie chart"""
    channel_data = df.groupby("canal")["ventas_total"].sum().reset_index()
    colors = get_theme_colors()
    
    fig = px.pie(
        channel_data, values="ventas_total", names="canal",
        title="🛒 Sales by Channel",
        hole=0.5,
        color_discrete_sequence=[colors['primary'], colors['secondary']]
    )
    st.plotly_chart(fig, use_container_width=True)

def render_transaction_table(df):
    """Render detailed transaction table"""
    st.subheader("📋 Transaction Details")
    table = df[["fecha", "vendedor", "producto", "region", "unidades", "ventas_total", "ganancia", "margen_%"]].copy()
    table["fecha"] = table["fecha"].dt.strftime("%Y-%m-%d")
    table["ventas_total"] = table["ventas_total"].apply(lambda x: f"${x:,.0f}")
    table["ganancia"] = table["ganancia"].apply(lambda x: f"${x:,.0f}")
    table["margen_%"] = table["margen_%"].apply(lambda x: f"{x}%")
    st.dataframe(table, use_container_width=True, height=300)

def render_charts_row1(df):
    """Render first row of charts: Monthly sales + Regional sales"""
    col1, col2 = st.columns([2, 1])
    
    with col1:
        render_monthly_sales(df)
    
    with col2:
        render_regional_sales(df)

def render_charts_row2(df):
    """Render second row of charts: Product sales + Salesperson performance"""
    col3, col4 = st.columns(2)
    
    with col3:
        render_product_sales(df)
    
    with col4:
        render_salesperson_performance(df)

def render_charts_row3(df):
    """Render third row: Channel sales + Transaction table"""
    col5, col6 = st.columns([1, 2])
    
    with col5:
        render_channel_sales(df)
    
    with col6:
        render_transaction_table(df)
