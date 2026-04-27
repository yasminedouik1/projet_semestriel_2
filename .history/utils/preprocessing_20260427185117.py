# utils/preprocessing.py
import pandas as pd

def prepare_input_regression(user_input):
    """Prépare les données pour le modèle de régression (23 features)"""
    feature_order = [
        'device_hours_per_day', 'phone_unlocks', 'digital_dependence_score',
        'sleep_quality', 'anxiety_score', 'sleep_hours', 'happiness_score',
        'high_risk_flag', 'stress_level', 'focus_score', 'social_media_mins',
        'daily_role_Unemployed_Looking', 'productivity_score', 'study_mins',
        'notifications_per_day', 'physical_activity_days', 'education_level_encoded',
        'region_Europe', 'device_type_Tablet', 'region_Asia', 'income_level_Low',
        'device_type_Laptop', 'daily_role_Part-time/Shift'
    ]

    data = {k: [v] for k, v in user_input.items()}
    df = pd.DataFrame(data)

    for col in feature_order:
        if col not in df.columns:
            df[col] = 0

    return df[feature_order]


def prepare_input_classification(user_input):
    """Prépare les données pour le modèle de classification"""
    # Liste des features importantes pour la classification (à adapter selon ton feature selection)
    feature_order = [
        'device_hours_per_day', 'phone_unlocks', 'digital_dependence_score',
        'anxiety_score', 'stress_level', 'sleep_hours', 'sleep_quality',
        'happiness_score', 'focus_score', 'notifications_per_day',
        # Ajoute ici les autres features que tu as gardées dans le feature selection classification
    ]

    data = {k: [v] for k, v in user_input.items()}
    df = pd.DataFrame(data)

    for col in feature_order:
        if col not in df.columns:
            df[col] = 0

    return df[feature_order]