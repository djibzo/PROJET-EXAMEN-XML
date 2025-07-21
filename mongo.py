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
collection = db["utilisateurs"]

def import_utilisateurs():
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
# ------------------ CREATE ------------------
def ajouter_utilisateur(nom, prenom, email):
    doc = {"nom": nom, "prenom": prenom, "email": email}
    result = collection.insert_one(doc)
    print(f"Utilisateur ajouté avec ID : {result.inserted_id}")


# ------------------ READ ------------------
def afficher_tous_utilisateurs():
    print("Tous les utilisateurs :")
    for user in collection.find():
        print(user)


def rechercher_par_nom(nom):
    print(f"Recherche de l'utilisateur avec nom = {nom} :")
    resultats = collection.find({"nom": nom})
    for r in resultats:
        print(r)


# ------------------ UPDATE ------------------
def mettre_a_jour_email(id, nouvel_email):
    result = collection.update_many({"_id": ObjectId(id)}, {"$set": {"email": nouvel_email}})
    print(f"{result.modified_count} document mis à jour.")


# ------------------ DELETE ------------------
def supprimer_utilisateur(id):
    result = collection.delete_many({"_id": ObjectId(id)})
    print(f"{result.deleted_count} utilisateur(s) supprimé(s).")


# ------------------ ANALYSE / REQUÊTES ------------------
def nombre_total_utilisateurs():
    total = collection.count_documents({})
    print(f"Nombre total d'utilisateurs : {total}")


def utilisateurs_email_gmail():
    print("Utilisateurs avec email groupeisi :")
    resultats = collection.find({"email": {"$regex": "@groupeisi.com"}})
    for user in resultats:
        print(user)

#supprimer_utilisateur('687e667aeb41b979938d7576')
#ajouter_utilisateur("Fall","Djibril","djibrilf@groupeisi.com")
afficher_tous_utilisateurs()