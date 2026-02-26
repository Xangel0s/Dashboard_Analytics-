import streamlit as st
import pandas as pd

@st.cache_data
def load_sales_data():
    """
    Load and process sales data
    Apply date conversion BEFORE any grouping to prevent errors
    """
    df = pd.read_csv("ventas_data.csv")
    
    # Convert dates BEFORE any grouping (critical to prevent errors)
    df["fecha"] = pd.to_datetime(df["fecha"])
    df["mes"] = df["fecha"].dt.to_period("M").astype(str)
    
    # Calculate derived metrics
    df["ganancia"] = df["ventas_total"] - df["costo_total"]
    df["margen_%"] = (df["ganancia"] / df["ventas_total"] * 100).round(1)
    
    return df

def apply_filters(df, regions, categories, channels, salespeople):
    """Apply selected filters to DataFrame"""
    return df[
        df["region"].isin(regions) &
        df["categoria"].isin(categories) &
        df["canal"].isin(channels) &
        df["vendedor"].isin(salespeople)
    ]

def calculate_kpis(df):
    """Calculate main KPIs"""
    return {
        'total_sales': df["ventas_total"].sum(),
        'total_profit': df["ganancia"].sum(),
        'avg_margin': df["margen_%"].mean(),
        'total_units': df["unidades"].sum(),
        'unique_customers': df["cliente"].nunique(),
        'total_target': df["meta_mensual"].sum()
    }
