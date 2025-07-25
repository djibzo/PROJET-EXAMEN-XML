from db_connection import get_db
from crud_evenements import *

def menu_evenements():
    db = get_db()
    collection = db["evenements"]

    while True:
        print("\nMenu Gestion des Événements")
        print("1. Importer les événements depuis XML")
        print("2. Ajouter un événement")
        print("3. Afficher tous les événements")
        print("4. Rechercher un événement par titre")
        print("5. Mettre à jour le lieu d'un événement")
        print("6. Supprimer un événement")
        print("7. Quitter")

        choix = input("Choisissez une option : ")

        if choix == "1":
            fichier_xml = input("Entrez le chemin du fichier XML : ")
            importer_evenements(collection, fichier_xml)
        elif choix == "2":
            titre = input("Titre : ")
            date = input("Date (YYYY-MM-DD) : ")
            lieu = input("Lieu : ")
            ajouter_evenement(collection, titre, date, lieu)
        elif choix == "3":
            afficher_tous_evenements(collection)
        elif choix == "4":
            titre = input("Titre à rechercher : ")
            rechercher_evenement_par_titre(collection, titre)
        elif choix == "5":
            id = input("ID de l'événement : ")
            nouveau_lieu = input("Nouveau lieu : ")
            mettre_a_jour_lieu_evenement(collection, id, nouveau_lieu)
        elif choix == "6":
            id = input("ID de l'événement à supprimer : ")
            supprimer_evenement(collection, id)
        elif choix == "7":
            print("Au revoir !")
            break
        else:
            print("Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
    menu_evenements()


