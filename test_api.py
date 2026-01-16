import requests

url = "http://127.0.0.1:5000/predict"

data = {
    'Age': 42.0,
    'Account_Manager': 1,
    'Years': 5.5,
    'Num_Sites': 12
}

# On envoie la requête POST
response = requests.post(url, data=data)

# On affiche le résultat JSON reçu
if response.status_code == 200:
    print("Résultat de la prédiction :", response.json())
else:
    print(f"Erreur {response.status_code} :", response.text)