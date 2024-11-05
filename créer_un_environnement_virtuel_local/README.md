# Préparer les dépendances dans votre environnement local (si besoin) :
    python -m venv venv

# Activer l'environnement virtuel. 
## Sur Linux/macOS
    source venv/bin/activate

## Sur Windows
    venv\Scripts\activate

# Installez les dépendances localement :
    pip install flask transformers torch

# Exportez les dépendances vers requirements.txt
    pip freeze > requirements.txt


# Construire l'image Docker (Podman)

## Si vous utilisez Docker Compose
    docker-compose build

## Si vous utilisez Podman Compose
    podman-compose build


# Lancer le conteneur Docker (Podman)
        Une fois l'image construite, vous pouvez lancer le conteneur :

## Pour démarrer le conteneur avec Docker
    docker-compose up  

## Pour démarrer le conteneur avec Podman
    podman-compose up

        Cela lancera votre application Flask à l'intérieur du conteneur, où toutes les dépendances seront isolées, et l'application sera accessible via http://localhost:5000.