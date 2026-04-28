import streamlit as st
import pandas as pd
import joblib
from utils.preprocessing import prepare_input_regression

st.set_page_config(page_title="Régression - Score de Dépression", page_icon="📈", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif;
}

.stApp {
    background-color: #f7f5f0;
}

h1 {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 2rem !important;
    font-weight: 700 !important;
    color: #1a3a5c !important;
    letter-spacing: -0.5px;
}

.stMarkdown p {
    color: #5a6e82 !important;
    font-size: 0.93rem;
}

h2 {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-weight: 600 !important;
    color: #1a3a5c !important;
    font-size: 1.15rem !important;
    border-bottom: 2px solid #e8b84b !important;
    padding-bottom: 0.4rem !important;
}

h3 {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-weight: 700 !important;
    color: #1a3a5c !important;
    font-size: 0.75rem !important;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    margin-bottom: 1.2rem !important;
    background: #e8b84b;
    border-radius: 4px;
    padding: 0.3rem 0.7rem;
    display: inline-block;
}

[data-testid="column"] {
    background: #ffffff;
    border: 1px solid #e2ddd4;
    border-radius: 14px;
    padding: 1.4rem 1.6rem !important;
    box-shadow: 0 2px 8px rgba(26,58,92,0.06);
}

label {
    color: #3d5166 !important;
    font-size: 0.82rem !important;
    font-weight: 600 !important;
}

[data-testid="stSlider"] [role="slider"] {
    background-color: #1a6cb5 !important;
    border-color: #1a6cb5 !important;
}
[data-testid="stSlider"] > div > div > div {
    background: #1a6cb5 !important;
}

[data-testid="stNumberInput"] input {
    background: #f7f5f0 !important;
    border: 1.5px solid #d6d0c4 !important;
    border-radius: 8px !important;
    color: #1a3a5c !important;
    font-size: 0.9rem !important;
}
[data-testid="stNumberInput"] input:focus {
    border-color: #1a6cb5 !important;
    box-shadow: 0 0 0 3px rgba(26,108,181,0.15) !important;
}

[data-testid="stSelectbox"] > div > div {
    background: #f7f5f0 !important;
    border: 1.5px solid #d6d0c4 !important;
    border-radius: 8px !important;
    color: #1a3a5c !important;
}

hr {
    border-color: #e2ddd4 !important;
    margin: 1.5rem 0 !important;
}

.stButton > button[kind="primary"] {
    background: #e8b84b !important;
    color: #1a3a5c !important;
    border: none !important;
    border-radius: 10px !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-weight: 700 !important;
    font-size: 0.95rem !important;
    letter-spacing: 0.03em;
    padding: 0.65rem 2rem !important;
    box-shadow: 0 3px 12px rgba(232,184,75,0.4) !important;
    transition: all 0.18s ease !important;
}
.stButton > button[kind="primary"]:hover {
    background: #d4a53a !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 5px 18px rgba(232,184,75,0.5) !important;
}

.stSuccess {
    background: #eaf7f0 !important;
    border: 1.5px solid #6ecfa3 !important;
    border-radius: 10px !important;
    color: #1a5c3a !important;
}
.stError {
    background: #fdf0ee !important;
    border: 1.5px solid #e8836b !important;
    border-radius: 10px !important;
    color: #7a2214 !important;
}
.stWarning {
    background: #fdf8ec !important;
    border: 1.5px solid #e8b84b !important;
    border-radius: 10px !important;
    color: #7a5a10 !important;
}

[data-testid="stSidebar"] {
    background: #1a3a5c !important;
}
[data-testid="stSidebar"] .stSuccess {
    background: rgba(232,184,75,0.15) !important;
    border: 1px solid rgba(232,184,75,0.4) !important;
    border-radius: 8px !important;
    color: #e8b84b !important;
}
[data-testid="stSidebar"] * {
    color: #c8d8e8 !important;
}

::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: #f7f5f0; }
::-webkit-scrollbar-thumb { background: #b8d0ea; border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: #1a6cb5; }
</style>
""", unsafe_allow_html=True)

st.title("📈 Prédiction du Score de Dépression")
st.markdown("**Modèle de Régression** — Prédit le score continu de dépression.")

@st.cache_resource
def load_model():
    try:
        return joblib.load("models/regression_model.joblib")
    except Exception as e:
        st.error(f"Erreur de chargement du modèle : {e}")
        st.stop()

model = load_model()

st.header("Vos habitudes numériques")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("📱 Usage numérique")
    device_hours = st.slider("Heures d'appareil par jour", 0.0, 18.0, 6.5, 0.1)
    phone_unlocks = st.number_input("Déverrouillages téléphone/jour", 0, 400, 140)
    digital_dependence = st.slider("Dépendance numérique", 0.0, 100.0, 35.0)
    notifications = st.number_input("Notifications/jour", 0, 1500, 300)
    social_media = st.number_input("Min. réseaux sociaux", 0, 700, 150)

with col2:
    st.subheader("🏃 Mode de vie")
    sleep_hours = st.slider("Heures de sommeil", 3.0, 12.0, 7.2, 0.1)
    sleep_quality = st.slider("Qualité du sommeil", 1.0, 5.0, 3.0, 0.1)
    study_mins = st.number_input("Min. étude/travail", 0, 500, 100)
    physical_activity = st.slider("Jours activité physique/semaine", 0, 7, 3)
    productivity = st.slider("Score productivité", 0, 100, 65)

with col3:
    st.subheader("🧠 Bien-être mental")
    anxiety_score = st.slider("Score anxiété", 0.0, 30.0, 7.0)
    happiness_score = st.slider("Score de bonheur", 0.0, 10.0, 7.0, 0.1)
    stress_level = st.slider("Niveau de stress", 0.0, 15.0, 5.0)
    focus_score = st.slider("Score de concentration", 0, 100, 50)
    high_risk_flag = st.selectbox("Haut risque connu ?", [0, 1], index=0)

st.divider()

if st.button("Prédire le Score de Dépression", type="primary", use_container_width=True):
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

    import plotly.graph_objects as go
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=prediction,
        title={'text': "Score de Dépression", 'font': {'family': 'Plus Jakarta Sans', 'color': '#1a3a5c'}},
        number={'font': {'color': '#1a3a5c', 'family': 'Plus Jakarta Sans'}},
        gauge={
            'axis': {'range': [0, 20], 'tickcolor': '#5a6e82'},
            'bar': {'color': '#1a6cb5'},
            'bgcolor': '#f7f5f0',
            'steps': [
                {'range': [0, 5], 'color': '#eaf7f0'},
                {'range': [5, 10], 'color': '#fdf8ec'},
                {'range': [10, 20], 'color': '#fdf0ee'},
            ],
            'threshold': {'line': {'color': '#e8b84b', 'width': 3}, 'value': 10}
        }
    ))
    fig.update_layout(paper_bgcolor='#ffffff', plot_bgcolor='#ffffff', font_color='#1a3a5c')
    st.plotly_chart(fig, use_container_width=True)