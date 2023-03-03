# On importe flask
from flask import Flask
# On déclare l'app Flask
app = Flask(__name__)

# On déclare la route et la fonction index
# La fonction index lit et retourne le contenu d'un fichier
@app.route('/')
def index():
    with open('file.txt', 'r') as file:
        content = file.read()
    return content

# On lance l'application
if __name__ == "__main__":
    app.run()




