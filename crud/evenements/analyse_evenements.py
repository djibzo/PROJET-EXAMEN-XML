from db_connection import get_db
from bson import ObjectId



db = get_db()
collection = db["evenements"]
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
