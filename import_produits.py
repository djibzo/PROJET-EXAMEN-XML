import xml.etree.ElementTree as ET
from variable import client, commandesFile

db = client["projet_xml"]
produits_collection = db["produits"]

def extractProduits():
    produits_map = {}

    tree = ET.parse(commandesFile)
    root = tree.getroot()

    for commande in root.findall("commande"):
        for produit in commande.find("produits").findall("produit"):
            nom = produit.find("nom").text
            quantite = int(produit.find("quantite").text)
            prix = int(produit.find("prix").text)

            if nom in produits_map:
                produits_map[nom]["quantite_totale"] += quantite
            else:
                produits_map[nom] = {
                    "nom": nom,
                    "quantite_totale": quantite,
                    "prix": prix
                }

    produits_collection.delete_many({})
    for prod in produits_map.values():
        produits_collection.insert_one(prod)

    print("✅ Produits importés avec succès.")

extractProduits()
