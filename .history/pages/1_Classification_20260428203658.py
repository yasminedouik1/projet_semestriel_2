import streamlit as st
import joblib
import os
from utils.preprocessing import prepare_input_classification

# Chemins corrects
MODEL_PATH = "models/classification_model.joblib"   # ou os.path.join("..", "classification_model.joblib") si besoin

st.set_page_config(page_title="Classification - Risque Dépression", page_icon="🔍", layout="wide")

st.title("🔍 Prédiction du Risque Élevé de Dépression")
st.markdown("**Modèle de Classification** — Prédit si `high_risk_flag` = 1")

@st.cache_resource
def load_model():
    try:
        return joblib.load(MODEL_PATH)
    except Exception as e:
        st.error(f"Erreur de chargement du modèle de classification : {e}")
        st.stop()

model = load_model()

st.sidebar.header("Vos habitudes numériques")

age = st.sidebar.number_input("Âge", 13, 50, 25)
device_hours = st.sidebar.slider("Heures d'appareil par jour", 0.0, 18.0, 7.0, 0.1)
phone_unlocks = st.sidebar.number_input("Déverrouillages téléphone/jour", 0, 400, 150)
notifications = st.sidebar.number_input("Notifications par jour", 0, 1500, 300)
social_media = st.sidebar.number_input("Minutes réseaux sociaux", 0, 700, 150)
study_mins = st.sidebar.number_input("Minutes étude/travail", 0, 500, 100)
physical_activity = st.sidebar.slider("Jours d'activité physique / semaine", 0, 7, 3)
sleep_hours = st.sidebar.slider("Heures de sommeil", 3.0, 12.0, 7.0, 0.1)
sleep_quality = st.sidebar.slider("Qualité du sommeil", 1.0, 5.0, 3.0, 0.1)
anxiety_score = st.sidebar.slider("Score d'anxiété", 0.0, 30.0, 7.0)
depression_score = st.sidebar.slider("Score de dépression actuel", 0.0, 25.0, 8.0)   # important !
stress_level = st.sidebar.slider("Niveau de stress", 0.0, 15.0, 5.0)
happiness_score = st.sidebar.slider("Score de bonheur", 0.0, 10.0, 7.0, 0.1)
focus_score = st.sidebar.slider("Score de concentration", 0, 100, 50)
digital_dependence = st.sidebar.slider("Score dépendance numérique", 0.0, 100.0, 35.0)
productivity = st.sidebar.slider("Score productivité", 0, 100, 65)

if st.button("Prédire le Risque", type="primary"):
    
    user_input = {
        'age': age,
        'device_hours_per_day': device_hours,
        'phone_unlocks': phone_unlocks,
        'notifications_per_day': notifications,
        'social_media_mins': social_media,
        'study_mins': study_mins,
        'physical_activity_days': physical_activity,
        'sleep_hours': sleep_hours,
        'sleep_quality': sleep_quality,
        'anxiety_score': anxiety_score,
        'depression_score': depression_score,          # très important
        'stress_level': stress_level,
        'happiness_score': happiness_score,
        'focus_score': focus_score,
        'digital_dependence_score': digital_dependence,
        'productivity_score': productivity,
        
        # One-hot et encoded (valeurs par défaut)
        'gender_encoded': 0,
        'region_encoded': 0,
        'income_level_encoded': 2,
        'education_level_encoded': 0,
        'daily_role_encoded': 1,
        'device_type_encoded': 0,
        'gender_Male': 0,
        'daily_role_Full-time Employee': 1,
        'daily_role_Part-time/Shift': 0,
        'daily_role_Student': 0,
        'daily_role_Unemployed_Looking': 0,
        # Ajoute d'autres si nécessaire
    }

    input_df = prepare_input_classification(user_input)
    
    proba = model.predict_proba(input_df)[0][1]
    prediction = model.predict(input_df)[0]

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Probabilité de Haut Risque", f"{proba:.1%}")
    with col2:
        if prediction == 1:
            st.error("🚨 **Haut risque** de dépression")
        else:
            st.success("✅ **Risque faible**")

    import plotly.graph_objects as go
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=proba * 100,
        title={'text': "Probabilité de Haut Risque (%)"},
        gauge={'axis': {'range': [0, 100]}}
    ))
    st.plotly_chart(fig, use_container_width=True)