from bson import ObjectId
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
categories = db["categories"]

def import_categories():
    tree = ET.parse("categories.xml")
    root = tree.getroot()

    for cat in root.findall("categorie"):
        doc = {
            "nom": cat.find("nom").text,
            "description": cat.find("description").text
        }
        categories.insert_one(doc)
    print("Importation des catégories terminée.")

# ------------------ CREATE ------------------
def ajouter_categorie(nom, description):
    doc = {"nom": nom, "description": description}
    result = categories.insert_one(doc)
    print(f"Catégorie ajoutée avec ID : {result.inserted_id}")

# ------------------ READ ------------------
def afficher_toutes_categories():
    print("Toutes les catégories :")
    for cat in categories.find():
        print(cat)

def rechercher_categorie(nom):
    print(f"Catégorie avec nom = {nom} :")
    resultats = categories.find({"nom": nom})
    for r in resultats:
        print(r)

# ------------------ UPDATE ------------------
def mettre_a_jour_description(id, nouvelle_description):
    result = categories.update_many({"_id": ObjectId(id)}, {"$set": {"description": nouvelle_description}})
    print(f"{result.modified_count} description(s) mise(s) à jour.")

# ------------------ DELETE ------------------
def supprimer_categorie(id):
    result = categories.delete_many({"_id": ObjectId(id)})
    print(f"{result.deleted_count} catégorie(s) supprimée(s).")

# ------------------ ANALYSE ------------------
def nombre_total_categories():
    total = categories.count_documents({})
    print(f"Nombre total de catégories : {total}")

afficher_toutes_categories()