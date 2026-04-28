import streamlit as st

st.set_page_config(
    page_title="Digital Lifestyle - Risque Dépression",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ====================== CSS GLOBAL ======================
st.markdown("""
    <style>
    .main { padding-top: 1.5rem; }
    .stApp { background-color: #f8fafc; }
    
    h1 {
        color: #1e3a8a;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #1e3a8a !important;
        color: white !important;
    }
    
    .stButton>button {
        background-color: #3b82f6;
        color: white;
        font-weight: 600;
        border-radius: 10px;
        padding: 0.8rem 1.5rem;
        width: 100%;
        margin: 6px 0;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #2563eb;
        transform: translateY(-2px);
    }
    
    /* Conteneurs */
    .form-container, .result-container {
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

# ====================== TITRE ======================
st.title("🧠 Digital Lifestyle Benchmark 2025")
st.markdown("**Application intelligente de prédiction du risque de dépression** basée sur les habitudes numériques.")
st.markdown("---")

# ====================== SIDEBAR ======================
st.sidebar.success("Navigation")
st.sidebar.markdown("### Choisissez une approche")

page = st.sidebar.radio(
    "Approche d'analyse",
    ["🔍 Classification - Risque Élevé", "📈 Régression - Score de Dépression"],
    label_visibility="collapsed"
)

# ====================== AFFICHAGE DES PAGES ======================
if page == "🔍 Classification - Risque Élevé":
    from pages.classification import show_page
    show_page()

elif page == "📈 Régression - Score de Dépression":
    from pages.regression import show_page
    show_page()import streamlit as st

st.set_page_config(
    page_title="Digital Lifestyle - Risque Dépression",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ====================== CSS GLOBAL ======================
st.markdown("""
    <style>
    .main { padding-top: 1.5rem; }
    .stApp { background-color: #f8fafc; }
    
    h1 {
        color: #1e3a8a;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #1e3a8a !important;
        color: white !important;
    }
    
    .stButton>button {
        background-color: #3b82f6;
        color: white;
        font-weight: 600;
        border-radius: 10px;
        padding: 0.8rem 1.5rem;
        width: 100%;
        margin: 6px 0;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #2563eb;
        transform: translateY(-2px);
    }
    
    /* Conteneurs */
    .form-container, .result-container {
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

# ====================== TITRE ======================
st.title("🧠 Digital Lifestyle Benchmark 2025")
st.markdown("**Application intelligente de prédiction du risque de dépression** basée sur les habitudes numériques.")
st.markdown("---")

# ====================== SIDEBAR ======================
st.sidebar.success("Navigation")
st.sidebar.markdown("### Choisissez une approche")

page = st.sidebar.radio(
    "Approche d'analyse",
    ["🔍 Classification - Risque Élevé", "📈 Régression - Score de Dépression"],
    label_visibility="collapsed"
)

# ====================== AFFICHAGE DES PAGES ======================
if page == "🔍 Classification - Risque Élevé":
    from pages.classification import show_page
    show_page()

elif page == "📈 Régression - Score de Dépression":
    from pages.regression import show_page
    show_page()