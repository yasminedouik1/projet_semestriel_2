import streamlit as st

st.set_page_config(
    page_title="Digital Lifestyle - Risque Dépression",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ====================== CSS PERSONNALISÉ ======================
st.markdown("""
    <style>
    /* Style général */
    .main {
        padding-top: 2rem;
    }
    .stApp {
        background-color: #f8f9fa;
    }
    
    /* Titre principal */
    h1 {
        color: #1e3a8a;
        font-weight: 700;
    }
    
    /* Sidebar */
    .css-1d391kg, .css-12oz5g7 {
        background-color: #1e3a8a !important;
        color: white !important;
    }
    .sidebar .sidebar-content {
        background-color: #1e3a8a;
    }
    
    /* Boutons */
    .stButton>button {
        background-color: #1e40af;
        color: white;
        font-weight: 600;
        border-radius: 8px;
        padding: 0.6rem 1.5rem;
        border: none;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #1e3a8a;
        transform: translateY(-2px);
    }
    
    /* Métriques */
    .stMetric {
        background-color: white;
        border-radius: 10px;
        padding: 1rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    /* Gauge */
    .stPlotlyChart {
        background-color: white;
        border-radius: 12px;
        padding: 1rem;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    }
    
    /* Info box */
    .stAlert {
        border-radius: 10px;
    }
    
    /* Amélioration des sliders et inputs */
    .stSlider {
        padding-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# ====================== CONTENU ======================
st.title("🧠 Digital Lifestyle Benchmark 2025")
st.markdown("""
**Application intelligente de prédiction du risque de dépression** basée sur les habitudes numériques des utilisateurs.
""")

st.sidebar.success("Sélectionnez une approche dans le menu ci-dessous")

st.markdown("---")