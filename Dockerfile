# Choisir une image Python de base
FROM python:3.8-slim

# Mettre à jour et installer des dépendances nécessaires
RUN apt-get update && apt-get install -y \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Créer un dossier de travail dans le conteneur
WORKDIR /app

# Copier le fichier requirements.txt dans le conteneur
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le contenu du projet dans le conteneur
COPY . .

# Exposer le port sur lequel l'application s'exécutera (si nécessaire)
EXPOSE 5000

# Définir la commande d'exécution (par exemple, lancer un script Python)
CMD ["python", "app.py"]
