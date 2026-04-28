import streamlit as st
import importlib.util
import sys
import os

st.set_page_config(
    page_title="Digital Lifestyle - Risque Dépression",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ====================== CSS AMÉLIORÉ ======================
st.markdown("""
    <style>
    .main { padding-top: 1.5rem; }
    .stApp { background-color: #f8fafc; }
    
    h1 { color: #1e3a8a; font-weight: 700; margin-bottom: 0.5rem; }
    
    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #1e3a8a !important;
        color: white !important;
    }
    
    .stButton>button {
        background-color: #3b82f6;
        color: white;
        font-weight: 600;
        border-radius: 8px;
        padding: 0.75rem 1.5rem;
        width: 100%;
        margin-bottom: 8px;
    }
    .stButton>button:hover {
        background-color: #2563eb;
    }
    
    .form-container, .result-container, .description-box {
        background-color: white;
        padding: 2rem;
        border-radius: 16px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
        margin-bottom: 1.5rem;
    }
    
    .stMetric, .stPlotlyChart {
        background-color: white;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.06);
    }
    </style>
""", unsafe_allow_html=True)

st.title("🧠 Digital Lifestyle Benchmark 2025")
st.markdown("**Application intelligente de prédiction du risque de dépression** basée sur les habitudes numériques.")
st.markdown("---")

# ====================== SIDEBAR ======================
st.sidebar.success("Navigation")
st.sidebar.markdown("### Choisissez une approche :")

page = st.sidebar.radio(
    "Approche d'analyse",
    ["🔍 Classification - Risque Élevé", "📈 Régression - Score de Dépression"],
    label_visibility="collapsed"
)

# ====================== FONCTION D'IMPORT DYNAMIQUE ======================
def import_module_from_file(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module

# ====================== DESCRIPTION + PAGE ======================
current_dir = os.path.dirname(os.path.abspath(__file__))

if page == "🔍 Classification - Risque Élevé":
    st.markdown("### 🔍 Approche Classification")
    st.markdown("""
    **Modèle de Classification** : Ce modèle prédit si l'utilisateur est à **haut risque** de dépression (Oui/Non) 
    en se basant sur ses habitudes numériques, son sommeil, son anxiété et son niveau de stress.
    """)
    
    try:
        classification = import_module_from_file("classification", os.path.join(current_dir, "classification.py"))
        classification.show_page()
    except FileNotFoundError:
        st.error("❌ Fichier `classification.py` non trouvé. Veuillez renommer `1_Classification.py` en `classification.py`")

elif page == "📈 Régression - Score de Dépression":
    st.markdown("### 📈 Approche Régression")
    st.markdown("""
    **Modèle de Régression** : Ce modèle prédit le **score continu** de dépression (de 0 à 20). 
    Il permet d’avoir une estimation plus fine du niveau de risque.
    """)
    
    try:
        regression = import_module_from_file("regression", os.path.join(current_dir, "regression.py"))
        regression.show_page()
    except FileNotFoundError:
        st.error("❌ Fichier `regression.py` non trouvé. Veuillez renommer `2_Régression.py` en `regression.py`")