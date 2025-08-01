from db_connection import get_db
from bson import ObjectId
import xml.etree.ElementTree as ET
from lxml import etree



def ajouter_evenement(collection, titre, date, lieu):
    try:
        doc = {"titre": titre, "date": date, "lieu": lieu}
        result = collection.insert_one(doc)
        print(f"Événement ajouté avec ID : {result.inserted_id}")
    except Exception as e:
        print(f"Erreur lors de l'ajout de l'événement : {e}")

def afficher_tous_evenements(collection):
    try:
        print("Tous les événements :")
        for evenement in collection.find():
            print(evenement)
    except Exception as e:
        print(f"Erreur lors de l'affichage des événements : {e}")


def supprimer_evenement(collection, id):
    try:
        result = collection.delete_many({"_id": ObjectId(id)})
        print(f"{result.deleted_count} événement(s) supprimé(s).")
    except Exception as e:
        print(f"Erreur lors de la suppression : {e}")

def valider_evenements_xml(fichier_xml):
    try:
        with open(fichier_xml, 'r') as file:
            xml_content = file.read()

        # Parse XML avec validation DTD
        parser = etree.XMLParser(dtd_validation=True)
        etree.fromstring(xml_content.encode('utf-8'), parser)
        print("Le fichier XML est valide.")
    except etree.XMLSyntaxError as e:
        print(f"Erreur de validation XML : {e}")
    except Exception as e:
        print(f"Erreur inattendue : {e}")

