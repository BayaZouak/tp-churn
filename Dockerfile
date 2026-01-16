# Utilisation d'une image Python ultra-légère
FROM python:3.12-slim

# Définition du dossier de travail
WORKDIR /app

# Installation des dépendances en premier (optimisation du cache)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie sélective des fichiers nécessaires uniquement
COPY app.py .
COPY data/ ./data/
COPY templates/ ./templates/
COPY tests tests

# Information sur le port utilisé par l'application
EXPOSE 5000

# Commande de lancement
CMD ["python", "app.py"]