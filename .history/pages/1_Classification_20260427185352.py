import streamlit as st
import joblib
from utils.preprocessing import prepare_input_classification

st.set_page_config(page_title="Classification - Risque Dépression", page_icon="🔍", layout="wide")

st.title("🔍 Prédiction du Risque Élevé")
st.markdown("**Modèle de Classification** — Prédit `high_risk_flag`")

@st.cache_resource
def load_model():
    return joblib.load("models/classification_model.joblib")

model = load_model()

st.sidebar.header("Vos habitudes numériques")

# Inputs principaux
age = st.sidebar.number_input("Âge", 13, 50, 25)
device_hours = st.sidebar.slider("Heures d'appareil/jour", 0.0, 18.0, 7.0, 0.1)
phone_unlocks = st.sidebar.number_input("Déverrouillages téléphone/jour", 0, 400, 150)
notifications = st.sidebar.number_input("Notifications/jour", 0, 1200, 300)
social_media = st.sidebar.number_input("Min. réseaux sociaux", 0, 700, 150)
anxiety = st.sidebar.slider("Score anxiété", 0.0, 30.0, 7.0)
stress = st.sidebar.slider("Niveau stress", 0.0, 15.0, 5.0)
sleep_hours = st.sidebar.slider("Heures sommeil", 3.0, 12.0, 7.0, 0.1)
happiness = st.sidebar.slider("Score bonheur", 0.0, 10.0, 7.0, 0.1)

if st.button("Prédire le Risque", type="primary"):
    user_input = {
        'age': age,
        'device_hours_per_day': device_hours,
        'phone_unlocks': phone_unlocks,
        'notifications_per_day': notifications,
        'social_media_mins': social_media,
        'anxiety_score': anxiety,
        'stress_level': stress,
        'sleep_hours': sleep_hours,
        'happiness_score': happiness,
        
        # Valeurs par défaut pour les one-hot (tu peux les rendre interactifs plus tard)
        'gender_Male': 0,
        'region_Asia': 0, 'region_Europe': 0, 'region_Middle East': 0,
        'region_North America': 0, 'region_South America': 0,
        'income_level_Low': 0, 'income_level_Lower-Mid': 1, 'income_level_Upper-Mid': 0,
        'education_level_High School': 0, 'education_level_Master': 0, 'education_level_PhD': 0,
        'daily_role_Full-time Employee': 1,
        'daily_role_Part-time/Shift': 0,
        'daily_role_Student': 0,
        'daily_role_Unemployed_Looking': 0,
        'device_type_Laptop': 0, 'device_type_Tablet': 0, 'device_type_iPhone': 0,
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

    # Gauge de probabilité
    import plotly.graph_objects as go
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=proba*100,
        title={'text': "Probabilité (%)"},
        gauge={'axis': {'range': [0, 100]}}
    ))
    st.plotly_chart(fig, use_container_width=True)