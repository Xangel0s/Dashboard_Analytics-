import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ─── CONFIG ───────────────────────────────────────────────
st.set_page_config(
    page_title="Dashboard de Ventas",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─── CARGAR DATOS ─────────────────────────────────────────
@st.cache_data
def cargar_datos():
    df = pd.read_csv("ventas_data.csv")
    # Convertir fechas ANTES de cualquier agrupación
    df["fecha"] = pd.to_datetime(df["fecha"])
    df["mes"] = df["fecha"].dt.to_period("M").astype(str)
    df["ganancia"] = df["ventas_total"] - df["costo_total"]
    df["margen_%"] = (df["ganancia"] / df["ventas_total"] * 100).round(1)
    return df

df = cargar_datos()

# ─── SIDEBAR ──────────────────────────────────────────────
with st.sidebar:
    col_logo, col_title = st.columns([1, 3])
    with col_logo:
        st.image("https://img.icons8.com/color/96/combo-chart.png", width=80)
    with col_title:
        st.markdown("# Analytics Pro")
        st.markdown("### Sales Intelligence")
        st.markdown("---")
    
    st.title("Filtros")

    regiones = st.multiselect(
        "🌎 Región",
        options=df["region"].unique(),
        default=df["region"].unique()
    )
    categorias = st.multiselect(
        "📦 Categoría",
        options=df["categoria"].unique(),
        default=df["categoria"].unique()
    )
    canal = st.multiselect(
        "🛒 Canal",
        options=df["canal"].unique(),
        default=df["canal"].unique()
    )
    vendedores = st.multiselect(
        "👤 Vendedor",
        options=df["vendedor"].unique(),
        default=df["vendedor"].unique()
    )

# Aplicar filtros
df_f = df[
    df["region"].isin(regiones) &
    df["categoria"].isin(categorias) &
    df["canal"].isin(canal) &
    df["vendedor"].isin(vendedores)
]

# ─── HEADER ───────────────────────────────────────────────
st.title("📊 Dashboard de Ventas 2024")
st.markdown("---")

# ─── KPIs ─────────────────────────────────────────────────
k1, k2, k3, k4, k5 = st.columns(5)

total_ventas   = df_f["ventas_total"].sum()
total_ganancia = df_f["ganancia"].sum()
margen_prom    = df_f["margen_%"].mean()
total_unidades = df_f["unidades"].sum()
num_clientes   = df_f["cliente"].nunique()

k1.metric("💰 Ventas Totales",   f"${total_ventas:,.0f}")
k2.metric("📈 Ganancia Total",   f"${total_ganancia:,.0f}")
k3.metric("🎯 Margen Promedio",  f"{margen_prom:.1f}%")
k4.metric("📦 Unidades Vendidas", f"{total_unidades:,}")
k5.metric("🤝 Clientes Únicos",   num_clientes)

st.markdown("---")

# ─── GAUGE CHART DE METAS ─────────────────────────────────
st.subheader("🎯 Avance vs Metas Mensuales")
col_gauge1, col_gauge2 = st.columns(2)

with col_gauge1:
    # Calcular avance de metas por vendedor actual
    if len(vendedores) > 0:
        meta_actual = df_f[df_f["vendedor"].isin(vendedores)]["meta_mensual"].mean()
        ventas_actuales = df_f[df_f["vendedor"].isin(vendedores)]["ventas_total"].sum()
        if meta_actual > 0:
            avance_pct = min((ventas_actuales / meta_actual) * 100, 100)
        else:
            avance_pct = 0
    else:
        avance_pct = 0
        meta_actual = 0
    
    fig_gauge = go.Figure(go.Indicator(
        mode = "gauge+number+delta",
        value = avance_pct,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': f"Avance de Meta<br><span style='font-size:0.8em;color:gray'>Meta: ${meta_actual:,.0f}</span>"},
        delta = {'reference': 100},
        gauge = {
            'axis': {'range': [None, 100]},
            'bar': {'color': "#6C63FF"},
            'steps': [
                {'range': [0, 50], 'color': "#1E1E2E"},
                {'range': [50, 80], 'color': "#2D2D3D"},
                {'range': [80, 100], 'color': "#3D3D4D"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 90
            }
        }
    ))
    fig_gauge.update_layout(height=300, font={'color': "#FAFAFA"})
    st.plotly_chart(fig_gauge, use_container_width=True)

with col_gauge2:
    # Métricas de metas
    meta_total = df_f["meta_mensual"].sum()
    ventas_total = df_f["ventas_total"].sum()
    cumplimiento_global = (ventas_total / meta_total * 100) if meta_total > 0 else 0
    
    st.metric("📊 Meta Total Acumulada", f"${meta_total:,.0f}")
    st.metric("✅ Cumplimiento Global", f"{cumplimiento_global:.1f}%")
    if cumplimiento_global >= 100:
        st.success("🎉 ¡Meta superada!")
    elif cumplimiento_global >= 80:
        st.warning("⚠️ Cerca de la meta")
    else:
        st.error("❌ Por debajo de la meta")

st.markdown("---")

# ─── FILA 1: Ventas por mes + Por región ──────────────────
col1, col2 = st.columns([2, 1])

with col1:
    ventas_mes = df_f.groupby("mes")["ventas_total"].sum().reset_index()
    fig1 = px.bar(
        ventas_mes, x="mes", y="ventas_total",
        title="📅 Ventas por Mes",
        color="ventas_total",
        color_continuous_scale="Viridis",
        labels={"ventas_total": "Ventas ($)", "mes": "Mes"}
    )
    fig1.update_layout(showlegend=False)
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    ventas_region = df_f.groupby("region")["ventas_total"].sum().reset_index()
    fig2 = px.pie(
        ventas_region, values="ventas_total", names="region",
        title="🌎 Ventas por Región",
        hole=0.4
    )
    st.plotly_chart(fig2, use_container_width=True)

# ─── FILA 2: Por producto + Por vendedor ──────────────────
col3, col4 = st.columns(2)

with col3:
    ventas_prod = df_f.groupby("producto")["ventas_total"].sum().sort_values(ascending=True).reset_index()
    fig3 = px.bar(
        ventas_prod, x="ventas_total", y="producto",
        orientation="h",
        title="🛍️ Ventas por Producto",
        color="ventas_total",
        color_continuous_scale="Blues",
        labels={"ventas_total": "Ventas ($)", "producto": ""}
    )
    fig3.update_layout(showlegend=False)
    st.plotly_chart(fig3, use_container_width=True)

with col4:
    vend_ranking = df_f.groupby("vendedor").agg(
        ventas=("ventas_total", "sum"),
        ganancia=("ganancia", "sum")
    ).reset_index().sort_values("ventas", ascending=False)

    fig4 = px.bar(
        vend_ranking, x="vendedor", y=["ventas", "ganancia"],
        title="👤 Ventas vs Ganancia por Vendedor",
        barmode="group",
        labels={"value": "$", "vendedor": ""},
        color_discrete_map={"ventas": "#6C63FF", "ganancia": "#00D4AA"}
    )
    st.plotly_chart(fig4, use_container_width=True)

# ─── FILA 3: Canal + Tabla ────────────────────────────────
col5, col6 = st.columns([1, 2])

with col5:
    canal_data = df_f.groupby("canal")["ventas_total"].sum().reset_index()
    fig5 = px.pie(
        canal_data, values="ventas_total", names="canal",
        title="🛒 Ventas por Canal",
        hole=0.5,
        color_discrete_sequence=["#6C63FF", "#00D4AA"]
    )
    st.plotly_chart(fig5, use_container_width=True)

with col6:
    st.subheader("📋 Detalle de Transacciones")
    tabla = df_f[["fecha", "vendedor", "producto", "region", "unidades", "ventas_total", "ganancia", "margen_%"]].copy()
    tabla["fecha"] = tabla["fecha"].dt.strftime("%Y-%m-%d")
    tabla["ventas_total"] = tabla["ventas_total"].apply(lambda x: f"${x:,.0f}")
    tabla["ganancia"] = tabla["ganancia"].apply(lambda x: f"${x:,.0f}")
    tabla["margen_%"] = tabla["margen_%"].apply(lambda x: f"{x}%")
    st.dataframe(tabla, use_container_width=True, height=300)

# ─── FOOTER ───────────────────────────────────────────────
st.markdown("---")
st.caption("Dashboard creado con Streamlit + Plotly | Datos: ventas_data.csv")
