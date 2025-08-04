from db_connection import get_db
from bson import ObjectId
import xml.etree.ElementTree as ET
from lxml import etree


db = get_db()
collection = db["produits"]

def addProduit(produit):
    collection.insert_one(produit)

def getProduits():
    for p in collection.find():
        print(p)

def updateProduit(nom, new_values):
    collection.update_one({"nom": nom}, {"$set": new_values})

def deleteProduit(nom):
    collection.delete_one({"nom": nom})

