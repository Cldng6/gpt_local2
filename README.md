# Documentation
## Premier commit
    git init
    git config --global init.defaultBranch main
    git remote add origin git@github.com:Cldng6/gpt_local2.git
    git add .
    git config user.email "mail"
    git commit -m "first commit"
    git push --set-upstream origin master



# Construire l'image Docker
    docker build -t gpt-container .

    ## installation docker s'il n'est pas installé.
        La commande « docker » n'a pas été trouvée, mais peut être installée avec :
        sudo snap install docker         # version 24.0.5, or
        sudo apt  install docker.io      # version 24.0.7-0ubuntu4.1
        sudo apt  install podman-docker  # version 4.9.3+ds1-1ubuntu0.2
        Voir « snap info docker » pour des versions additionelles.

# Reconstruire l'image Docker (Podman)
    podman build -t gpt-container .

# Relancez votre conteneur avec la nouvelle image :
    podman run -p 5000:5000 localhost/gpt-container

# Vérification de l'installation des bibliothèques dans le conteneur
    podman exec -it <container_id> /bin/bash

# Vérifiez que transformers est installé en exécutant la commande suivante à l'intérieur du conteneur :
    pip show transformers
        Si la bibliothèque est correctement installée, vous devriez voir des informations sur la version de transformers.
## Si ce n'est pas le cas, vous pouvez essayer de l'installer manuellement à l'intérieur du conteneur :    

    pip install transformers
        Logs et erreurs d'installation

        Si l'installation échoue ou si vous ne voyez toujours pas les bibliothèques après avoir reconstruire l'image, vous pouvez examiner les logs d'installation pour voir si des erreurs se produisent lors de l'installation des dépendances.

# Créer un environnement virtuel (si ce n'est pas déjà fait).
    python3 -m venv /app/venv

# Activer l'environnement virtuel.
    source venv/bin/activate  # Sur Linux/macOS
    venv\Scripts\activate     # Sur Windows

# Réinstaller les dépendances dans cet environnement.
    pip install -r requirements.txt

# Vérification de l'installation
    pip show transformers
    pip show torch

























# Vérification de l'exécution du conteneur avec Podman
    podman run -p 5000:5000 localhost/gpt-container



# Étape 2 : Lancer le conteneur Docker
    docker run -p 5000:5000 gpt-container

# Tester l'API
    curl -X POST http://localhost:5000/generate \
    -H "Content-Type: application/json" \
    -d '{"text": "Il était une fois"}'

        ## installer s'il n'est pas installé.
        La commande « curl » n'a pas été trouvée, mais peut être installée avec :
        sudo snap install curl  # version 8.1.2, or
        sudo apt  install curl  # version 8.5.0-2ubuntu10.4
        Voir « snap info curl » pour des versions additionelles.

# Nettoyage et gestion des conteneurs
        Si vous avez terminé et souhaitez arrêter votre conteneur, vous pouvez le faire avec :

        docker stop <container_id>

        Pour supprimer l'image Docker (si vous n'en avez plus besoin) :

        docker rmi gpt-container

# Conclusion
        Vous avez maintenant une structure Docker complète pour exécuter un modèle GPT-2 localement avec Flask. Vous pouvez ajuster le modèle pour utiliser d'autres versions comme GPT-3 (via l'API d'OpenAI) ou GPT-Neo pour un modèle plus puissant, ou encore ajouter des fonctionnalités supplémentaires à votre application.

# Package===
    apt install python3-pip
    apt install python3.12-venv# gpt_local
