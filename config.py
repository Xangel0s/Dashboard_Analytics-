import streamlit as st

# ─── MAIN CONFIGURATION ───────────────────────────────────────
def setup_page_config():
    """Configure the main Streamlit page"""
    st.set_page_config(
        page_title="Sales Analytics Pro",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="expanded"
    )

def get_theme_colors():
    """Return the theme color palette"""
    return {
        'primary': "#6C63FF",
        'secondary': "#00D4AA", 
        'background': "#0F1117",
        'secondary_bg': "#1E1E2E",
        'text': "#FAFAFA",
        'success': "#00D4AA",
        'warning': "#FFA500",
        'danger': "#FF4444"
    }

def get_app_info():
    """Return application information"""
    return {
        'name': "Sales Analytics Pro",
        'subtitle': "Business Intelligence Dashboard",
        'version': "2.0.0",
        'logo_url': "https://img.icons8.com/color/96/combo-chart.png"
    }
