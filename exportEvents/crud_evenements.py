from db_connection import get_db
from bson import ObjectId
import xml.etree.ElementTree as ET
from lxml import etree


def importer_evenements(collection, fichier_xml):
    try:
        # Parse XML
        tree = ET.parse(fichier_xml)
        root = tree.getroot()

        # Insérer dans MongoDB
        for evenement in root.findall("evenement"):
            doc = {
                "id": evenement.find("id").text,
                "titre": evenement.find("titre").text,
                "date": evenement.find("date").text,
                "lieu": evenement.find("lieu").text
            }
            collection.insert_one(doc)

        print("Importation des événements terminée.")
    except ET.ParseError:
        print("Erreur : Le fichier XML est mal formé.")
    except Exception as e:
        print(f"Erreur inattendue : {e}")


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

def rechercher_evenement_par_titre(collection, titre):
    try:
        print(f"Recherche de l'événement avec titre = {titre} :")
        resultats = collection.find({"titre": titre})
        for r in resultats:
            print(r)
    except Exception as e:
        print(f"Erreur lors de la recherche : {e}")

def mettre_a_jour_lieu_evenement(collection, id, nouveau_lieu):
    try:
        result = collection.update_many({"_id": ObjectId(id)}, {"$set": {"lieu": nouveau_lieu}})
        print(f"{result.modified_count} document(s) mis à jour.")
    except Exception as e:
        print(f"Erreur lors de la mise à jour : {e}")

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

