"""
Centre de jeux Multi-joueurs 
point d'entrée principal du programme
auteurs :RONNY VALDO ET N'GUESSAM SUZANNE
"""

import os

from jeux import jeux_pendu,jeux_devine,jeux_calcul
from classements import afficher_classements, afficher_historique
from gamification import afficher_succes
from utils import clear_screen, pause, afficher_titre
from profils import créer_profil, charger_profil, afficher_profil   
from regles import afficher_regles
def afficher_menu_principal():
    """menu principal du centre de jeux"""
    profil_actuel = None
    
    while True:
        clear_screen()
        affiche_titre("🎮CENTRE DE JEUX 🎮")
    if profil_actuel:
       afficher_profil(profil_actuel)
       print()
    print("1. Créer un profil")
    print("2. Charger un profil")
    print("3. Jouer")
    print("4. classements")
    print("5. Mon historique")
    print("6. Mes succès")
    print("7. Afficher les règles des jeux")
    print("8. Quitter")

    choix = input("Choisissez une option: ").strip

    if choix == '1':
        nouveau = créer_profil()
    if nouveau:
        profil_actuel = nouveau
        print("Profil créé avec succès!")
        pause()
    elif choix == '2':
        chargé = charger_profil()
        if chargé:
            profil_actuel = chargé
            print("Profil chargé avec succès!")
            pause()
    elif choix == '3': 
        if not profil_actuel:
            print("Veuillez créer ou charger un profil avant de jouer.")
            pause()
        else:
            afficher_titre("Choisissez un jeu")
            print("1. Le Pendu")
            print("2. Devine le Nombre")
            print("3. Calcul Mental")
            jeu_choix = input("Choisissez un jeu: ").strip()
            if jeu_choix == '1':
                jeux_pendu(profil_actuel)
            elif jeu_choix == '2':
                jeux_devine(profil_actuel)
            elif jeu_choix == '3':
                jeux_calcul(profil_actuel)
            else:
                print("Choix invalide.")
                pause()
    elif choix == '4':
        afficher_classements()
        pause()
    elif choix == '5':
        if not profil_actuel:
            print("Veuillez créer ou charger un profil pour voir votre historique.")
        else:
            afficher_historique(profil_actuel)
        pause()
    elif choix == '6':
        if not profil_actuel:
            print("Veuillez créer ou charger un profil pour voir vos succès.")
        else:
            afficher_succes(profil_actuel)
        pause()
    elif choix == '7':
        afficher_regles()
        pause()
    elif choix == '8':
        print("Merci d'avoir joué! À bientôt!")

if __name__ == "__main__":
 afficher_menu_principal()