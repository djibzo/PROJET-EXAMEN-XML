import xml.etree.ElementTree as ET
from variable import client

def export_produits_to_xml(filename="produits.xml"):
    db = client["projet_xml"]
    collection = db["produits"]
    root = ET.Element("produits")
    for produit in collection.find():
        produit_elem = ET.SubElement(root, "produit")
        nom_elem = ET.SubElement(produit_elem, "nom")
        nom_elem.text = produit["nom"]
        quantite_elem = ET.SubElement(produit_elem, "quantite_totale")
        quantite_elem.text = str(produit["quantite_totale"])
        prix_elem = ET.SubElement(produit_elem, "prix")
        prix_elem.text = str(produit["prix"])
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)

    print(f"Export XML terminé : '{filename}' a été généré avec succès.")

# Exécution directe
if __name__ == "__main__":
    export_produits_to_xml()
