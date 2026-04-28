import streamlit as st
import joblib
from utils.preprocessing import prepare_input_classification

st.set_page_config(page_title="Classification - Risque Dépression", page_icon="🔍", layout="wide")

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

[data-testid="metric-container"] {
    background: #eef4fb !important;
    border: 1.5px solid #b8d0ea !important;
    border-radius: 12px !important;
    padding: 1rem 1.2rem !important;
}
[data-testid="metric-container"] label {
    color: #3d6a96 !important;
    font-size: 0.78rem !important;
    font-weight: 600 !important;
    text-transform: uppercase;
    letter-spacing: 0.06em;
}
[data-testid="metric-container"] [data-testid="metric-value"] {
    color: #1a3a5c !important;
    font-size: 2rem !important;
    font-weight: 700 !important;
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
        title={'text': "Probabilité de Haut Risque (%)", 'font': {'family': 'Plus Jakarta Sans', 'color': '#1a3a5c'}},
        number={'font': {'color': '#1a3a5c', 'family': 'Plus Jakarta Sans'}},
        gauge={
            'axis': {'range': [0, 100], 'tickcolor': '#5a6e82'},
            'bar': {'color': '#1a6cb5'},
            'bgcolor': '#f7f5f0',
            'steps': [
                {'range': [0, 40], 'color': '#eef4fb'},
                {'range': [40, 70], 'color': '#fdf8ec'},
                {'range': [70, 100], 'color': '#fdf0ee'},
            ],
            'threshold': {'line': {'color': '#e8b84b', 'width': 3}, 'value': 50}
        }
    ))
    fig.update_layout(paper_bgcolor='#ffffff', plot_bgcolor='#ffffff', font_color='#1a3a5c')
    st.plotly_chart(fig, use_container_width=True)