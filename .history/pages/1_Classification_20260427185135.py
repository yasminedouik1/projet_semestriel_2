import streamlit as st
import pandas as pd
import joblib
from utils.preprocessing import prepare_input_classification

st.set_page_config(page_title="Classification - Risque Dépression", page_icon="🔍", layout="wide")

st.title("🔍 Prédiction du Risque Élevé de Dépression")
st.markdown("**Modèle de Classification** — Prédit si la personne est à haut risque (`high_risk_flag`).")

# Chargement du modèle
@st.cache_resource
def load_model():
    try:
        return joblib.load("models/classification_model.joblib")
    except Exception as e:
        st.error(f"Erreur lors du chargement du modèle : {e}")
        st.stop()

model = load_model()

# Sidebar
st.sidebar.header("Vos habitudes numériques")

device_hours = st.sidebar.slider("Heures d'appareil par jour", 0.0, 18.0, 7.0, 0.1)
phone_unlocks = st.sidebar.number_input("Déverrouillages de téléphone/jour", 0, 400, 150)
digital_dependence = st.sidebar.slider("Score de dépendance numérique", 0.0, 100.0, 35.0)
anxiety = st.sidebar.slider("Score d'anxiété", 0.0, 30.0, 7.0)
stress = st.sidebar.slider("Niveau de stress", 0.0, 15.0, 5.0)
sleep_hours = st.sidebar.slider("Heures de sommeil", 3.0, 12.0, 7.0)
sleep_quality = st.sidebar.slider("Qualité du sommeil", 1.0, 5.0, 3.0, 0.1)
happiness_score = st.sidebar.slider("Score de bonheur", 0.0, 10.0, 7.0, 0.1)
focus_score = st.sidebar.slider("Score de concentration", 0, 100, 50)
notifications = st.sidebar.number_input("Notifications par jour", 0, 1200, 300)

if st.button("Prédire le Risque", type="primary"):
    user_input = {
        'device_hours_per_day': device_hours,
        'phone_unlocks': phone_unlocks,
        'digital_dependence_score': digital_dependence,
        'anxiety_score': anxiety,
        'stress_level': stress,
        'sleep_hours': sleep_hours,
        'sleep_quality': sleep_quality,
        'happiness_score': happiness_score,
        'focus_score': focus_score,
        'notifications_per_day': notifications,
    }

    input_df = prepare_input_classification(user_input)
    
    proba = model.predict_proba(input_df)[0][1]
    prediction = model.predict(input_df)[0]

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Probabilité de haut risque", f"{proba:.1%}")
    with col2:
        if prediction == 1:
            st.error("🚨 **Haut risque** de dépression")
        else:
            st.success("✅ **Risque faible**")

    # Optionnel : jauge de probabilité
    import plotly.graph_objects as go
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=proba * 100,
        title={'text': "Probabilité de Haut Risque (%)"},
        gauge={'axis': {'range': [0, 100]},
               'bar': {'color': "red" if proba > 0.5 else "green"}}
    ))
    st.plotly_chart(fig, use_container_width=True)

st.info("💡 Modèle de classification entraîné sur les features sélectionnées.")