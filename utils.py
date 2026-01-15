"""
Modules utilitaires pour le centre de jeux
auteurs : RONNY VALDO ET N'GUESSAM SUZANNE
"""
import os
import json

def clear_screen():
    """Efface l'écran du terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    """Met en pause l'exécution jusqu'à ce que l'utilisateur appuie sur Entrée."""
    input("Appuyez sur Entrée pour continuer...")

def afficher_titre(titre):
    """Affiche un titre encadré."""
    print("\n" + "="*60)
    print(titre.center(60))
    print("="*60 + "\n")

def sauvegarder_fichier(chemin,data):
    """Sauvegarde les données dans un fichier JSON.
    
    Args:
        chemin: Chemin du fichier
        data: Données à sauvegarder (dict ou list)
    
    Returns:
        bool: True si succès, False sinon"""
    try:
        # Créer le dossier parent si nécessaire
        dossier = os.path.dirname(chemin)
        if dossier and not os.path.exists(dossier):
            os.makedirs(dossier)
        
        with open(chemin, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"❌ Erreur de sauvegarde: {e}")
        return False
    
def charger_fichier(chemin):
   def charger_fichier(chemin, afficher_messages=True):
    """
    Charge les données depuis un fichier JSON
    
    Args:
        chemin: Chemin du fichier
        afficher_messages: Si True, affiche les messages de statut
    
    Returns:
        dict/list: Données chargées, ou None en cas d'erreur
    """
    try:
        if not os.path.exists(chemin):
            if afficher_messages:
                print(f"❌ Fichier '{chemin}' introuvable")
            return None
        
        with open(chemin, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if afficher_messages:
            print(f"✅ '{chemin}' chargé avec succès")
        
        return data
            
    except json.JSONDecodeError:
        if afficher_messages:
            print(f"❌ Le fichier '{chemin}' contient du JSON invalide")
        return None
    
    except Exception as e:
        if afficher_messages:
            print(f"❌ Erreur de chargement : {e}")
        return None
    def gestion_erreur(message):
        """Gestion des erreurs de fichier JSON."""
    print(f"❌ Erreur: {message}")
    pause()








