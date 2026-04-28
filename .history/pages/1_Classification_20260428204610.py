import streamlit as st
import joblib
from utils.preprocessing import prepare_input_classification

st.set_page_config(page_title="Classification - Risque Dépression", page_icon="🔍", layout="wide")

st.title("🔍 Prédiction du Risque Élevé de Dépression")
st.markdown("**Modèle de Classification** — Prédit si `high_risk_flag` = 1")

@st.cache_resource
def load_model():
    return joblib.load("models/classification_model.joblib")

model = load_model()

st.header("Vos habitudes numériques")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("📱 Usage numérique")
    age = st.number_input("Âge", 13, 50, 25)
    device_hours = st.slider("Heures d'appareil par jour", 0.0, 18.0, 7.0, 0.1)
    phone_unlocks = st.number_input("Déverrouillages téléphone/jour", 0, 400, 150)
    notifications = st.number_input("Notifications par jour", 0, 1500, 300)
    social_media = st.number_input("Minutes réseaux sociaux", 0, 700, 150)
    digital_dependence = st.slider("Score dépendance numérique", 0.0, 100.0, 35.0)

with col2:
    st.subheader("🏃 Mode de vie")
    study_mins = st.number_input("Minutes étude/travail", 0, 500, 100)
    physical_activity = st.slider("Jours d'activité physique / semaine", 0, 7, 3)
    sleep_hours = st.slider("Heures de sommeil", 3.0, 12.0, 7.0, 0.1)
    sleep_quality = st.slider("Qualité du sommeil", 1.0, 5.0, 3.0, 0.1)
    productivity = st.slider("Score productivité", 0, 100, 65)
    focus_score = st.slider("Score de concentration", 0, 100, 50)

with col3:
    st.subheader("🧠 Bien-être mental")
    anxiety_score = st.slider("Score d'anxiété", 0.0, 30.0, 7.0)
    depression_score = st.slider("Score de dépression actuel", 0.0, 25.0, 8.0)
    stress_level = st.slider("Niveau de stress", 0.0, 15.0, 5.0)
    happiness_score = st.slider("Score de bonheur", 0.0, 10.0, 7.0, 0.1)

st.divider()

if st.button("Prédire le Risque", type="primary", use_container_width=True):

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
        'depression_score': depression_score,
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