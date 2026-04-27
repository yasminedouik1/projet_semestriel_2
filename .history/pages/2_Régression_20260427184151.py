import streamlit as st
import pandas as pd
import joblib
import numpy as np

st.set_page_config(page_title="Régression - Score de Dépression", page_icon="📈", layout="wide")

st.title("📈 Prédiction par Régression")
st.markdown("**Prédiction du score continu de dépression (`depression_score`)** basé sur les habitudes numériques.")

# Chargement du modèle
@st.cache_resource
def load_regression_model():
    return joblib.load("models/regression_model.joblib")

model = load_regression_model()

# === Sidebar - Inputs utilisateur ===
st.sidebar.header("📊 Vos habitudes numériques")

device_hours = st.sidebar.slider("Heures d'utilisation d'appareil par jour", 0.0, 18.0, 6.5, step=0.1)
phone_unlocks = st.sidebar.number_input("Nombre de déverrouillages de téléphone par jour", 0, 400, 140)
digital_dependence = st.sidebar.slider("Score de dépendance numérique", 0.0, 100.0, 35.0)
sleep_quality = st.sidebar.slider("Qualité du sommeil (1-5)", 1.0, 5.0, 3.0, step=0.1)
anxiety_score = st.sidebar.slider("Score d'anxiété", 0.0, 30.0, 7.0)
sleep_hours = st.sidebar.slider("Heures de sommeil par nuit", 3.0, 12.0, 7.2, step=0.1)
happiness_score = st.sidebar.slider("Score de bonheur", 0.0, 10.0, 7.0, step=0.1)
stress_level = st.sidebar.slider("Niveau de stress", 0.0, 15.0, 5.0)
focus_score = st.sidebar.slider("Score de concentration", 0, 100, 50)
notifications = st.sidebar.number_input("Notifications par jour", 0, 1500, 300)
social_media = st.sidebar.number_input("Minutes sur les réseaux sociaux", 0, 700, 150)
study_mins = st.sidebar.number_input("Minutes d'étude/travail intellectuel", 0, 500, 100)
physical_activity = st.sidebar.slider("Jours d'activité physique par semaine", 0, 7, 3)
productivity = st.sidebar.slider("Score de productivité", 0, 100, 65)

# Features catégorielles / encodées (à adapter selon ton feature selection)
high_risk_flag = st.sidebar.selectbox("Êtes-vous déjà considéré à haut risque ?", [0, 1], index=0)

# Création du DataFrame d'entrée
input_data = {
    'device_hours_per_day': [device_hours],
    'phone_unlocks': [phone_unlocks],
    'digital_dependence_score': [digital_dependence],
    'sleep_quality': [sleep_quality],
    'anxiety_score': [anxiety_score],
    'sleep_hours': [sleep_hours],
    'happiness_score': [happiness_score],
    'high_risk_flag': [high_risk_flag],
    'stress_level': [stress_level],
    'focus_score': [focus_score],
    'social_media_mins': [social_media],
    'daily_role_Unemployed_Looking': [0],           # À ajuster selon les inputs
    'productivity_score': [productivity],
    'study_mins': [study_mins],
    'notifications_per_day': [notifications],
    'physical_activity_days': [physical_activity],
    'education_level_encoded': [1],                 # À améliorer avec un selectbox
    'region_Europe': [0],
    'device_type_Tablet': [0],
    'region_Asia': [0],
    'income_level_Low': [0],
    'device_type_Laptop': [0],
    'daily_role_Part-time/Shift': [0]
}

input_df = pd.DataFrame(input_data)

if st.button("🔮 Prédire le Score de Dépression", type="primary"):
    prediction = model.predict(input_df)[0]
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.metric(
            label="**Score de Dépression Prédit**",
            value=f"{prediction:.2f}",
            delta=None
        )
        
        # Interprétation
        if prediction < 5:
            st.success("🟢 **Niveau faible** de dépression")
        elif prediction < 10:
            st.warning("🟡 **Niveau modéré** de dépression")
        else:
            st.error("🔴 **Niveau élevé** de dépression - Consultez un professionnel")

    # Gauge visuelle (avec plotly)
    import plotly.graph_objects as go
    
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=prediction,
        title={'text': "Score de Dépression"},
        gauge={
            'axis': {'range': [0, 20]},
            'bar': {'color': "darkblue"},
            'steps': [
                {'range': [0, 5], 'color': "lightgreen"},
                {'range': [5, 10], 'color': "yellow"},
                {'range': [10, 20], 'color': "red"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 10
            }
        }
    ))
    
    st.plotly_chart(fig, use_container_width=True)

st.info("💡 Les features utilisées sont celles sélectionnées lors de l'étape de Feature Selection pour la régression.")