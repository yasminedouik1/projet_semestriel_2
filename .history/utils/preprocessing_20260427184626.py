# utils/preprocessing.py
import pandas as pd

def prepare_input_regression(user_input):
    """
    Prépare les données pour le modèle de régression (23 features)
    user_input : dict contenant les valeurs saisies
    """
    feature_order = [
        'device_hours_per_day', 'phone_unlocks', 'digital_dependence_score',
        'sleep_quality', 'anxiety_score', 'sleep_hours', 'happiness_score',
        'high_risk_flag', 'stress_level', 'focus_score', 'social_media_mins',
        'daily_role_Unemployed_Looking', 'productivity_score', 'study_mins',
        'notifications_per_day', 'physical_activity_days', 'education_level_encoded',
        'region_Europe', 'device_type_Tablet', 'region_Asia', 'income_level_Low',
        'device_type_Laptop', 'daily_role_Part-time/Shift'
    ]

    # Créer le DataFrame avec les valeurs de l'utilisateur
    data = {k: [v] for k, v in user_input.items()}
    df = pd.DataFrame(data)

    # Ajouter les colonnes manquantes à 0
    for col in feature_order:
        if col not in df.columns:
            df[col] = 0

    # Réordonner exactement comme pendant l'entraînement
    return df[feature_order]


def prepare_input_classification(user_input):
    """À compléter plus tard selon tes 18 features de classification"""
    # Pour l'instant version minimale
    data = {
        'device_hours_per_day': [user_input.get('device_hours', 7.0)],
        'phone_unlocks': [user_input.get('phone_unlocks', 150)],
        'digital_dependence_score': [user_input.get('digital_dependence', 35.0)],
        # Ajoute ici les autres features importantes de la classification
    }
    df = pd.DataFrame(data)
    return df