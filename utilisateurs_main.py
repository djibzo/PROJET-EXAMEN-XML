from db_connection import get_db
from utilisateurs_crud_operations import *

def menu_principal():
    db = get_db()
    collection = db["utilisateurs"]

    while True:
        print("\nMenu Principal")
        print("1. Ajouter un utilisateur")
        print("2. Afficher tous les utilisateurs")
        print("3. Rechercher un utilisateur par nom")
        print("4. Mettre à jour l'email d'un utilisateur")
        print("5. Supprimer un utilisateur")
        print("6. Nombre total d'utilisateurs")
        print("7. Utilisateurs avec email groupeisi")
        print("8. Quitter")

        choix = input("Choisissez une option : ")

        if choix == "1":
            nom = input("Nom : ")
            prenom = input("Prénom : ")
            email = input("Email : ")
            ajouter_utilisateur(collection, nom, prenom, email)
        elif choix == "2":
            afficher_tous_utilisateurs(collection)
        elif choix == "3":
            nom = input("Nom à rechercher : ")
            rechercher_par_nom(collection, nom)
        elif choix == "4":
            id = input("ID de l'utilisateur : ")
            nouvel_email = input("Nouvel email : ")
            mettre_a_jour_email(collection, id, nouvel_email)
        elif choix == "5":
            id = input("ID de l'utilisateur à supprimer : ")
            supprimer_utilisateur(collection, id)
        elif choix == "6":
            nombre_total_utilisateurs(collection)
        elif choix == "7":
            utilisateurs_email_gmail(collection)
        elif choix == "8":
            print("Au revoir !")
            break
        else:
            print("Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
    menu_principal()
