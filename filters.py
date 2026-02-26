import streamlit as st
from config import get_app_info

def render_sidebar(df):
    """
    Render sidebar with logo, title and interactive filters
    Returns selected filters
    """
    app_info = get_app_info()
    
    with st.sidebar:
        # Sidebar header
        col_logo, col_title = st.columns([1, 3])
        with col_logo:
            st.image(app_info['logo_url'], width=80)
        with col_title:
            st.markdown("# Sales Analytics")
            st.markdown("### Business Intelligence")
            st.markdown("---")
        
        st.title("Filters")
        
        # Interactive filters
        regions = st.multiselect(
            "🌎 Region",
            options=df["region"].unique(),
            default=df["region"].unique()
        )
        categories = st.multiselect(
            "📦 Category",
            options=df["categoria"].unique(),
            default=df["categoria"].unique()
        )
        channels = st.multiselect(
            "🛒 Channel",
            options=df["canal"].unique(),
            default=df["canal"].unique()
        )
        salespeople = st.multiselect(
            "👤 Salesperson",
            options=df["vendedor"].unique(),
            default=df["vendedor"].unique()
        )
        
        # Filter summary
        st.markdown("---")
        st.markdown("**Filter Summary:**")
        st.markdown(f"- Regions: {len(regions)} selected")
        st.markdown(f"- Categories: {len(categories)} selected")
        st.markdown(f"- Channels: {len(channels)} selected")
        st.markdown(f"- Salespeople: {len(salespeople)} selected")
        
        return regions, categories, channels, salespeople
