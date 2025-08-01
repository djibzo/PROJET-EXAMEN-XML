from bson import ObjectId
from datetime import datetime
import xml.etree.ElementTree as ET
from db_connection import get_db

db = get_db()
def import_utilisateurs():  
    collection = db["utilisateurs"]
    # Parse XML
    tree = ET.parse("utilisateurs.xml")
    root = tree.getroot()

    # Insérer dans MongoDB
    for user in root.findall("utilisateur"):
        doc = {
            "nom": user.find("nom").text,
            "prenom": user.find("prenom").text,
            "email": user.find("email").text
        }
        collection.insert_one(doc)

    print("Importation terminée ")
    
    
# evenements
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

def exporter_evenements(collection, fichier_xml):
    try:
        # Récupérer tous les événements
        evenements = collection.find()

        # Créer l'arbre XML
        root = ET.Element("evenements")
        for evenement in evenements:
            elem = ET.SubElement(root, "evenement")
            ET.SubElement(elem, "id").text = str(evenement["_id"])
            ET.SubElement(elem, "titre").text = evenement["titre"]
            ET.SubElement(elem, "date").text = evenement["date"]
            ET.SubElement(elem, "lieu").text = evenement["lieu"]

        # Écrire dans le fichier XML
        tree = ET.ElementTree(root)
        tree.write(fichier_xml, encoding='utf-8', xml_declaration=True)
        print("Exportation des événements terminée.")
    except Exception as e:
        print(f"Erreur lors de l'exportation : {e}")
        