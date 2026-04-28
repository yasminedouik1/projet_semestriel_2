import streamlit as st

st.set_page_config(
    page_title="Digital Lifestyle - Risque Dépression",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ====================== CSS ======================
st.markdown("""
    <style>
    .main { padding-top: 1.5rem; }
    .stApp { background-color: #f8fafc; }
    h1 { color: #1e3a8a; font-weight: 700; }
    
    section[data-testid="stSidebar"] {
        background-color: #1e3a8a !important;
        color: white !important;
    }
    
    .stButton>button {
        background-color: #3b82f6;
        color: white;
        font-weight: 600;
        border-radius: 8px;
        padding: 0.75rem;
        width: 100%;
    }
    
    .form-container, .result-container {
        background-color: white;
        padding: 2rem;
        border-radius: 16px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        margin-bottom: 1.5rem;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🧠 Digital Lifestyle Benchmark 2025")
st.markdown("**Application intelligente de prédiction du risque de dépression**")
st.markdown("---")

# Sidebar Navigation
st.sidebar.success("Navigation")
page = st.sidebar.radio(
    "Choisissez une approche :",
    ["🔍 Classification - Risque Élevé", "📈 Régression - Score de Dépression"]
)

# ====================== Chargement des pages ======================
if page == "🔍 Classification - Risque Élevé":
    try:
        from pages.classification import show_page
        show_page()
    except Exception as e:
        st.error(f"Erreur dans Classification : {e}")

elif page == "📈 Régression - Score de Dépression":
    try:
        from pages.regression import show_page
        show_page()
    except Exception as e:
        st.error(f"Erreur dans Régression : {e}")