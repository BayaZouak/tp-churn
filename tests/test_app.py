import pytest
import sys
import os

# Ajoute le dossier parent au chemin de recherche pour trouver app.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app 

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    """Vérifie que la page d'accueil s'affiche (code 200)."""
    response = client.get('/')
    assert response.status_code == 200

def test_predict_route(client):
    """Vérifie que l'envoi de données au formulaire retourne un JSON de prédiction."""
    data = {
        'Age': '45',
        'Account_Manager': '0',
        'Years': '10',
        'Num_Sites': '5'
    }
    response = client.post('/predict', data=data)
    assert response.status_code == 200
    
    json_res = response.get_json()
    assert 'churn_prediction' in json_res
    assert json_res['churn_prediction'] in [0, 1]