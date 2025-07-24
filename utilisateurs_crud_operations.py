from bson import ObjectId
import re

def valider_donnees_utilisateur(user):
    """Valide les données d'un utilisateur."""
    if not user.find("nom") or not user.find("prenom") or not user.find("email"):
        raise ValueError("Champs obligatoires manquants (nom, prenom, email).")
    
    email = user.find("email").text
    if not re.match(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
        raise ValueError(f"Email invalide : {email}")

def ajouter_utilisateur(collection, nom, prenom, email):
    try:
        doc = {"nom": nom, "prenom": prenom, "email": email}
        result = collection.insert_one(doc)
        print(f"Utilisateur ajouté avec ID : {result.inserted_id}")
        afficher_tous_utilisateurs(collection)
    except Exception as e:
        print(f"Erreur lors de l'ajout de l'utilisateur : {e}")

def afficher_tous_utilisateurs(collection):
    try:
        print("Tous les utilisateurs :")
        for user in collection.find():
            print(user)
    except Exception as e:
        print(f"Erreur lors de l'affichage des utilisateurs : {e}")

def rechercher_par_nom(collection, nom):
    try:
        print(f"Recherche de l'utilisateur avec nom = {nom} :")
        resultats = collection.find({"nom": nom})
        for r in resultats:
            print(r)
    except Exception as e:
        print(f"Erreur lors de la recherche : {e}")

def mettre_a_jour_email(collection, id, nouvel_email):
    try:
        result = collection.update_many({"_id": ObjectId(id)}, {"$set": {"email": nouvel_email}})
        print(f"{result.modified_count} document mis à jour.")
        afficher_tous_utilisateurs(collection)
    except Exception as e:
        print(f"Erreur lors de la mise à jour : {e}")

def supprimer_utilisateur(collection, id):
    try:
        result = collection.delete_many({"_id": ObjectId(id)})
        print(f"{result.deleted_count} utilisateur(s) supprimé(s).")
        afficher_tous_utilisateurs(collection)
    except Exception as e:
        print(f"Erreur lors de la suppression : {e}")

def nombre_total_utilisateurs(collection):
    total = collection.count_documents({})
    print(f"Nombre total d'utilisateurs : {total}")

def utilisateurs_email_gmail(collection):
    print("Utilisateurs avec email groupeisi :")
    resultats = collection.find({"email": {"$regex": "@groupeisi.com"}})
    for user in resultats:
        print(user)
