from pymongo import MongoClient
from pymongo.server_api import ServerApi
from pymongo.errors import ConnectionFailure

# Connexion MongoDB
uri = "mongodb+srv://djibrilf:rhmAtMmw8z1xHJG5@cluster0.f6wb0nc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Creer un nouveau client
client = MongoClient(uri, server_api=ServerApi('1'))

commandesFile = "xml/commandes.xml"