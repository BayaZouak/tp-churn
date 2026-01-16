import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib

# charger les données
data = pd.read_csv('data/train_data.csv')
 
X = data[['Age', 'Account_Manager', 'Years', 'Num_Sites']]
 
y = data['Churn']
 
model = LogisticRegression(max_iter=1000)
model.fit(X, y)

# Sauvegarder le modèle avec joblib
joblib.dump( model, 'data/churn_model_clean.pkl')
print("Modèle de régression logistique entrainé et sauvegardé")
