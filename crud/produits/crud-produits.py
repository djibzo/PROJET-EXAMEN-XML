from variable import client

db = client["projet_xml"]
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

