# 📊 Sales Analytics Pro - Professional Dashboard

[![Streamlit](https://img.shields.io/badge/Streamlit-1.54+-red?style=for-the-badge&logo=streamlit)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Plotly](https://img.shields.io/badge/Plotly-6.5+-yellow?style=for-the-badge&logo=plotly)](https://plotly.com/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

A **professional, modular sales analytics dashboard** built with Streamlit and Plotly. Features real-time KPIs, interactive charts, goal tracking, and advanced filtering capabilities.

## ✨ Key Features

### 🎯 **Advanced Analytics**
- **Real-time KPIs**: Total Sales, Profit, Margin, Units, Customers
- **Goal Tracking**: Interactive gauge charts showing progress vs targets
- **Performance Metrics**: Individual and team performance analysis
- **Trend Analysis**: Monthly sales trends and patterns

### 📊 **Interactive Visualizations**
- **7 Chart Types**: Bar charts, pie charts, horizontal bars, gauge indicators
- **Dynamic Filtering**: Region, Category, Channel, Salesperson filters
- **Responsive Design**: Professional dark theme with custom color palette
- **Data Tables**: Formatted transaction details with sorting

### 🏗️ **Professional Architecture**
- **Modular Design**: Clean separation of concerns across 7 modules
- **Best Practices**: Type hints, docstrings, error handling
- **Performance**: Cached data loading and optimized rendering
- **Scalability**: Easy to extend and maintain

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip package manager

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/sales-analytics-pro.git
cd sales-analytics-pro

# Install dependencies
pip install -r requirements.txt

# Run the dashboard
streamlit run main.py
```

### 🌐 Access
Open your browser and navigate to **http://localhost:8501**

## 📁 Project Structure

```
sales-analytics-pro/
├── main.py                 # Entry point and application flow
├── config.py              # Configuration and theme settings
├── data_loader.py         # Data processing and caching
├── filters.py             # Interactive sidebar filters
├── kpis.py               # KPI calculations and display
├── meta_dashboard.py     # Goal tracking and gauge charts
├── charts.py             # All visualization components
├── requirements.txt       # Python dependencies
├── .streamlit/
│   └── config.toml       # Streamlit theme configuration
├── ventas_data.csv        # Sample sales data
└── README.md             # This file
```

## 🎨 Architecture Overview

### Module Responsibilities

| Module | Purpose | Key Functions |
|--------|---------|---------------|
| **`config.py`** | Central configuration | Theme colors, app info, page setup |
| **`data_loader.py`** | Data processing | Load, clean, cache, calculate metrics |
| **`filters.py`** | User interface | Sidebar, interactive filters |
| **`kpis.py`** | Business metrics | Calculate and display KPIs |
| **`meta_dashboard.py`** | Goal tracking | Gauge charts, progress indicators |
| **`charts.py`** | Data visualization | All chart components |
| **`main.py`** | Application flow | Orchestrate all modules |

## 📊 Data Schema

The dashboard expects CSV data with the following columns:

```csv
fecha,vendedor,region,producto,categoria,unidades,precio_unitario,ventas_total,costo_total,meta_mensual,cliente,canal
```

**Field Descriptions:**
- `fecha`: Sale date
- `vendedor`: Salesperson name
- `region`: Geographic region (North/South/Center/East/West)
- `producto`: Product name
- `categoria`: Product category (Technology/Accessories/Storage/Networks)
- `unidades`: Units sold
- `precio_unitario`: Unit price ($)
- `ventas_total`: Total sale amount ($)
- `costo_total`: Total cost ($)
- `meta_mensual`: Monthly target ($)
- `cliente`: Customer name
- `canal`: Sales channel (Online/Store)

## 🎯 Key Features Explained

### 1. **Real-time KPI Dashboard**
- Total sales revenue with formatting
- Profit calculations and margins
- Unit sales tracking
- Customer count analysis

### 2. **Goal Tracking System**
- Interactive gauge charts
- Progress vs target visualization
- Individual and team goal tracking
- Performance indicators

### 3. **Advanced Filtering**
- Multi-select region filter
- Category-based filtering
- Sales channel selection
- Team member filtering

### 4. **Comprehensive Visualizations**
- Monthly sales trends
- Regional distribution analysis
- Product performance ranking
- Salesperson comparison charts
- Channel effectiveness analysis

## 🔧 Customization

### Theme Customization
Edit `config.py` to modify colors and branding:

```python
def get_theme_colors():
    return {
        'primary': "#6C63FF",
        'secondary': "#00D4AA",
        'background': "#0F1117",
        # ... more colors
    }
```

### Adding New Charts
Extend `charts.py` with new visualization functions:

```python
def render_custom_chart(df):
    # Your chart implementation
    fig = px.bar(...)
    st.plotly_chart(fig, use_container_width=True)
```

## 🚀 Deployment

### Streamlit Community Cloud
1. Push to GitHub
2. Connect to [Streamlit Cloud](https://streamlit.io/cloud)
3. Deploy with one click

### Docker Deployment
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "main.py"]
```

## 📈 Performance Features

- **Data Caching**: `@st.cache_data` for optimized loading
- **Lazy Loading**: Components render on-demand
- **Memory Efficient**: Optimized data processing
- **Fast Rendering**: Streamlit's optimized frontend

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) for the amazing framework
- [Plotly](https://plotly.com/) for interactive visualizations
- [Pandas](https://pandas.pydata.org/) for data manipulation

## 📞 Contact

**Project Creator:** Xangel0s
**LinkedIn:** https://www.linkedin.com/in/angel-lopez-de-la-cruz-79a7522a8/
**GitHub:** https://github.com/Xangel0s

---

⭐ **Star this repository** if you find it useful!

🔗 **Share on LinkedIn** to help others discover this dashboard!

#DataAnalytics #Streamlit #Python #Dashboard #BusinessIntelligence #SalesAnalytics
