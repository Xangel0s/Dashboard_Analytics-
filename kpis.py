import streamlit as st
from config import get_theme_colors

def render_main_kpis(kpis):
    """
    Render the 5 main KPIs in the header
    """
    colors = get_theme_colors()
    
    k1, k2, k3, k4, k5 = st.columns(5)
    
    with k1:
        st.metric(
            "💰 Total Sales", 
            f"${kpis['total_sales']:,.0f}",
            delta=None
        )
    
    with k2:
        st.metric(
            "📈 Total Profit", 
            f"${kpis['total_profit']:,.0f}",
            delta=None
        )
    
    with k3:
        st.metric(
            "🎯 Avg Margin", 
            f"{kpis['avg_margin']:.1f}%",
            delta=None
        )
    
    with k4:
        st.metric(
            "📦 Units Sold", 
            f"{kpis['total_units']:,}",
            delta=None
        )
    
    with k5:
        st.metric(
            "🤝 Unique Customers", 
            kpis['unique_customers'],
            delta=None
        )

def render_goal_kpis(df):
    """
    Render additional KPIs related to goals
    """
    total_target = df["meta_mensual"].sum()
    total_sales = df["ventas_total"].sum()
    achievement_rate = (total_sales / total_target * 100) if total_target > 0 else 0
    
    st.metric("📊 Total Target", f"${total_target:,.0f}")
    st.metric("✅ Achievement Rate", f"{achievement_rate:.1f}%")
    
    # Visual achievement indicator
    if achievement_rate >= 100:
        st.success("🎉 Target Exceeded!")
    elif achievement_rate >= 80:
        st.warning("⚠️ Close to Target")
    else:
        st.error("❌ Below Target")
    
    return achievement_rate
