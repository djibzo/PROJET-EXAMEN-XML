import sys

# Importations CRUD
from crud.utilisateur import crud_utilisateurs
from crud.utilisateur import analyse_utilisateurs
from crud.commandes import crud_commandes
from crud.categories import crud_categories, analyse_categories
from crud.produits import crud_produits
from crud.evenements import crud_evenements, analyse_evenements

def menu_utilisateurs():
    while True:
        print("\n--- Menu Utilisateurs ---")
        print("1. Ajouter un utilisateur")
        print("2. Afficher tous les utilisateurs")
        print("3. Rechercher par nom")
        print("4. Mettre à jour l'email")
        print("5. Supprimer un utilisateur")
        print("6. Analyse")
        print("7. Retour")
        choix = input("Votre choix: ")
        if choix == "1":
            nom = input("Nom: ")
            prenom = input("Prénom: ")
            email = input("Email: ")
            crud_utilisateurs.ajouter_utilisateur(nom, prenom, email)
        elif choix == "2":
            crud_utilisateurs.afficher_tous_utilisateurs()
        elif choix == "3":
            nom = input("Nom à rechercher: ")
            crud_utilisateurs.rechercher_par_nom(nom)
        elif choix == "4":
            id = input("ID utilisateur: ")
            email = input("Nouvel email: ")
            crud_utilisateurs.mettre_a_jour_email(id, email)
        elif choix == "5":
            id = input("ID utilisateur à supprimer: ")
            crud_utilisateurs.supprimer_utilisateur(id)
        elif choix == "6":
            print("\n--- Analyse Utilisateurs ---")
            print("1. Nombre total d'utilisateurs")
            print("2. Retour")
            choix_analyse = input("Votre choix: ")
            if choix_analyse == "1":
                analyse_utilisateurs.nombre_total_utilisateurs()
            elif choix_analyse == "2":
                continue
            else:
                print("Choix invalide.")
        elif choix == "7":
            break
        else:
            print("Choix invalide.")

def menu_produits():
    while True:
        print("\n--- Menu Produits ---")
        print("1. Ajouter un produit")
        print("2. Afficher tous les produits")
        print("3. Mettre à jour un produit")
        print("4. Supprimer un produit")
        print("5. Retour")
        choix = input("Votre choix: ")
        if choix == "1":
            nom = input("Nom: ")
            prix = float(input("Prix: "))
            quantite = int(input("Quantité: "))
            produit = {"nom": nom, "prix": prix, "quantite": quantite}
            crud_produits.addProduit(produit)
        elif choix == "2":
            crud_produits.getProduits()
        elif choix == "3":
            nom = input("Nom du produit à modifier: ")
            champ = input("Champ à modifier (prix/quantite): ")
            valeur = input("Nouvelle valeur: ")
            new_values = {champ: float(valeur) if champ == "prix" else int(valeur)}
            crud_produits.updateProduit(nom, new_values)
        elif choix == "4":
            nom = input("Nom du produit à supprimer: ")
            crud_produits.deleteProduit(nom)
        elif choix == "5":
            break
        else:
            print("Choix invalide.")

def menu_categories():
    while True:
        print("\n--- Menu Catégories ---")
        print("1. Ajouter une catégorie")
        print("2. Afficher toutes les catégories")
        print("3. Rechercher une catégorie")
        print("4. Mettre à jour la description")
        print("5. Supprimer une catégorie")
        print("6. Analyse")
        print("7. Retour")
        choix = input("Votre choix: ")
        if choix == "1":
            nom = input("Nom: ")
            description = input("Description: ")
            crud_categories.ajouter_categorie(nom, description)
        elif choix == "2":
            crud_categories.afficher_toutes_categories()
        elif choix == "3":
            nom = input("Nom à rechercher: ")
            crud_categories.rechercher_categorie(nom)
        elif choix == "4":
            id = input("ID catégorie: ")
            description = input("Nouvelle description: ")
            crud_categories.mettre_a_jour_description(id, description)
        elif choix == "5":
            id = input("ID catégorie à supprimer: ")
            crud_categories.supprimer_categorie(id)
        elif choix == "6":
            print("\n--- Analyse Catégories ---")
            print("1. Nombre total de catégories")
            print("2. Retour")
            choix_analyse = input("Votre choix: ")
            if choix_analyse == "1":
                analyse_categories.nombre_total_categories()
            elif choix_analyse == "2":
                continue
            else:
                print("Choix invalide.")
        elif choix == "7":
            break
        else:
            print("Choix invalide.")

def menu_commandes():
    while True:
        print("\n--- Menu Commandes ---")
        print("1. Ajouter une commande")
        print("2. Afficher toutes les commandes")
        print("3. Mettre à jour une commande")
        print("4. Supprimer une commande")
        print("5. Retour")
        choix = input("Votre choix: ")
        if choix == "1":
            print("Ajout d'une commande non implémenté dans ce menu.")
        elif choix == "2":
            crud_commandes.getCommandes(crud_commandes.commandesCollection)
        elif choix == "3":
            id_commande = int(input("ID de la commande à modifier: "))
            champ = input("Champ à modifier (ex: client.nom): ")
            valeur = input("Nouvelle valeur: ")
            nouvelle_valeur = {champ: valeur}
            crud_commandes.UpdateCommande(id_commande, nouvelle_valeur, crud_commandes.commandesCollection)
        elif choix == "4":
            id_commande = int(input("ID de la commande à supprimer: "))
            crud_commandes.deleteCommande(id_commande, crud_commandes.commandesCollection)
        elif choix == "5":
            break
        else:
            print("Choix invalide.")

def menu_evenements():
    db = __import__('db_connection').get_db()
    collection = db["evenements"]
    while True:
        print("\n--- Menu Événements ---")
        print("1. Ajouter un événement")
        print("2. Afficher tous les événements")
        print("3. Supprimer un événement")
        print("4. Analyse")
        print("5. Retour")
        choix = input("Votre choix: ")
        if choix == "1":
            titre = input("Titre: ")
            date = input("Date: ")
            lieu = input("Lieu: ")
            crud_evenements.ajouter_evenement(collection, titre, date, lieu)
        elif choix == "2":
            crud_evenements.afficher_tous_evenements(collection)
        elif choix == "3":
            id = input("ID de l'événement à supprimer: ")
            crud_evenements.supprimer_evenement(collection, id)
        elif choix == "4":
            print("\n--- Analyse Événements ---")
            print("1. Rechercher un événement par titre")
            print("2. Mettre à jour le lieu d'un événement")
            print("3. Retour")
            choix_analyse = input("Votre choix: ")
            if choix_analyse == "1":
                titre = input("Titre à rechercher : ")
                analyse_evenements.rechercher_evenement_par_titre(collection, titre)
            elif choix_analyse == "2":
                id = input("ID de l'événement : ")
                lieu = input("Nouveau lieu : ")
                analyse_evenements.mettre_a_jour_lieu_evenement(collection, id, lieu)
            elif choix_analyse == "3":
                continue
            else:
                print("Choix invalide.")
        elif choix == "5":
            break
        else:
            print("Choix invalide.")

def menu():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Utilisateurs")
        print("2. Produits")
        print("3. Catégories")
        print("4. Commandes")
        print("5. Événements")
        print("6. Quitter")
        choix = input("Votre choix: ")
        if choix == "1":
            menu_utilisateurs()
        elif choix == "2":
            menu_produits()
        elif choix == "3":
            menu_categories()
        elif choix == "4":
            menu_commandes()
        elif choix == "5":
            menu_evenements()
        elif choix == "6":
            print("Au revoir !")
            sys.exit()
        else:
            print("Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    menu()