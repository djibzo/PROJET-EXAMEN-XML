from bson import ObjectId
from datetime import datetime
import xml.etree.ElementTree as ET
from db_connection import get_db

def valider_participation(user_id, event_id):
    """Valide qu'un utilisateur et un événement existent avant l'inscription."""
    db = get_db()
    
    # Vérifier que l'utilisateur existe
    user = db["utilisateurs"].find_one({"_id": ObjectId(user_id)})
    if not user:
        raise ValueError(f"Utilisateur avec ID {user_id} n'existe pas.")
    
    # Vérifier que l'événement existe
    event = db["evenements"].find_one({"_id": ObjectId(event_id)})
    if not event:
        raise ValueError(f"Événement avec ID {event_id} n'existe pas.")
    
    return user, event

def importer_participations(collection, fichier_xml):
    """Importe les participations depuis un fichier XML."""
    try:
        # Parse XML
        tree = ET.parse(fichier_xml)
        root = tree.getroot()
        
        count_success = 0
        count_errors = 0
        
        # Insérer dans MongoDB
        for participation in root.findall("participation"):
            try:
                user_id = participation.find("user_id").text
                event_id = participation.find("event_id").text
                date_inscription_str = participation.find("date_inscription").text
                statut = participation.find("statut").text
                
                # Convertir la date string en datetime
                date_inscription = datetime.strptime(date_inscription_str, "%Y-%m-%d")
                
                # Valider que l'utilisateur et l'événement existent
                valider_participation(user_id, event_id)
                
                # Vérifier si la participation n'existe pas déjà
                participation_existante = collection.find_one({
                    "user_id": ObjectId(user_id),
                    "event_id": ObjectId(event_id)
                })
                
                if not participation_existante:
                    doc = {
                        "user_id": ObjectId(user_id),
                        "event_id": ObjectId(event_id),
                        "date_inscription": date_inscription,
                        "statut": statut
                    }
                    collection.insert_one(doc)
                    count_success += 1
                else:
                    print(f"Participation déjà existante pour user_id={user_id}, event_id={event_id}")
                    count_errors += 1
                    
            except Exception as e:
                print(f"Erreur lors de l'import d'une participation : {e}")
                count_errors += 1
        
        print(f"Importation terminée: {count_success} participations ajoutées, {count_errors} erreurs.")
        if count_success > 0:
            afficher_toutes_participations(collection)
            
    except ET.ParseError:
        print("Erreur : Le fichier XML est mal formé.")
    except Exception as e:
        print(f"Erreur lors de l'importation : {e}")

def inscrire_utilisateur(collection, user_id, event_id, statut="confirmé"):
    """Inscrit un utilisateur à un événement."""
    try:
        # Valider que l'utilisateur et l'événement existent
        user, event = valider_participation(user_id, event_id)
        
        # Vérifier si l'utilisateur n'est pas déjà inscrit
        participation_existante = collection.find_one({
            "user_id": ObjectId(user_id),
            "event_id": ObjectId(event_id)
        })
        
        if participation_existante:
            print(f"L'utilisateur {user['nom']} {user['prenom']} est déjà inscrit à l'événement '{event['titre']}'.")
            return
        
        # Créer la participation
        doc = {
            "user_id": ObjectId(user_id),
            "event_id": ObjectId(event_id),
            "date_inscription": datetime.now(),
            "statut": statut
        }
        result = collection.insert_one(doc)
        print(f"Inscription réussie! ID de participation : {result.inserted_id}")
        print(f"Utilisateur : {user['nom']} {user['prenom']}")
        print(f"Événement : {event['titre']} ({event['date']})")
        
        afficher_toutes_participations(collection)
    except ValueError as e:
        print(f"Erreur de validation : {e}")
    except Exception as e:
        print(f"Erreur lors de l'inscription : {e}")

def afficher_toutes_participations(collection):
    """Affiche toutes les participations avec détails utilisateur/événement."""
    try:
        print("\n=== Toutes les participations ===")
        db = get_db()
        
        participations = collection.find()
        count = 0
        
        for participation in participations:
            count += 1
            # Récupérer les détails de l'utilisateur
            user = db["utilisateurs"].find_one({"_id": participation["user_id"]})
            # Récupérer les détails de l'événement
            event = db["evenements"].find_one({"_id": participation["event_id"]})
            
            print(f"\n{count}. Participation ID: {participation['_id']}")
            if user:
                print(f"   Utilisateur: {user['nom']} {user['prenom']} ({user['email']})")
            else:
                print(f"   Utilisateur: ID {participation['user_id']} (introuvable)")
            
            if event:
                print(f"   Événement: {event['titre']} - {event['date']} à {event['lieu']}")
            else:
                print(f"   Événement: ID {participation['event_id']} (introuvable)")
            
            print(f"   Date d'inscription: {participation['date_inscription']}")
            print(f"   Statut: {participation['statut']}")
        
        if count == 0:
            print("Aucune participation trouvée.")
        else:
            print(f"\nTotal: {count} participation(s)")
            
    except Exception as e:
        print(f"Erreur lors de l'affichage des participations : {e}")

def rechercher_participations_par_utilisateur(collection, user_id):
    """Recherche toutes les participations d'un utilisateur."""
    try:
        db = get_db()
        user = db["utilisateurs"].find_one({"_id": ObjectId(user_id)})
        
        if not user:
            print(f"Utilisateur avec ID {user_id} introuvable.")
            return
        
        print(f"\n=== Participations de {user['nom']} {user['prenom']} ===")
        
        participations = collection.find({"user_id": ObjectId(user_id)})
        count = 0
        
        for participation in participations:
            count += 1
            event = db["evenements"].find_one({"_id": participation["event_id"]})
            
            print(f"\n{count}. {event['titre'] if event else 'Événement introuvable'}")
            if event:
                print(f"   Date: {event['date']} à {event['lieu']}")
            print(f"   Inscrit le: {participation['date_inscription']}")
            print(f"   Statut: {participation['statut']}")
        
        if count == 0:
            print("Aucune participation trouvée pour cet utilisateur.")
        else:
            print(f"\nTotal: {count} participation(s)")
            
    except Exception as e:
        print(f"Erreur lors de la recherche : {e}")

def rechercher_participants_par_evenement(collection, event_id):
    """Recherche tous les participants d'un événement."""
    try:
        db = get_db()
        event = db["evenements"].find_one({"_id": ObjectId(event_id)})
        
        if not event:
            print(f"Événement avec ID {event_id} introuvable.")
            return
        
        print(f"\n=== Participants à '{event['titre']}' ===")
        print(f"Date: {event['date']} - Lieu: {event['lieu']}")
        
        participations = collection.find({"event_id": ObjectId(event_id)})
        count = 0
        
        for participation in participations:
            count += 1
            user = db["utilisateurs"].find_one({"_id": participation["user_id"]})
            
            print(f"\n{count}. {user['nom'] + ' ' + user['prenom'] if user else 'Utilisateur introuvable'}")
            if user:
                print(f"   Email: {user['email']}")
            print(f"   Inscrit le: {participation['date_inscription']}")
            print(f"   Statut: {participation['statut']}")
        
        if count == 0:
            print("Aucun participant trouvé pour cet événement.")
        else:
            print(f"\nTotal: {count} participant(s)")
            
    except Exception as e:
        print(f"Erreur lors de la recherche : {e}")

def modifier_statut_participation(collection, participation_id, nouveau_statut):
    """Modifie le statut d'une participation."""
    try:
        statuts_valides = ["confirmé", "en_attente", "annulé"]
        if nouveau_statut not in statuts_valides:
            print(f"Statut invalide. Statuts valides: {', '.join(statuts_valides)}")
            return
        
        result = collection.update_one(
            {"_id": ObjectId(participation_id)}, 
            {"$set": {"statut": nouveau_statut}}
        )
        
        if result.modified_count > 0:
            print(f"Statut mis à jour vers '{nouveau_statut}'.")
            afficher_toutes_participations(collection)
        else:
            print("Aucune participation trouvée avec cet ID.")
            
    except Exception as e:
        print(f"Erreur lors de la modification : {e}")

def desinscrire_utilisateur(collection, participation_id):
    """Supprime une participation (désinscription)."""
    try:
        # Récupérer les détails avant suppression
        participation = collection.find_one({"_id": ObjectId(participation_id)})
        if not participation:
            print("Participation introuvable.")
            return
        
        db = get_db()
        user = db["utilisateurs"].find_one({"_id": participation["user_id"]})
        event = db["evenements"].find_one({"_id": participation["event_id"]})
        
        result = collection.delete_one({"_id": ObjectId(participation_id)})
        
        if result.deleted_count > 0:
            print("Désinscription réussie!")
            if user and event:
                print(f"Utilisateur {user['nom']} {user['prenom']} désinscrit de '{event['titre']}'")
            afficher_toutes_participations(collection)
        else:
            print("Aucune participation supprimée.")
            
    except Exception as e:
        print(f"Erreur lors de la désinscription : {e}")

def statistiques_participations(collection):
    """Affiche des statistiques sur les participations."""
    try:
        db = get_db()
        
        print("\n=== Statistiques des participations ===")
        
        # Total des participations
        total_participations = collection.count_documents({})
        print(f"Total des participations: {total_participations}")
        
        # Participations par statut
        statuts = ["confirmé", "en_attente", "annulé"]
        for statut in statuts:
            count = collection.count_documents({"statut": statut})
            print(f"Participations {statut}: {count}")
        
        # Événement le plus populaire
        pipeline = [
            {"$group": {"_id": "$event_id", "count": {"$sum": 1}}},
            {"$sort": {"count": -1}},
            {"$limit": 1}
        ]
        
        result = list(collection.aggregate(pipeline))
        if result:
            event_id = result[0]["_id"]
            count = result[0]["count"]
            event = db["evenements"].find_one({"_id": event_id})
            if event:
                print(f"Événement le plus populaire: '{event['titre']}' ({count} participants)")
        
        # Utilisateur le plus actif
        pipeline = [
            {"$group": {"_id": "$user_id", "count": {"$sum": 1}}},
            {"$sort": {"count": -1}},
            {"$limit": 1}
        ]
        
        result = list(collection.aggregate(pipeline))
        if result:
            user_id = result[0]["_id"]
            count = result[0]["count"]
            user = db["utilisateurs"].find_one({"_id": user_id})
            if user:
                print(f"Utilisateur le plus actif: {user['nom']} {user['prenom']} ({count} participations)")
                
    except Exception as e:
        print(f"Erreur lors du calcul des statistiques : {e}")