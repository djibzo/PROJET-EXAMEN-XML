from pymongo import MongoClient
from pymongo.server_api import ServerApi
from pymongo.errors import ConnectionFailure

# Connexion MongoDB
uri = "mongodb+srv://djibrilf:rhmAtMmw8z1xHJG5@cluster0.f6wb0nc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Fonction pour obtenir la connexion à la base de données
def get_db():
    client = MongoClient(uri, server_api=ServerApi('1'))
    try:
        client.admin.command('ping')
        print("Connexion à MongoDB réussie")
    except ConnectionFailure as e:
        print(f"Echec de connexion : {e}")
        raise
    return client["projet_xml"]
