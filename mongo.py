import xml.etree.ElementTree as ET
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from pymongo.errors import ConnectionFailure
# Connexion MongoDB
uri = "mongodb+srv://djibrilf:rhmAtMmw8z1xHJG5@cluster0.f6wb0nc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Creer un nouveau client
client = MongoClient(uri, server_api=ServerApi('1'))
try:
    client.admin.command('ping')
    print("SUCCES")
except ConnectionFailure as e:
    print(f"Echec : {e}")

db = client["projet_xml"]
collection = db["utilisateurs"]


# Parse XML
tree = ET.parse("utilisateurs.xml")
root = tree.getroot()

# Insérer dans MongoDB
for user in root.findall("utilisateur"):
    doc = {
        "id": int(user.find("id").text),
        "nom": user.find("nom").text,
        "prenom": user.find("prenom").text,
        "email": user.find("email").text
    }
    collection.insert_one(doc)

print("Importation terminée ")
