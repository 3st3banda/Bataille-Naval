#!/usr/bin/python3
# -*- coding: Utf-8 -*

#Chargement des bibliothèques
import pygame
from pygame.locals import *

#Taille des sprites et de la fenêtre
taille_case = 10

taille_sprite = 72
cote_fenetre_longueur = taille_case * taille_sprite + 560
cote_fenetre_largeur = taille_case * taille_sprite

screen = fenetre = pygame.display.set_mode((cote_fenetre_longueur, cote_fenetre_largeur))
#fenetre.fill((64,89,141))

#Fond de la fenêtre
image_fond = "images/fond.png"
fond = pygame.image.load(image_fond).convert()

#Titre de la fenêtre
titre_fenetre = "Bataille Navale"

#Images du jeu
image_grille = "images/grille.png"

#Liste de couple représantant les positions des grilles (x,y)
case = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9),
       (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9),
       (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9),
       (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9),
       (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9),
       (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9),
       (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8), (6, 9),
       (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9),
       (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8), (8, 9),
       (9, 0), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9)]

#Position du curseur à l'origine
depart = (0,0)

#pygame.mixer.init()
#son = pygame.mixer.Sound("son/musique.mp3")
#son.play(loops=-1, maxtime=0, fade_ms=0)