import xml.etree.ElementTree as ET
from pymongo import MongoClient
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from variable import uri, client, commandesFile


try:
    client = MongoClient(uri)
    db = client["projet_xml"]  # nom de la base
    print("Connexion a la base MongoDB, reussie!")
except Exception as e:
    print(e)


def sendToMongoCommandesElements(fileName, commandesCollection):
    tree = ET.parse(fileName)
    root = tree.getroot()
    for commande in root.findall('commande'):
        id_commande = int(commande.find('id').text)
        date = commande.find('date').text

        # Extraire les infos client
        client_elem = commande.find('client')
        nom_client = client_elem.find('nom').text
        email_client = client_elem.find('email').text

        # Extraire les produits
        produits = []
        for produit in commande.find('produits').findall('produit'):
            produits.append({
                "nom": produit.find('nom').text,
                "quantite": int(produit.find('quantite').text),
                "prix": int(produit.find('prix').text)
            })

        # Structure du document à insérer
        ligne = {
            "id": id_commande,
            "date": date,
            "client": {
                "nom": nom_client,
                "email": email_client
            },
            "produits": produits
        }

        commandesCollection.insert_one(ligne)

    print("Importation des commandes réussie !")


# Exportation des données XML vers MongoDB
sendToMongoCommandesElements(commandesFile, db["commandes"])


# # CRUD Operations

# Récupération de la collection "commandes"
commandesCollection = db["commandes"]

nouvelle_commande = {
        "id": 60,
        "date": "2025-07-17",
        "client": {
            "nom": "Ousmane Sarr",
            "email": "ousmane.sarr@example.com"
        },
        "produits": [
            {"nom": "Imprimante", "quantite": 1, "prix": 120000}
        ]
    }

def addCommande(nouvelle_commande, commandesCollection):
    # 1. CREATE – Ajouter une nouvelle commande
    commandesCollection.insert_one(nouvelle_commande)
    print("Commande ajoutée avec succès !")

def getCommandes(commandesCollection):
    # READ – Lire toutes les commandes
    for commande in commandesCollection.find():
        print(commande)

valeur_a_modifier = {"client.nom": "Fatou NDOYE", "client.email": "fatou.ndoye@exemple.com"}

def UpdateCommande(id_commande, nouvelle_valeur, commandesCollection):
    # UPDATE – Modifier un champ (ex: changer le nom du client avec id = 1)
    commandesCollection.update_one(
        {"id": id_commande},
        {"$set": nouvelle_valeur}
    )
    print("Commande mise à jour avec succès !")

def deleteCommande(id_commande, commandesCollection):
    # DELETE – Supprimer une commande (ex: avec id = 2)
    suppr = commandesCollection.delete_one({"id": id_commande})
    print("Commande supprimée avec succès!")



