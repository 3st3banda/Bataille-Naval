"""Import"""
import pygame
import random

"""Intialisation des Images"""
pygame.init()

# Chargement des Images de fond
img = pygame.image.load("Projet Bataille Naval\Image\IMG_Bataille_Naval.jpg")
icone_jeu = pygame.image.load("Projet Bataille Naval\Image\Logo.png")

#Bandes son
rise = pygame.mixer.music.load("Projet Bataille Naval\Bandes son\Scott Buckley - The Rise.mp3")

# Chargement Icons
title = pygame.image.load("Projet Bataille Naval\Image/title bataille naval.png")

"""Button (Temp)"""
# (temp)Style du text
text = pygame.font.SysFont("calibri", 30)

# Objets Rect
barre = pygame.Rect((0, 0), (1280, 60))
option = pygame.Rect((400, 0), (150, 80))
stats = pygame.Rect((550, 0), (150, 80))
shop = pygame.Rect((700, 0), (150, 80))
jouer = pygame.Rect((340, 590), (600, 100))

# (temp) Texte
Title = text.render("Bataille Naval", False, (0, 0, 100))
textJouer = text.render("Jouer", False, (0, 0, 100))
textoption = text.render("Option", False, (200, 0, 0))
textstats = text.render("Stats", False, (200, 0, 0))
textshop = text.render("Shop", False, (200, 0, 0))

#Boutons
color_button = ((77, 78, 78), (139, 235, 249))
play_button = (jouer, textJouer)
option_button = (option, textoption)
stats_button = (stats, textstats)
shop_button = (shop, textshop)