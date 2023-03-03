#On récupère l'image python alpine
FROM python:3.9-alpine
#On se place dans le dossier app
WORKDIR /app
#On copie tous les fichiers dans le dossier app
COPY . /app
#On installe les dépendances en enlevant le cache
RUN pip install --no-cache-dir -r requirements.txt
#On déclare l'environement Flask avec le fichier app.py
ENV FLASK_APP=app.py
#On expose le port 5000 du conteneur
EXPOSE 5000
#On exécute la commande qui lance l'app Flask
CMD ["flask", "run", "--host=0.0.0.0"]

