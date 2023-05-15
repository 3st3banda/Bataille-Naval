#!/usr/bin/python3
# -*- coding: Utf-8 -*

#Chargement des bibliotheques et des fichiers constantes.py et fonctions.py
import pygame
from pygame.locals import *
from fonction import *
from constantes import *

#Création matrice de jeu
matrice = generer_matrice(taille_case)
ecrire_matrice(matrice)

tab = generer_tab()

#Démarrer pygame
pygame.init()

#Création de la fenêtre Pygame (écran : longueur = 1280, largeur = 720, écran bleu foncé par défaut)
screen = fenetre = pygame.display.set_mode((cote_fenetre_longueur, cote_fenetre_largeur))
fenetre.fill((34,53,92))

#Création variable pour animation (chaque valeur de "anim_curseur" est associée par cheminement à une image)
anim_curseur = 0
anim_curseur_reverse = anim_curseur
anim_missile = 0
anim_missile_reverse = anim_missile
sprite_bombe = 0
valeur_defaut = 0
vague_explo = 0
afficher_croix = 0
switch_tab = 0


#Initialisation du conteur du nombre de bombe(s) lachée(s)
bombe_lachee = 0

#Icone et titre fenêtre
icone_jeu = pygame.image.load(image_icone)
pygame.display.set_icon(icone_jeu)
pygame.display.set_caption(titre_fenetre)

#BOUCLE PRINCIPALE
running = True
while running:

	#Limitation de vitesse de la boucle
    pygame.time.Clock().tick(60)

    #Gestion des événements du jeu souris et clavier
    for event in pygame.event.get():
            if event.type == QUIT:
                running = 0
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = 0

                #Touches de déplacement
                elif event.key == K_RIGHT:
                    matrice=deplacer_curseur(matrice, "droite")
                elif event.key == K_LEFT:
                    matrice=deplacer_curseur(matrice, "gauche")
                elif event.key == K_UP:
                    matrice=deplacer_curseur(matrice, "haut")
                elif event.key == K_DOWN:
                    matrice=deplacer_curseur(matrice, "bas")

                elif event.key == K_TAB:
                    if switch_tab == 0:
                        switch_tab = 1
                    else:
                        switch_tab = 0
                
                #Lâcher une bombe
                elif event.key == K_SPACE:
                    bombe_lachee = 1
                    valeur_defaut = 0
                    update_matrice_missile_anim(matrice)

	#Affichages du fond et des sprites aux nouvelles positions
    fenetre.blit(fond, (0,0))
    fenetre = afficher(matrice, fenetre, switch_tab)

    if switch_tab == 1:
        update_tab(tab)

    if anim_curseur_reverse == 10:
        anim_curseur -= 1
        if anim_curseur == 1:
            anim_curseur_reverse = 0
    else:
        anim_curseur_reverse = anim_curseur = anim_curseur + 1

    screen.blit(pygame.image.load("images/tab.png").convert_alpha(),(72 * 11, 72 * 8))
    
    if switch_tab == 0:
        screen.blit(pygame.image.load("images/curseur/curseur_" + str(anim_curseur) + ".png").convert_alpha(),(superposition_curseur(matrice)))
    
    if afficher_croix == 1:
        afficher_2(matrice, fenetre)

    if bombe_lachee == 1:
        if valeur_defaut == 0:
            valeur_defaut = 1
            pxl_avant_impact = 720

        else:
            valeur_arrivee = nb_lignes_bombe_depart(matrice)

            if pxl_avant_impact <= valeur_arrivee + 36:
                bombe_lachee = 0
                vague_explo = 1
            
            else:
                pxl_avant_impact -= 10
                
                if anim_missile_reverse == 5:
                    anim_missile -= 1
                    if anim_missile == 1:
                        anim_missile_reverse = 0

                else:
                    anim_missile_reverse = anim_missile = anim_missile + 1

                screen.blit(pygame.image.load("images/missile/missile_" + str(anim_missile) + ".png").convert_alpha(),(pos_bombe_colonne(matrice) - 36, pxl_avant_impact))
    
    if vague_explo != 0:
        screen.blit(pygame.image.load("images/vague_explo/vague_explo_" + str(vague_explo) + ".png").convert_alpha(),(pos_bombe_colonne(matrice), valeur_arrivee))
        if vague_explo == 23:
            vague_explo = 0
            update_matrice_missile_def(matrice)
            afficher_croix = 1
        else:
            vague_explo += 1

    #screen.blit(pygame.image.load("images/matrice_2.png").convert_alpha(),(72 * 11 - 1, 72))

    pygame.time.delay(25)   #Temps de pause (en milisecondes) qui permet la fluidité de l'animation
    pygame.display.flip()   #Actualise l'affichage de tout l'écran

#Fermeture Pygame
pygame.quit ()