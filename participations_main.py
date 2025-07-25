from db_connection import get_db
from participations_crud_operations import *

def afficher_utilisateurs_disponibles():
    """Affiche la liste des utilisateurs avec leurs IDs pour faciliter la sélection."""
    try:
        db = get_db()
        collection = db["utilisateurs"]
        
        print("\n=== Utilisateurs disponibles ===")
        users = collection.find()
        count = 0
        
        for user in users:
            count += 1
            print(f"{count}. ID: {user['_id']} - {user['nom']} {user['prenom']} ({user['email']})")
        
        if count == 0:
            print("Aucun utilisateur trouvé. Veuillez d'abord ajouter des utilisateurs.")
        
    except Exception as e:
        print(f"Erreur lors de l'affichage des utilisateurs : {e}")

def afficher_evenements_disponibles():
    """Affiche la liste des événements avec leurs IDs pour faciliter la sélection."""
    try:
        db = get_db()
        collection = db["evenements"]
        
        print("\n=== Événements disponibles ===")
        events = collection.find()
        count = 0
        
        for event in events:
            count += 1
            print(f"{count}. ID: {event['_id']} - {event['titre']} ({event['date']} à {event['lieu']})")
        
        if count == 0:
            print("Aucun événement trouvé. Veuillez d'abord ajouter des événements.")
        
    except Exception as e:
        print(f"Erreur lors de l'affichage des événements : {e}")

def menu_participations():
    """Menu principal pour la gestion des participations."""
    db = get_db()
    collection = db["participations"]

    while True:
        print("\n" + "="*50)
        print("          GESTION DES PARTICIPATIONS")
        print("="*50)
        print("1.  Importer les participations depuis XML")
        print("2.  Inscrire un utilisateur à un événement")
        print("3.  Afficher toutes les participations")
        print("4.  Voir les participations d'un utilisateur")
        print("5.  Voir les participants d'un événement")
        print("6.  Modifier le statut d'une participation")
        print("7.  Désinscrire un utilisateur (supprimer participation)")
        print("8.  Statistiques des participations")
        print("9.  Afficher les utilisateurs disponibles")
        print("10. Afficher les événements disponibles")
        print("11. Quitter")
        print("-" * 50)

        choix = input("Choisissez une option (1-11) : ").strip()

        if choix == "1":
            print("\n--- Importation depuis XML ---")
            fichier_xml = input("Chemin du fichier XML (par défaut: xml/participations.xml) : ").strip()
            if not fichier_xml:
                fichier_xml = "xml/participations.xml"
            importer_participations(collection, fichier_xml)

        elif choix == "2":
            print("\n--- Inscription à un événement ---")
            afficher_utilisateurs_disponibles()
            user_id = input("\nEntrez l'ID de l'utilisateur : ").strip()
            
            afficher_evenements_disponibles()
            event_id = input("\nEntrez l'ID de l'événement : ").strip()
            
            print("\nStatuts disponibles: confirmé, en_attente, annulé")
            statut = input("Statut (par défaut: confirmé) : ").strip()
            if not statut:
                statut = "confirmé"
            
            inscrire_utilisateur(collection, user_id, event_id, statut)

        elif choix == "3":
            afficher_toutes_participations(collection)

        elif choix == "4":
            print("\n--- Participations par utilisateur ---")
            afficher_utilisateurs_disponibles()
            user_id = input("\nEntrez l'ID de l'utilisateur : ").strip()
            rechercher_participations_par_utilisateur(collection, user_id)

        elif choix == "5":
            print("\n--- Participants par événement ---")
            afficher_evenements_disponibles()
            event_id = input("\nEntrez l'ID de l'événement : ").strip()
            rechercher_participants_par_evenement(collection, event_id)

        elif choix == "6":
            print("\n--- Modification de statut ---")
            afficher_toutes_participations(collection)
            participation_id = input("\nEntrez l'ID de la participation : ").strip()
            
            print("\nStatuts disponibles: confirmé, en_attente, annulé")
            nouveau_statut = input("Nouveau statut : ").strip()
            modifier_statut_participation(collection, participation_id, nouveau_statut)

        elif choix == "7":
            print("\n--- Désinscription ---")
            afficher_toutes_participations(collection)
            participation_id = input("\nEntrez l'ID de la participation à supprimer : ").strip()
            
            confirmation = input("Êtes-vous sûr de vouloir supprimer cette participation ? (oui/non) : ").strip().lower()
            if confirmation in ["oui", "o", "yes", "y"]:
                desinscrire_utilisateur(collection, participation_id)
            else:
                print("Suppression annulée.")

        elif choix == "8":
            statistiques_participations(collection)

        elif choix == "9":
            afficher_utilisateurs_disponibles()

        elif choix == "10":
            afficher_evenements_disponibles()

        elif choix == "11":
            print("\n" + "="*50)
            print("     Merci d'avoir utilisé le système!")
            print("         Au revoir! 👋")
            print("="*50)
            break

        else:
            print("\n❌ Option invalide. Veuillez choisir entre 1 et 11.")
            
        # Pause pour permettre à l'utilisateur de lire les résultats
        if choix != "11":
            input("\nAppuyez sur Entrée pour continuer...")

def menu_rapide():
    """Menu rapide avec les actions les plus courantes."""
    print("\n" + "="*40)
    print("         MENU RAPIDE - PARTICIPATIONS")
    print("="*40)
    print("1. Inscrire un utilisateur")
    print("2. Voir toutes les participations")
    print("3. Statistiques")
    print("4. Menu complet")
    print("5. Quitter")
    print("-" * 40)
    
    choix = input("Choix rapide (1-5) : ").strip()
    
    if choix == "4":
        menu_participations()
    elif choix == "5":
        print("Au revoir!")
        return
    elif choix in ["1", "2", "3"]:
        db = get_db()
        collection = db["participations"]
        
        if choix == "1":
            afficher_utilisateurs_disponibles()
            user_id = input("\nID utilisateur : ").strip()
            afficher_evenements_disponibles()
            event_id = input("\nID événement : ").strip()
            inscrire_utilisateur(collection, user_id, event_id)
        elif choix == "2":
            afficher_toutes_participations(collection)
        elif choix == "3":
            statistiques_participations(collection)
    else:
        print("Option invalide.")

if __name__ == "__main__":
    print("\n🎯 Système de Gestion des Participations")
    print("   XML-MongoDB Integration Project")
    
    # Proposer le menu rapide d'abord
    print("\nQuel menu souhaitez-vous utiliser ?")
    print("1. Menu rapide (actions courantes)")
    print("2. Menu complet (toutes les fonctionnalités)")
    
    type_menu = input("Votre choix (1-2) : ").strip()
    
    if type_menu == "1":
        menu_rapide()
    else:
        menu_participations()