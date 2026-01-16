import os
import joblib
from sklearn.linear_model import LogisticRegression

def test_model_creation():
    # Vérifier si le fichier du modèle existe après l'exécution de train.py
    model_path = 'data/churn_model_clean.pkl'
    assert os.path.exists(model_path), "Le fichier du modèle .pkl est introuvable."

def test_model_type():
    # Vérifier que l'objet sauvegardé est bien une Régression Logistique
    model = joblib.load('data/churn_model_clean.pkl')
    assert isinstance(model, LogisticRegression), "Le modèle chargé n'est pas une LogisticRegression."

def test_model_prediction_shape():
    # Vérifier que le modèle accepte le bon nombre de features (4)
    model = joblib.load('data/churn_model_clean.pkl')
    sample_data = [[30, 1, 5, 10]] # Age, Account_Manager, Years, Num_Sites
    prediction = model.predict(sample_data)
    assert len(prediction) == 1
    assert prediction[0] in [0, 1]