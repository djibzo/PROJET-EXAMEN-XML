import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from db_connection import get_db
from bson import ObjectId
import xml.etree.ElementTree as ET
from pymongo import MongoClient


db = get_db()
collection = db["utilisateurs"]

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


