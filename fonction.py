#!/usr/bin/python3
# -*- coding: Utf-8 -*

#Chargement des bibliotheques et du fichier constantes.py
import pygame
from pygame.locals import *
from constantes import *

#Logo du jeu
image_icone = "images/logo.png"

"""
Fonction d'affichage de la matrice en console. La matrice est affichée
en laisant une ligne pour chaque liste qui la compose. Le parametre
de la fonction est matrice, ce parametre n'est pas modifié par la
fonction.
"""

def ecrire_matrice(matrice):

    for ligne in matrice:
        print(ligne)

def ecrire_matrice_2(matrice_2):

    for ligne in matrice_2:
        print(ligne)

"""
Fonction de génération de matrice carré (ligne = colonne). Cette
fonction utilise un paramètre d'entrée qui est la taille de la matrice.
Le retour de la fonction est la matrice générée.
"""

def generer_matrice(taille):

    matrice = []

    for j in range(taille):
        ligne = []
        for i in range(taille):
            ligne.append(0)
        matrice.append(ligne)

    for couple in case:
        matrice [couple[1]][couple[0]] = 1
    matrice[depart[1]][depart[0]] = 2

    return matrice

"""
Fonction d'affichage de la matrice vers la fenêtre Pygame. Cette
fonction utilise deux parametres d'entrée qui sont la matrice et
la fenetre. Seule la fenetre est modifiée par la fonction. Retour
de la fenetre pygame en sortie.
"""

def afficher(matrice, fenetre, switch_tab):

    grille = pygame.image.load(image_grille).convert_alpha()
    curseur = pygame.image.load("images/curseur/curseur_10.png").convert_alpha()

    for ligne in range(taille_case):
        for colonne in range(taille_case):

            if matrice[ligne][colonne] == 1 or 5:
                fenetre.blit(grille,(colonne * taille_sprite,ligne * taille_sprite))

            if matrice[ligne][colonne] == 2:
                if switch_tab != 1:
                    fenetre.blit(curseur,(colonne * taille_sprite,ligne * taille_sprite))

            if matrice[ligne][colonne] == 3:
                fenetre.blit(depart,(colonne * taille_sprite,ligne * taille_sprite))

    return fenetre

def afficher_2(matrice, fenetre):

    explosion=pygame.image.load("images/explosion.png").convert_alpha()

    for ligne in range(taille_case):
        for colonne in range(taille_case):
            if matrice[ligne][colonne] == 4:
                fenetre.blit(explosion,(colonne * taille_sprite,ligne * taille_sprite))
        
    return fenetre


"""
Fonction qui permet de trouver la position du curseur dans la matrice.
Cette fonction utilise un parametre d'entrée (matrice). La matrice
n'est pas modifiée par la fonction. Retour d'un couple d'entier en
sortie representant, sur la matrice, la position en (x,y).
"""

def trouver_curseur(matrice):
    pos = False

    for ligne in range(taille_case):
        for colonne in range(taille_case):

            if matrice[ligne][colonne] == 2:
                    pos = (ligne,colonne)

    return pos

"""
Fonction semblable à la précédente, son rôle est de superposé les
coordonnées de l'animation du curseur avec ce dernier, sa position
étant sa ligne et sa colonne dans la matrice multiplié par 72 qui
correspond au nombre de pixels par case lors de l'affichage. Retour
des coordonnées, en pixels, d'un couple d'entier représentant la
position en (x, y).
"""

def superposition_curseur(matrice):
    position = False

    for ligne in range(taille_case):
        for colonne in range(taille_case):

            if matrice[ligne][colonne] == 2:
                    position = (colonne * 72,ligne * 72)

    return position

"""
Fonction qui permet de déplacer le curseur dans la matrice. Cette
fonction utilise deux parametres d'entrée qui sont la matrice et le
sens de déplacement. La matrice est modifiée par la fonction si le
déplacement est possible. Retour de la matrice en sortie.
"""

def deplacer_curseur(matrice:list,sens:str)->list:
    pos=trouver_curseur(matrice)
    nombre_sauts = 1

    if sens == "bas" and pos [0] < 9:

        if matrice[pos[0] + 1][pos[1]] != 4:
            matrice[pos[0]][pos[1]] = 1
            matrice[pos[0] + 1][pos[1]] = 2

        #Dans le cas où le déplacement se fait dans la direction d'une case déjà utilisée par le joueur
        elif matrice[pos[0] + 1][pos[1]] == 4:

                #Initialsation de la boucle (max 9 tours)
                while nombre_sauts != 0:

                    #Evite le "out of range" si les cases sont occupées jusqu'au bord de la matrice
                    if pos[0] + nombre_sauts <= 9:

                        #Condition simplifiée : Si la case de déplacement est "libre" (à indice 1), alors...
                        if matrice[pos[0] + nombre_sauts][pos[1]] != 4:

                            #La position actuelle devient "libre" (à l'indice 1)
                            matrice[pos[0]][pos[1]] = 1

                            #La nouvelle position est modifiée dans la matrice
                            matrice[pos[0] + nombre_sauts][pos[1]] = 2

                            #Critère d'arrêt de la boucle
                            nombre_sauts = 0

                        elif nombre_sauts == 9:

                            #Critère d'arrêt supplémentaire pour éviter l'erreur "list index out of range"
                            nombre_sauts = 0

                        else :
                            nombre_sauts += 1
                    else :
                        nombre_sauts = 0

    if sens == "haut" and pos [0] > 0:

        if matrice[pos[0] - 1][pos[1]] != 4:
            matrice[pos[0]][pos[1]] = 1
            matrice[pos[0] - 1][pos[1]] = 2

        elif matrice[pos[0] - 1][pos[1]] == 4:
            while nombre_sauts != 0:
                    
                if pos[0] - nombre_sauts >= 0:

                    if matrice[pos[0] - nombre_sauts][pos[1]] != 4:
                        matrice[pos[0]][pos[1]] = 1
                        matrice[pos[0] - nombre_sauts][pos[1]] = 2
                        nombre_sauts = 0

                    elif nombre_sauts == 9:
                        nombre_sauts = 0

                    else :
                        nombre_sauts += 1

                else :
                    nombre_sauts = 0

    if sens == "droite" and pos [1] < 9:

        if matrice[pos[0]][pos[1] + 1] != 4:
            matrice[pos[0]][pos[1]] = 1
            matrice[pos[0]][pos[1] + 1] = 2

        elif matrice[pos[0]][pos[1] + 1] == 4:
            while nombre_sauts != 0:

                if pos[1] + nombre_sauts <= 9:

                    if matrice[pos[0]][pos[1] + nombre_sauts] != 4:
                        matrice[pos[0]][pos[1]] = 1
                        matrice[pos[0]][pos[1] + nombre_sauts] = 2
                        nombre_sauts = 0

                    elif nombre_sauts == 9:
                        nombre_sauts = 0

                    else :
                        nombre_sauts += 1

                else :
                    nombre_sauts = 0

    if sens == "gauche" and pos [1] > 0:

        if matrice[pos[0]][pos[1] - 1] != 4:
            matrice[pos[0]][pos[1]] = 1
            matrice[pos[0]][pos[1] - 1] = 2

        elif matrice[pos[0]][pos[1] - 1] == 4:
            while nombre_sauts != 0:

                if pos[1] - nombre_sauts >= 0:

                    if matrice[pos[0]][pos[1] - nombre_sauts] != 4:
                        matrice[pos[0]][pos[1]] = 1
                        matrice[pos[0]][pos[1] - nombre_sauts] = 2
                        nombre_sauts = 0

                    elif nombre_sauts == 9:
                        nombre_sauts = 0

                    else :
                        nombre_sauts += 1
                
                else :
                    nombre_sauts = 0

    return matrice

def update_matrice_missile_anim(matrice):
    pos=trouver_curseur(matrice)
    matrice[pos[0]][pos[1]] = 5
    matrice[0][0] = 2

def update_matrice_missile_def(matrice):
    for ligne in range(taille_case):
        for colonne in range(taille_case):

            if matrice[ligne][colonne] == 5:
                matrice[ligne][colonne] = 4

def pos_bombe_colonne(matrice):
    for ligne in range(taille_case):
        for colonne in range(taille_case):

            if matrice[ligne][colonne] == 5:
                pos_colonne_bombe = (colonne * 72)

    return pos_colonne_bombe

def nb_lignes_bombe_depart(matrice):
    for ligne in range(taille_case):
        for colonne in range(taille_case):

            if matrice[ligne][colonne] == 5:
                nb_lignes = (ligne * 72)

    return nb_lignes

def generer_tab():

    tab = [1, 1, 1, 1, 1]
    tab[0] = 2

    return tab

def update_tab(tab):
    curseur_tab = pygame.image.load("images/curseur_tab.png").convert_alpha()

    for element in tab:
        if element == 2:
            fenetre.blit(curseur_tab,(deplacer_tab(tab) + 1, 8 * 72 + 1))

def deplacer_tab(tab):
    return 12 * 72