"""Import"""
import pygame
import random


"""Intialisation des Images"""
pygame.init()


# Chargement des Images
img = pygame.image.load("Projet Bataille Naval\Image\IMG_Bataille_Naval.jpg")
icone_jeu = pygame.image.load("Projet Bataille Naval\Image\Logo.png")
title = pygame.image.load("Projet Bataille Naval\Image/title bataille naval.png")
icone_option1 = pygame.image.load("Projet Bataille Naval\Image\Option1.png")
button_jouer = pygame.image.load("Projet Bataille Naval\Image\Bouton_Jouer.png")
button_stats = pygame.image.load("Projet Bataille Naval\Image\Bouton_Stats.png")
button_shop = pygame.image.load("Projet Bataille Naval\Image\Bouton_Shop.png")

#Bandes son
rise = pygame.mixer.music.load("Projet Bataille Naval\Bandes son\Scott Buckley - The Rise.mp3")


"""Button (Temp)"""
# (temp)Style du text
text = pygame.font.SysFont("Norwester", 30)


# Objets Rect
stats_rect = pygame.Rect((550, 0), (150, 80))
shop_rect = pygame.Rect((700, 0), (150, 80))
jouer_rect = pygame.Rect((390, 590), (500, 100))
option_rect = pygame.Rect((30, 30), (50, 50))


# (temp) Texte
Title = text.render("Bataille Naval", False, (255, 255, 255))
textJouer = text.render("Jouer", False, (255, 255, 255))
textstats = text.render("Stats", False, (0, 0, 0))
textshop = text.render("Shop", False, (0, 0, 0))
