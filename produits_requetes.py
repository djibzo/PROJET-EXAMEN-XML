from variable import client

db = client["projet_xml"]
collection = db["produits"]

def topProduits():
    for p in collection.find().sort("quantite_totale", -1).limit(5):
        print(p)

def produitsChers():
    for p in collection.find({"prix": {"$gt": 200000}}):
        print(p)

if __name__ == "__main__":
    topProduits()
