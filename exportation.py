from bson import ObjectId
from datetime import datetime
import xml.etree.ElementTree as ET
from db_connection import get_db

db = get_db()
def import_utilisateurs():
    collection = db["utilisateurs"]
    # Parse XML
    tree = ET.parse("utilisateurs.xml")
    root = tree.getroot()

    # Insérer dans MongoDB
    for user in root.findall("utilisateur"):
        doc = {
            "nom": user.find("nom").text,
            "prenom": user.find("prenom").text,
            "email": user.find("email").text
        }
        collection.insert_one(doc)

    print("Importation terminée ")