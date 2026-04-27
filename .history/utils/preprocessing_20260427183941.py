import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib

# Charge le scaler si tu en as un
scaler = joblib.load("models/scaler.pkl")  # optionnel

def prepare_input_classification(...):
    data = {
        'device_hours_per_day': [device_hours],
        'phone_unlocks': [phone_unlocks],
        'digital_dependence_score': [digital_dependence],
        # ... tous les features utilisés dans le modèle final (18 features pour classification)
        # N'oublie pas les variables one-hot si tu en as (gender_Male, etc.)
    }
    df = pd.DataFrame(data)
    
    # Applique le même encoding / scaling que dans tes notebooks
    # Exemple : si tu as fait get_dummies, il faut recréer les colonnes manquantes à 0
    
    return df