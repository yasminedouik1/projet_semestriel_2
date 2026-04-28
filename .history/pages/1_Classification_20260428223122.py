import streamlit as st
import joblib
from utils.preprocessing import prepare_input_classification

st.set_page_config(page_title="Classification - Risque Dépression", page_icon="🔍", layout="wide")

# ─── CSS GLOBAL ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600&family=DM+Serif+Display&display=swap');

/* Base */
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

/* Fond principal */
.stApp {
    background: linear-gradient(135deg, #0f1117 0%, #1a1f2e 50%, #0f1117 100%);
    min-height: 100vh;
}

/* Titre principal */
h1 {
    font-family: 'DM Serif Display', serif !important;
    font-size: 2.2rem !important;
    background: linear-gradient(90deg, #e0eaff, #a5b4fc);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: -0.5px;
    margin-bottom: 0.2rem !important;
}

/* Sous-titre markdown */
.stMarkdown p {
    color: #8892b0 !important;
    font-size: 0.95rem;
}

/* Header section */
h2 {
    font-family: 'DM Sans', sans-serif !important;
    font-weight: 600 !important;
    color: #cdd6f4 !important;
    font-size: 1.25rem !important;
    border-bottom: 1px solid #2a2f45;
    padding-bottom: 0.5rem;
    margin-bottom: 1.2rem !important;
}

/* Subheaders colonnes */
h3 {
    font-family: 'DM Sans', sans-serif !important;
    font-weight: 500 !important;
    color: #a5b4fc !important;
    font-size: 0.9rem !important;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 1rem !important;
}

/* Blocs colonnes */
[data-testid="column"] {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(165,180,252,0.1);
    border-radius: 16px;
    padding: 1.4rem 1.6rem !important;
    backdrop-filter: blur(10px);
}

/* Labels des inputs */
label, .stSlider label, .stNumberInput label, .stSelectbox label {
    color: #8892b0 !important;
    font-size: 0.82rem !important;
    font-weight: 500 !important;
    letter-spacing: 0.03em;
}

/* Sliders — track */
[data-testid="stSlider"] > div > div > div > div {
    background: linear-gradient(90deg, #6366f1, #a5b4fc) !important;
}

/* Slider thumb */
[data-testid="stSlider"] > div > div > div > div > div {
    background: #a5b4fc !important;
    border: 2px solid #6366f1 !important;
    box-shadow: 0 0 8px rgba(99,102,241,0.5) !important;
}

/* Number inputs */
[data-testid="stNumberInput"] input {
    background: rgba(255,255,255,0.05) !important;
    border: 1px solid rgba(165,180,252,0.2) !important;
    border-radius: 8px !important;
    color: #e2e8f0 !important;
    font-size: 0.9rem !important;
}
[data-testid="stNumberInput"] input:focus {
    border-color: #6366f1 !important;
    box-shadow: 0 0 0 2px rgba(99,102,241,0.2) !important;
}

/* Selectbox */
[data-testid="stSelectbox"] > div > div {
    background: rgba(255,255,255,0.05) !important;
    border: 1px solid rgba(165,180,252,0.2) !important;
    border-radius: 8px !important;
    color: #e2e8f0 !important;
}

/* Divider */
hr {
    border-color: rgba(165,180,252,0.15) !important;
    margin: 1.5rem 0 !important;
}

/* Bouton principal */
.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #6366f1, #818cf8) !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-weight: 600 !important;
    font-size: 1rem !important;
    letter-spacing: 0.04em;
    padding: 0.65rem 2rem !important;
    box-shadow: 0 4px 20px rgba(99,102,241,0.35) !important;
    transition: all 0.2s ease !important;
}
.stButton > button[kind="primary"]:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 6px 28px rgba(99,102,241,0.5) !important;
}

/* Metrics */
[data-testid="metric-container"] {
    background: rgba(165,180,252,0.07) !important;
    border: 1px solid rgba(165,180,252,0.15) !important;
    border-radius: 12px !important;
    padding: 1rem 1.2rem !important;
}
[data-testid="metric-container"] label {
    color: #8892b0 !important;
    font-size: 0.8rem !important;
}
[data-testid="metric-container"] [data-testid="metric-value"] {
    color: #a5b4fc !important;
    font-size: 1.8rem !important;
    font-weight: 600 !important;
}

/* Alertes */
.stSuccess {
    background: rgba(52,211,153,0.1) !important;
    border: 1px solid rgba(52,211,153,0.25) !important;
    border-radius: 10px !important;
    color: #6ee7b7 !important;
}
.stError {
    background: rgba(248,113,113,0.1) !important;
    border: 1px solid rgba(248,113,113,0.25) !important;
    border-radius: 10px !important;
    color: #fca5a5 !important;
}
.stWarning {
    background: rgba(251,191,36,0.1) !important;
    border: 1px solid rgba(251,191,36,0.25) !important;
    border-radius: 10px !important;
    color: #fde68a !important;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: rgba(15,17,23,0.95) !important;
    border-right: 1px solid rgba(165,180,252,0.1) !important;
}
[data-testid="stSidebar"] .stSuccess {
    font-size: 0.85rem;
}

/* Scrollbar */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: #0f1117; }
::-webkit-scrollbar-thumb { background: #2a2f45; border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: #6366f1; }
</style>
""", unsafe_allow_html=True)

# ─── CONTENU ──────────────────────────────────────────────────────────────────
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