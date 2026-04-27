import streamlit as st
import pandas as pd
import joblib
from utils.preprocessing import prepare_input_classification

st.title("🔍 Prédiction Classification - Risque Élevé")

@st.cache_resource
def load_model():
    return joblib.load("models/classification_model.joblib")

model = load_model()

# Sidebar pour les inputs utilisateur
st.sidebar.header("Vos habitudes numériques")

device_hours = st.sidebar.slider("Heures d'appareil par jour", 0.0, 18.0, 7.0)
phone_unlocks = st.sidebar.number_input("Déverrouillages de téléphone/jour", 0, 400, 150)
digital_dependence = st.sidebar.slider("Score de dépendance numérique", 0.0, 100.0, 35.0)
anxiety = st.sidebar.slider("Score d'anxiété", 0.0, 30.0, 7.0)
stress = st.sidebar.slider("Niveau de stress", 0.0, 15.0, 5.0)
sleep_hours = st.sidebar.slider("Heures de sommeil", 3.0, 12.0, 7.0)
# ... ajoute tous les features importants identifiés dans feature selection

if st.button("Prédire le risque"):
    input_df = prepare_input_classification(
        device_hours, phone_unlocks, digital_dependence, anxiety,
        stress, sleep_hours, # + autres features
    )
    
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
    
    # Optionnel : SHAP ou feature importance si tu as le temps