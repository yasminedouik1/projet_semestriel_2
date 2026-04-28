import streamlit as st

st.set_page_config(
    page_title="Digital Lifestyle - Risque Dépression",
    page_icon="🧠",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif;
}

.stApp {
    background-color: #f7f5f0;
}

h1 {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 2.4rem !important;
    font-weight: 700 !important;
    color: #1a3a5c !important;
    letter-spacing: -0.5px;
}

.stMarkdown p {
    color: #5a6e82 !important;
    font-size: 0.95rem;
    line-height: 1.75;
}

.stMarkdown strong {
    color: #1a3a5c !important;
    font-weight: 600;
}

[data-testid="stSidebar"] {
    background: #1a3a5c !important;
}
[data-testid="stSidebar"] .stSuccess {
    background: rgba(232,184,75,0.15) !important;
    border: 1px solid rgba(232,184,75,0.4) !important;
    border-radius: 8px !important;
    color: #e8b84b !important;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-weight: 600;
    font-size: 0.85rem;
}
[data-testid="stSidebar"] * {
    color: #c8d8e8 !important;
}

::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: #f7f5f0; }
::-webkit-scrollbar-thumb { background: #b8d0ea; border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: #1a6cb5; }
</style>
""", unsafe_allow_html=True)

st.title("🧠 Digital Lifestyle Benchmark 2025")
st.markdown("""
**Application de prédiction du risque de dépression** basée sur les habitudes numériques.

**Deux approches disponibles :**
- **Classification** : Prédire si la personne est à **haut risque** (`high_risk_flag`)
- **Régression** : Prédire le **score de dépression** (`depression_score`)
""")

st.sidebar.success("Choisissez une page dans le menu à gauche")