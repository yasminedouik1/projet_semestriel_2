import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pandas as pd

def plot_feature_importance(model, feature_names, top_n=15):
    """Affiche l'importance des features pour un modèle tree-based"""
    if hasattr(model, 'feature_importances_'):
        importances = model.feature_importances_
    elif hasattr(model, 'named_steps') and hasattr(model.named_steps['model'], 'feature_importances_'):
        importances = model.named_steps['model'].feature_importances_
    else:
        st.warning("Ce modèle ne supporte pas l'importance des features.")
        return None
    
    feat_imp = pd.DataFrame({
        'Feature': feature_names,
        'Importance': importances
    }).sort_values('Importance', ascending=False).head(top_n)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=feat_imp, x='Importance', y='Feature', palette='viridis', ax=ax)
    ax.set_title(f'Top {top_n} Features les plus importantes')
    plt.tight_layout()
    return fig


def plot_prediction_distribution(y_true=None, y_pred=None):
    """Compare distribution réelle vs prédite (si données disponibles)"""
    fig = plt.figure(figsize=(10, 6))
    if y_true is not None:
        sns.kdeplot(y_true, label='Réel', fill=True, alpha=0.5)
    if y_pred is not None:
        sns.kdeplot(y_pred, label='Prédit', fill=True, alpha=0.5)
    plt.title("Distribution des Scores de Dépression")
    plt.xlabel("Score de Dépression")
    plt.legend()
    return fig


def create_gauge_chart(value, title="Score"):
    """Gauge plotly pour un score unique"""
    import plotly.graph_objects as go
    
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=value,
        title={'text': title},
        gauge={
            'axis': {'range': [0, 20]},
            'bar': {'color': "#1f77b4"},
            'steps': [
                {'range': [0, 5], 'color': "#90EE90"},
                {'range': [5, 10], 'color': "#FFD700"},
                {'range': [10, 20], 'color': "#FF4500"}
            ]
        }
    ))
    return fig