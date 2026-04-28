import streamlit as st

st.set_page_config(
    page_title="Digital Lifestyle - Risque Dépression",
    page_icon="🧠",
    layout="wide"
)

# ─── CSS GLOBAL ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600&family=DM+Serif+Display&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #0f1117 0%, #1a1f2e 50%, #0f1117 100%);
    min-height: 100vh;
}

h1 {
    font-family: 'DM Serif Display', serif !important;
    font-size: 2.6rem !important;
    background: linear-gradient(90deg, #e0eaff, #a5b4fc);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: -0.5px;
    margin-bottom: 0.3rem !important;
}

.stMarkdown p {
    color: #8892b0 !important;
    font-size: 0.95rem;
    line-height: 1.7;
}

.stMarkdown strong {
    color: #cdd6f4 !important;
}

/* Cards approche */
.approach-card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(165,180,252,0.15);
    border-radius: 16px;
    padding: 1.6rem 2rem;
    margin-top: 2rem;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: rgba(15,17,23,0.95) !important;
    border-right: 1px solid rgba(165,180,252,0.1) !important;
}

[data-testid="stSidebar"] .stSuccess {
    background: rgba(99,102,241,0.12) !important;
    border: 1px solid rgba(99,102,241,0.25) !important;
    border-radius: 10px !important;
    color: #a5b4fc !important;
    font-size: 0.85rem;
}

/* Scrollbar */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: #0f1117; }
::-webkit-scrollbar-thumb { background: #2a2f45; border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: #6366f1; }
</style>
""", unsafe_allow_html=True)

# ─── CONTENU ──────────────────────────────────────────────────────────────────
st.title("🧠 Digital Lifestyle Benchmark 2025")
st.markdown("""
**Application de prédiction du risque de dépression** basée sur les habitudes numériques.

**Deux approches disponibles :**
- **Classification** : Prédire si la personne est à **haut risque** (`high_risk_flag`)
- **Régression** : Prédire le **score de dépression** (`depression_score`)
""")

st.sidebar.success("Choisissez une page dans le menu à gauche")