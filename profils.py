"""
Module de gestion des profils joueurs
Tous les profils sont stockés dans data/profils.json
"""

import os
from datetime import datetime
from utils import (
    charger_fichier, 
    sauvegarder_fichier, 
    clear_screen, 
    pause, 
    afficher_titre
)

FICHIER_PROFILS = "data/profils.json"

def initialiser_fichier_profils():
    """Initialise le fichier profils.json s'il n'existe pas"""
    os.makedirs("data", exist_ok=True)
    
    if not os.path.exists(FICHIER_PROFILS):
        sauvegarder_fichier(FICHIER_PROFILS, {"joueurs": []})

def creer_profil():
    """Créer un nouveau profil joueur"""
    clear_screen()
    afficher_titre("CRÉER UN PROFIL")
    
    initialiser_fichier_profils()
    data = charger_fichier(FICHIER_PROFILS)
    
    nom = input("Entrez votre nom (3-20 caractères): ").strip()
    
    if len(nom) < 3 or len(nom) > 20:
        print("❌ Le nom doit contenir entre 3 et 20 caractères.")
        pause()
        return None
    
    # Vérifier si le profil existe déjà
    for joueur in data["joueurs"]:
        if joueur["nom"].lower() == nom.lower():
            print(f"❌ Un profil existe déjà pour '{nom}'.")
            pause()
            return None
    
    # Créer le nouveau profil
    profil = {
        "nom": nom,
        "date_creation": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "parties": [],
        "score_total": 0,
        "succes": [],
        "stats": {
            "devinette": {"jouees": 0, "gagnees": 0},
            "calcul": {"jouees": 0, "gagnees": 0},
            "pendu": {"jouees": 0, "gagnees": 0}
        }
    }
    
    # Ajouter à la liste des joueurs
    data["joueurs"].append(profil)
    
    if sauvegarder_fichier(FICHIER_PROFILS, data):
        print(f"✅ Profil '{nom}' créé avec succès!")
        pause()
        return profil
    else:
        print("❌ Erreur lors de la création du profil.")
        pause()
        return None

def charger_profil():
    """Charger un profil existant"""
    clear_screen()
    afficher_titre("CHARGER UN PROFIL")
    
    initialiser_fichier_profils()
    data = charger_fichier(FICHIER_PROFILS)
    
    if not data or not data.get("joueurs"):
        print("❌ Aucun profil trouvé. Créez-en un d'abord!")
        pause()
        return None
    
    joueurs = data["joueurs"]
    
    print("Profils disponibles:")
    for i, joueur in enumerate(joueurs, 1):
        print(f"{i}. {joueur['nom']} - {joueur['score_total']} pts - {len(joueur['parties'])} parties")
    
    try:
        choix = int(input(f"\nChoisissez un profil (1-{len(joueurs)}): "))
        if 1 <= choix <= len(joueurs):
            profil = joueurs[choix - 1]
            print(f"✅ Profil '{profil['nom']}' chargé!")
            pause()
            return profil
        else:
            print("❌ Choix invalide.")
            pause()
            return None
    except ValueError:
        print("❌ Entrée invalide.")
        pause()
        return None

def sauvegarder_profil(profil):
    """Sauvegarder un profil dans le fichier JSON central"""
    if not profil:
        return False
    
    data = charger_fichier(FICHIER_PROFILS)
    if not data:
        return False
    
    # Trouver et mettre à jour le profil
    for i, joueur in enumerate(data["joueurs"]):
        if joueur["nom"] == profil["nom"]:
            data["joueurs"][i] = profil
            return sauvegarder_fichier(FICHIER_PROFILS, data)
    
    return False

def afficher_profil(profil):
    """Affiche les informations du profil"""
    if not profil:
        return
    
    print(f"👤 Profil: {profil['nom']}")
    print(f"💰 Score total: {profil['score_total']} pts")
    print(f"🎯 Parties jouées: {len(profil['parties'])}")
    
    # Calcul du nombre total de succès disponibles
    from gamification import SUCCES_LISTE
    print(f"🏆 Succès: {len(profil['succes'])}/{len(SUCCES_LISTE)}")
    
    # Statistiques par jeu
    stats = profil["stats"]
    print(f"\n📊 Statistiques:")
    for jeu, stat in stats.items():
        if stat["jouees"] > 0:
            taux = (stat["gagnees"] / stat["jouees"] * 100)
            print(f"   {jeu.capitalize()}: {stat['gagnees']}/{stat['jouees']} ({taux:.1f}%)")