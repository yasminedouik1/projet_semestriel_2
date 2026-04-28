import streamlit as st
import pandas as pd
import joblib
from utils.preprocessing import prepare_input_regression

st.set_page_config(page_title="Régression - Score de Dépression", page_icon="📈", layout="wide")

st.title("📈 Prédiction du Score de Dépression")
st.markdown("**Modèle de Régression** — Prédit le score continu de dépression.")

# Chargement du modèle
@st.cache_resource
def load_model():
    try:
        return joblib.load("models/regression_model.joblib")
    except Exception as e:
        st.error(f"Erreur de chargement du modèle de régression : {e}")
        st.stop()

model = load_model()

st.sidebar.header("Vos habitudes numériques")

# Inputs
device_hours = st.sidebar.slider("Heures d'appareil par jour", 0.0, 18.0, 6.5, 0.1)
phone_unlocks = st.sidebar.number_input("Déverrouillages téléphone/jour", 0, 400, 140)
digital_dependence = st.sidebar.slider("Dépendance numérique", 0.0, 100.0, 35.0)
sleep_quality = st.sidebar.slider("Qualité du sommeil", 1.0, 5.0, 3.0, 0.1)
anxiety_score = st.sidebar.slider("Score anxiété", 0.0, 30.0, 7.0)
sleep_hours = st.sidebar.slider("Heures de sommeil", 3.0, 12.0, 7.2, 0.1)
happiness_score = st.sidebar.slider("Score de bonheur", 0.0, 10.0, 7.0, 0.1)
stress_level = st.sidebar.slider("Niveau de stress", 0.0, 15.0, 5.0)
focus_score = st.sidebar.slider("Score de concentration", 0, 100, 50)
notifications = st.sidebar.number_input("Notifications/jour", 0, 1500, 300)
social_media = st.sidebar.number_input("Min. réseaux sociaux", 0, 700, 150)
study_mins = st.sidebar.number_input("Min. étude/travail", 0, 500, 100)
physical_activity = st.sidebar.slider("Jours activité physique/semaine", 0, 7, 3)
productivity = st.sidebar.slider("Score productivité", 0, 100, 65)
high_risk_flag = st.sidebar.selectbox("Haut risque connu ?", [0, 1], index=0)

if st.button("Prédire le Score de Dépression", type="primary"):
    user_input = {
        'device_hours_per_day': device_hours,
        'phone_unlocks': phone_unlocks,
        'digital_dependence_score': digital_dependence,
        'sleep_quality': sleep_quality,
        'anxiety_score': anxiety_score,
        'sleep_hours': sleep_hours,
        'happiness_score': happiness_score,
        'high_risk_flag': high_risk_flag,
        'stress_level': stress_level,
        'focus_score': focus_score,
        'social_media_mins': social_media,
        'study_mins': study_mins,
        'notifications_per_day': notifications,
        'physical_activity_days': physical_activity,
        'productivity_score': productivity,
        # One-hot features à 0 pour l'instant
        'daily_role_Unemployed_Looking': 0,
        'education_level_encoded': 1,
        'region_Europe': 0,
        'device_type_Tablet': 0,
        'region_Asia': 0,
        'income_level_Low': 0,
        'device_type_Laptop': 0,
        'daily_role_Part-time/Shift': 0,
    }

    input_df = prepare_input_regression(user_input)
    
    prediction = model.predict(input_df)[0]

    st.success(f"**Score de dépression prédit : {prediction:.2f}**")

    if prediction < 5:
        st.success("🟢 Niveau faible")
    elif prediction < 10:
        st.warning("🟡 Niveau modéré")
    else:
        st.error("🔴 Niveau élevé — Consultez un professionnel")

    # Gauge
    import plotly.graph_objects as go
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=prediction,
        title={'text': "Score de Dépression"},
        gauge={'axis': {'range': [0, 20]},
               'bar': {'color': "darkblue"},
               'steps': [
                   {'range': [0, 5], 'color': "lightgreen"},
                   {'range': [5, 10], 'color': "yellow"},
                   {'range': [10, 20], 'color': "red"}
               ]}
    ))
    st.plotly_chart(fig, use_container_width=True)