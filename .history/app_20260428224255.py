import streamlit as st

st.set_page_config(
    page_title="Digital Lifestyle - Risque Dépression",
    page_icon="🧠",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif;
}

.stApp {
    background-color: #f7f5f0;
}

[data-testid="stSidebar"] {
    background: #1a3a5c !important;
}
[data-testid="stSidebar"] .stSuccess {
    background: rgba(232,184,75,0.15) !important;
    border: 1px solid rgba(232,184,75,0.4) !important;
    border-radius: 8px !important;
    color: #e8b84b !important;
    font-weight: 600;
    font-size: 0.85rem;
}
[data-testid="stSidebar"] * {
    color: #c8d8e8 !important;
}

.hero-banner {
    background: linear-gradient(135deg, #1a3a5c 0%, #1e4d7a 60%, #1a3a5c 100%);
    border-radius: 18px;
    padding: 3rem 3.5rem;
    margin-bottom: 2.5rem;
    position: relative;
    overflow: hidden;
}
.hero-banner::before {
    content: '';
    position: absolute;
    top: -40px; right: -40px;
    width: 200px; height: 200px;
    background: rgba(232,184,75,0.08);
    border-radius: 50%;
}
.hero-banner::after {
    content: '';
    position: absolute;
    bottom: -60px; left: 30%;
    width: 280px; height: 280px;
    background: rgba(232,184,75,0.05);
    border-radius: 50%;
}
.hero-tag {
    display: inline-block;
    background: rgba(232,184,75,0.2);
    color: #e8b84b;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    padding: 0.3rem 0.9rem;
    border-radius: 20px;
    border: 1px solid rgba(232,184,75,0.35);
    margin-bottom: 1rem;
}
.hero-title {
    font-size: 2.6rem;
    font-weight: 800;
    color: #ffffff;
    letter-spacing: -1px;
    line-height: 1.15;
    margin-bottom: 1rem;
}
.hero-title span { color: #e8b84b; }
.hero-desc {
    color: #a8c4d8;
    font-size: 1rem;
    line-height: 1.75;
    max-width: 620px;
    margin-bottom: 1.8rem;
}
.hero-badges { display: flex; gap: 0.8rem; flex-wrap: wrap; }
.hero-badge {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.15);
    color: #d0e4f0;
    font-size: 0.8rem;
    font-weight: 500;
    padding: 0.35rem 0.9rem;
    border-radius: 20px;
}

.section-title {
    font-size: 1.2rem;
    font-weight: 700;
    color: #1a3a5c;
    margin-bottom: 0.3rem;
    padding-bottom: 0.4rem;
    border-bottom: 2px solid #e8b84b;
    display: inline-block;
}

.approach-card {
    background: #ffffff;
    border: 1px solid #e2ddd4;
    border-radius: 14px;
    padding: 1.5rem 1.8rem;
    box-shadow: 0 2px 8px rgba(26,58,92,0.06);
    height: 100%;
}
.approach-icon { font-size: 1.8rem; margin-bottom: 0.7rem; }
.approach-label {
    display: inline-block;
    font-size: 0.68rem;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    padding: 0.2rem 0.6rem;
    border-radius: 4px;
    margin-bottom: 0.7rem;
}
.label-blue { background: #eef4fb; color: #1a6cb5; }
.label-mustard { background: #fdf8ec; color: #9a6f10; }
.approach-title { font-size: 1.15rem; font-weight: 700; color: #1a3a5c; margin-bottom: 0.5rem; }
.approach-desc { font-size: 0.88rem; color: #5a6e82; line-height: 1.65; }

.stat-card {
    background: #ffffff;
    border: 1px solid #e2ddd4;
    border-radius: 12px;
    padding: 1.1rem 1.3rem;
    text-align: center;
    box-shadow: 0 2px 6px rgba(26,58,92,0.05);
}
.stat-number { font-size: 2rem; font-weight: 800; color: #1a6cb5; line-height: 1.1; }
.stat-label { font-size: 0.78rem; color: #5a6e82; font-weight: 500; margin-top: 0.3rem; }

.tip-card {
    background: #ffffff;
    border: 1px solid #e2ddd4;
    border-left: 4px solid #e8b84b;
    border-radius: 0 12px 12px 0;
    padding: 1.1rem 1.3rem;
    box-shadow: 0 2px 6px rgba(26,58,92,0.05);
    margin-bottom: 0.9rem;
}
.tip-title { font-size: 0.88rem; font-weight: 700; color: #1a3a5c; margin-bottom: 0.3rem; }
.tip-body { font-size: 0.82rem; color: #5a6e82; line-height: 1.6; }
.tip-icon { font-size: 1.1rem; margin-right: 0.4rem; }

.info-box {
    background: #eef4fb;
    border: 1px solid #b8d0ea;
    border-radius: 12px;
    padding: 1.2rem 1.5rem;
    margin-top: 0.5rem;
}
.info-box p { font-size: 0.85rem; color: #1a3a5c !important; line-height: 1.7; margin: 0; }

.warn-box {
    background: #fdf8ec;
    border: 1px solid #e8c97b;
    border-radius: 12px;
    padding: 1.2rem 1.5rem;
    margin-top: 1rem;
}
.warn-box p { font-size: 0.85rem; color: #7a5a10 !important; line-height: 1.7; margin: 0; }

.step-row { display: flex; align-items: flex-start; gap: 1rem; margin-bottom: 1.1rem; }
.step-num {
    min-width: 32px; height: 32px;
    background: #1a3a5c; color: #e8b84b;
    font-size: 0.85rem; font-weight: 800;
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    flex-shrink: 0;
}
.step-content { padding-top: 0.25rem; }
.step-title { font-size: 0.88rem; font-weight: 700; color: #1a3a5c; margin-bottom: 0.15rem; }
.step-desc { font-size: 0.8rem; color: #5a6e82; line-height: 1.55; }

::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: #f7f5f0; }
::-webkit-scrollbar-thumb { background: #b8d0ea; border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: #1a6cb5; }
</style>
""", unsafe_allow_html=True)

# ── HERO ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-banner">
  <div class="hero-tag">🧠 Intelligence Artificielle · Santé Mentale</div>
  <div class="hero-title">Digital Lifestyle<br><span>Benchmark 2025</span></div>
  <div class="hero-desc">
    Une application de machine learning qui analyse vos habitudes numériques et votre mode de vie
    pour évaluer votre risque de dépression — en temps réel, avec deux modèles complémentaires.
  </div>
  <div class="hero-badges">
    <span class="hero-badge">🔍 Classification binaire</span>
    <span class="hero-badge">📈 Régression continue</span>
    <span class="hero-badge">⚡ Prédiction instantanée</span>
    <span class="hero-badge">📊 16 indicateurs analysés</span>
  </div>
</div>
""", unsafe_allow_html=True)

# ── LES DEUX APPROCHES ────────────────────────────────────────────────────────
st.markdown('<div class="section-title">Les deux approches disponibles</div>', unsafe_allow_html=True)
st.write("")

col1, col2 = st.columns(2, gap="medium")
with col1:
    st.markdown("""
    <div class="approach-card">
      <div class="approach-icon">🔍</div>
      <span class="approach-label label-blue">Classification</span>
      <div class="approach-title">Risque Élevé de Dépression</div>
      <div class="approach-desc">
        Le modèle prédit si vous êtes à <strong>haut risque</strong> ou non (<code>high_risk_flag</code>).
        Résultat binaire accompagné d'une probabilité en pourcentage et d'une jauge dynamique.<br><br>
        Idéal pour une <strong>détection rapide</strong> d'un signal d'alerte.
      </div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="approach-card">
      <div class="approach-icon">📈</div>
      <span class="approach-label label-mustard">Régression</span>
      <div class="approach-title">Score Continu de Dépression</div>
      <div class="approach-desc">
        Le modèle estime un <strong>score numérique</strong> de 0 à 20 (<code>depression_score</code>).
        Trois niveaux : faible (0–5), modéré (5–10), élevé (10–20), avec recommandations adaptées.<br><br>
        Idéal pour <strong>mesurer l'intensité</strong> et suivre l'évolution dans le temps.
      </div>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# ── STATISTIQUES ──────────────────────────────────────────────────────────────
st.markdown('<div class="section-title">Ce que l\'application analyse</div>', unsafe_allow_html=True)
st.write("")

c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown('<div class="stat-card"><div class="stat-number">16</div><div class="stat-label">Indicateurs analysés</div></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="stat-card"><div class="stat-number">2</div><div class="stat-label">Modèles ML distincts</div></div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="stat-card"><div class="stat-number">0–20</div><div class="stat-label">Échelle de score</div></div>', unsafe_allow_html=True)
with c4:
    st.markdown('<div class="stat-card"><div class="stat-number">< 1s</div><div class="stat-label">Temps de prédiction</div></div>', unsafe_allow_html=True)

st.write("")

# ── COMMENT ÇA MARCHE + ASTUCES ───────────────────────────────────────────────
col_left, col_right = st.columns([1, 1], gap="large")

with col_left:
    st.markdown('<div class="section-title">Comment utiliser l\'application</div>', unsafe_allow_html=True)
    st.write("")
    st.markdown("""
    <div class="step-row">
      <div class="step-num">1</div>
      <div class="step-content">
        <div class="step-title">Choisissez une approche</div>
        <div class="step-desc">Dans le menu latéral, sélectionnez Classification (risque binaire) ou Régression (score continu) selon votre besoin.</div>
      </div>
    </div>
    <div class="step-row">
      <div class="step-num">2</div>
      <div class="step-content">
        <div class="step-title">Renseignez vos habitudes</div>
        <div class="step-desc">Remplissez le formulaire avec vos données réelles : heures d'écran, qualité du sommeil, niveau de stress, activité physique…</div>
      </div>
    </div>
    <div class="step-row">
      <div class="step-num">3</div>
      <div class="step-content">
        <div class="step-title">Lancez la prédiction</div>
        <div class="step-desc">Cliquez sur le bouton de prédiction. Le modèle traite vos données et affiche instantanément le résultat avec la jauge visuelle.</div>
      </div>
    </div>
    <div class="step-row">
      <div class="step-num">4</div>
      <div class="step-content">
        <div class="step-title">Interprétez le résultat</div>
        <div class="step-desc">Lisez l'interprétation colorée (vert / orange / rouge) et les recommandations associées à votre niveau de risque.</div>
      </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="info-box">
      <p>💡 <strong>Conseil :</strong> Pour des résultats plus précis, renseignez vos valeurs moyennes sur les 7 derniers jours, pas uniquement votre état du jour.</p>
    </div>
    """, unsafe_allow_html=True)

with col_right:
    st.markdown('<div class="section-title">Astuces pour réduire le risque</div>', unsafe_allow_html=True)
    st.write("")
    st.markdown("""
    <div class="tip-card">
      <div class="tip-title"><span class="tip-icon">📵</span>Limitez le temps d'écran le soir</div>
      <div class="tip-body">Évitez les écrans au moins 1h avant de dormir. La lumière bleue perturbe la mélatonine et dégrade la qualité du sommeil, facteur clé de dépression.</div>
    </div>
    <div class="tip-card">
      <div class="tip-title"><span class="tip-icon">🏃</span>Bougez au moins 3 fois par semaine</div>
      <div class="tip-body">30 minutes d'activité physique modérée réduisent significativement les scores d'anxiété et de stress. La marche rapide suffit.</div>
    </div>
    <div class="tip-card">
      <div class="tip-title"><span class="tip-icon">🔔</span>Désactivez les notifications non essentielles</div>
      <div class="tip-body">Chaque notification interrompt votre concentration et augmente le niveau de cortisol. Gardez uniquement les alertes vraiment importantes.</div>
    </div>
    <div class="tip-card">
      <div class="tip-title"><span class="tip-icon">😴</span>Ciblez 7 à 9 heures de sommeil</div>
      <div class="tip-body">Le manque chronique de sommeil est l'un des plus forts prédicteurs de dépression. Un horaire régulier améliore la qualité du sommeil.</div>
    </div>
    <div class="tip-card">
      <div class="tip-title"><span class="tip-icon">📱</span>Faites des pauses digitales quotidiennes</div>
      <div class="tip-body">Instituez des plages "sans écran" dans la journée (repas, promenades). Réduire la dépendance numérique améliore nettement le bonheur perçu.</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# ── AVERTISSEMENT ─────────────────────────────────────────────────────────────
st.markdown("""
<div class="warn-box">
  <p>⚠️ <strong>Avertissement :</strong> Cette application est un outil d'aide à la prise de conscience,
  pas un diagnostic médical. Les résultats sont basés sur un modèle statistique entraîné sur des données
  anonymisées. En cas de score élevé ou de détresse persistante, consultez un professionnel de santé mentale.</p>
</div>
""", unsafe_allow_html=True)

st.sidebar.success("Choisissez une page dans le menu à gauche")