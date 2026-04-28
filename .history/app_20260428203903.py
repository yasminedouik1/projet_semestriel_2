import streamlit as st

st.set_page_config(
    page_title="Digital Lifestyle - Risque Dépression",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Digital Lifestyle Benchmark 2025")
st.markdown("""
**Application de prédiction du risque de dépression** basée sur les habitudes numériques.

**Deux approches disponibles :**
- **Classification** : Prédire si la personne est à **haut risque** (`high_risk_flag`)
- **Régression** : Prédire le **score de dépression** (`depression_score`)
""")

st.sidebar.success("Choisissez une page dans le menu à gauche")