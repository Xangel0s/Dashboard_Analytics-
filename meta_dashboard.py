import streamlit as st
import plotly.graph_objects as go
from config import get_theme_colors
from kpis import render_goal_kpis

def render_goal_dashboard(df, salespeople):
    """
    Render goal dashboard with gauge chart and related KPIs
    """
    colors = get_theme_colors()
    
    st.subheader("🎯 Goal Tracking & Progress")
    col_gauge1, col_gauge2 = st.columns(2)
    
    with col_gauge1:
        # Calculate goal progress for selected salespeople
        if len(salespeople) > 0:
            avg_target = df[df["vendedor"].isin(salespeople)]["meta_mensual"].mean()
            current_sales = df[df["vendedor"].isin(salespeople)]["ventas_total"].sum()
            if avg_target > 0:
                progress_pct = min((current_sales / avg_target) * 100, 100)
            else:
                progress_pct = 0
        else:
            progress_pct = 0
            avg_target = 0
        
        # Create gauge chart
        fig_gauge = go.Figure(go.Indicator(
            mode = "gauge+number+delta",
            value = progress_pct,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': f"Goal Progress<br><span style='font-size:0.8em;color:gray'>Target: ${avg_target:,.0f}</span>"},
            delta = {'reference': 100},
            gauge = {
                'axis': {'range': [None, 100]},
                'bar': {'color': colors['primary']},
                'steps': [
                    {'range': [0, 50], 'color': colors['secondary_bg']},
                    {'range': [50, 80], 'color': "#2D2D3D"},
                    {'range': [80, 100], 'color': "#3D3D4D"}
                ],
                'threshold': {
                    'line': {'color': colors['danger'], 'width': 4},
                    'thickness': 0.75,
                    'value': 90
                }
            }
        ))
        fig_gauge.update_layout(height=300, font={'color': colors['text']})
        st.plotly_chart(fig_gauge, use_container_width=True)
    
    with col_gauge2:
        # Goal KPIs
        achievement_rate = render_goal_kpis(df)
        
        # Additional metrics
        st.markdown("---")
        st.markdown("**Salesperson Performance:**")
        if len(salespeople) > 0:
            for salesperson in salespeople[:3]:  # Show up to 3 salespeople
                person_data = df[df["vendedor"] == salesperson]
                person_target = person_data["meta_mensual"].mean()
                person_sales = person_data["ventas_total"].sum()
                person_achievement = (person_sales / person_target * 100) if person_target > 0 else 0
                
                st.markdown(f"• {salesperson}: {person_achievement:.1f}%")
        else:
            st.markdown("• Select salespeople to see details")
    
    return progress_pct
