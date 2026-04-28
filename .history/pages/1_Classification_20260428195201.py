import streamlit as st
import joblib
from utils.preprocessing import prepare_input_classification

st.title("🔍 Classification - Risque Élevé de Dépression")
st.markdown("**Modèle de classification** — Prédit si vous êtes à haut risque de dépression.")

# ====================== FORMULAIRE ======================
with st.container():
    st.markdown('<div class="form-container">', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input("Âge", 13, 50, 25)
        device_hours = st.slider("Heures d'appareil par jour", 0.0, 18.0, 7.0, 0.1)
        phone_unlocks = st.number_input("Déverrouillages téléphone/jour", 0, 400, 150)
        notifications = st.number_input("Notifications par jour", 0, 1500, 300)
        social_media = st.number_input("Minutes réseaux sociaux", 0, 700, 150)
        
    with col2:
        anxiety_score = st.slider("Score d'anxiété", 0.0, 30.0, 7.0)
        stress_level = st.slider("Niveau de stress", 0.0, 15.0, 5.0)
        sleep_hours = st.slider("Heures de sommeil", 3.0, 12.0, 7.0, 0.1)
        happiness_score = st.slider("Score de bonheur", 0.0, 10.0, 7.0, 0.1)
        depression_score = st.slider("Score de dépression actuel", 0.0, 25.0, 8.0)

    predict_btn = st.button("🚀 Prédire le Risque", type="primary", use_container_width=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# ====================== RÉSULTATS ======================
if predict_btn:
    with st.container():
        st.markdown('<div class="result-container">', unsafe_allow_html=True)
        
        user_input = {
            'age': age, 'device_hours_per_day': device_hours, 'phone_unlocks': phone_unlocks,
            'notifications_per_day': notifications, 'social_media_mins': social_media,
            'anxiety_score': anxiety_score, 'stress_level': stress_level,
            'sleep_hours': sleep_hours, 'happiness_score': happiness_score,
            'depression_score': depression_score,
            'focus_score': 50, 'digital_dependence_score': 35.0,
            'productivity_score': 65.0, 'physical_activity_days': 3,
            'study_mins': 100,
            'gender_encoded': 0, 'region_encoded': 0, 'income_level_encoded': 2,
            'education_level_encoded': 0, 'daily_role_encoded': 1,
            'device_type_encoded': 0, 'gender_Male': 0,
            'daily_role_Full-time Employee': 1,
        }

        input_df = prepare_input_classification(user_input)
        
        proba = model.predict_proba(input_df)[0][1]
        prediction = model.predict(input_df)[0]

        st.success("### Résultat de l'analyse")

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Probabilité de Haut Risque", f"{proba:.1%}")
        with col2:
            if prediction == 1:
                st.error("### 🚨 HAUT RISQUE DE DÉPRESSION")
            else:
                st.success("### ✅ Risque faible détecté")

        # Gauge
        import plotly.graph_objects as go
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=proba * 100,
            title={'text': "Probabilité de Haut Risque"},
            gauge={
                'axis': {'range': [0, 100]},
                'bar': {'color': "#ef4444" if proba > 0.5 else "#22c55e"},
                'steps': [{'range': [0, 50], 'color': "#86efac"}, {'range': [50, 100], 'color': "#fca5a5"}]
            }
        ))
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

else:
    st.info("👆 Remplissez le formulaire ci-dessus et cliquez sur **Prédire le Risque**")