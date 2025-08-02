import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from db_connection import get_db
from bson import ObjectId
import xml.etree.ElementTree as ET
from pymongo import MongoClient


db = get_db()
categories = db["categories"]

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