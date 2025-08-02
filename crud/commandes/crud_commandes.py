import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from db_connection import get_db
import xml.etree.ElementTree as ET


# # CRUD Operations

# Récupération de la collection "commandes"
db = get_db()
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
