# utils/preprocessing.py
import pandas as pd

def prepare_input_classification(user_input):
    """
    IMPORTANT : Cette fonction doit reproduire EXACTEMENT les colonnes 
    utilisées pendant l'entraînement du modèle de classification.
    """
    feature_order = [
        'age', 'device_hours_per_day', 'phone_unlocks', 'notifications_per_day',
        'social_media_mins', 'study_mins', 'physical_activity_days', 'sleep_hours',
        'sleep_quality', 'anxiety_score', 'depression_score', 'stress_level',
        'happiness_score', 'focus_score', 'digital_dependence_score', 'productivity_score',
        
        # Colonnes encodées (Label Encoding)
        'gender_encoded', 'region_encoded', 'income_level_encoded',
        'education_level_encoded', 'daily_role_encoded', 'device_type_encoded',
        
        # Colonnes One-Hot (get_dummies)
        'gender_Male',
        'region_Asia', 'region_Europe', 'region_Middle East', 'region_North America', 'region_South America',
        'income_level_Low', 'income_level_Lower-Mid', 'income_level_Upper-Mid',
        'education_level_High School', 'education_level_Master', 'education_level_PhD',
        'daily_role_Full-time Employee', 'daily_role_Part-time/Shift', 
        'daily_role_Student', 'daily_role_Unemployed_Looking',
        'device_type_Laptop', 'device_type_Tablet', 'device_type_iPhone'
    ]

    # Créer le DataFrame avec les valeurs fournies
    data = {k: [v] for k, v in user_input.items()}
    df = pd.DataFrame(data)

    # Ajouter toutes les colonnes manquantes avec la valeur 0
    for col in feature_order:
        if col not in df.columns:
            df[col] = 0

    # Réordonner les colonnes exactement comme pendant l'entraînement
    return df[feature_order]


def prepare_input_regression(user_input):
    """Préparation pour la régression (déjà fonctionnelle)"""
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