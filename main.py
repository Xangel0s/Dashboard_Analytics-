import streamlit as st

# Import modules
from config import setup_page_config
from data_loader import load_sales_data, apply_filters, calculate_kpis
from filters import render_sidebar
from kpis import render_main_kpis
from meta_dashboard import render_goal_dashboard
from charts import render_charts_row1, render_charts_row2, render_charts_row3

# ─── INITIAL CONFIGURATION ─────────────────────────────────────
setup_page_config()

# ─── DATA LOADING ───────────────────────────────────────────
df = load_sales_data()

# ─── SIDEBAR WITH FILTERS ───────────────────────────────────────
regions, categories, channels, salespeople = render_sidebar(df)

# ─── APPLY FILTERS ───────────────────────────────────────────
filtered_df = apply_filters(df, regions, categories, channels, salespeople)

# ─── MAIN HEADER ───────────────────────────────────────────
st.title("📊 Sales Analytics Pro - 2024")
st.markdown("---")

# ─── MAIN KPIS ───────────────────────────────────────────
kpis = calculate_kpis(filtered_df)
render_main_kpis(kpis)

st.markdown("---")

# ─── GOAL TRACKING DASHBOARD ─────────────────────────────────
render_goal_dashboard(filtered_df, salespeople)

st.markdown("---")

# ─── MAIN CHARTS ─────────────────────────────────────────────
st.subheader("📈 Sales Analysis Dashboard")

# Row 1: Monthly sales + Regional sales
render_charts_row1(filtered_df)

# Row 2: Product sales + Salesperson performance  
render_charts_row2(filtered_df)

# Row 3: Channel sales + Transaction table
render_charts_row3(filtered_df)

# ─── FOOTER ───────────────────────────────────────────────────
st.markdown("---")
st.caption("Sales Analytics Pro v2.0.0 | Built with Streamlit + Plotly | Data: ventas_data.csv")
