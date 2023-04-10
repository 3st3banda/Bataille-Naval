"""Import"""
import pygame
import random


"""Intialisation des Images"""
pygame.init()


# Chargement des Images
img = pygame.image.load("Projet Bataille Naval\Image\IMG_Bataille_Naval.jpg")
icone_jeu = pygame.image.load("Projet Bataille Naval\Image\Logo.png")
icone_option1 = pygame.image.load("Projet Bataille Naval\Image\Bouton_option_avant_clic_50x50.png")
icone_option2 = pygame.image.load("Projet Bataille Naval\Image\Bouton_option_clic_50x50.png")
button_jouer = pygame.image.load("Projet Bataille Naval\Image\BOUTON_JOUER_AVANT_CLIC.png")
button_jouer2 = pygame.image.load("Projet Bataille Naval\Image\BOUTON_JOUER_CLIC.png")
button_stats = pygame.image.load("Projet Bataille Naval\Image\BOUTON_STATS_AVANT_CLIC.png")
button_stats2 = pygame.image.load("Projet Bataille Naval\Image\BOUTON_STATS_CLIC.png")
button_shop = pygame.image.load("Projet Bataille Naval\Image\BOUTON_SHOP_AVANT_CLIC.png")
button_shop2 = pygame.image.load("Projet Bataille Naval\Image\BOUTON_SHOP_CLIC.png")
button_retour = pygame.image.load("Projet Bataille Naval\Image\RETOUR_AVANT_CLIC.png")
button_retour2 = pygame.image.load("Projet Bataille Naval\Image\RETOUR_CLIC.png")
title = pygame.image.load("Projet Bataille Naval\Image/titre.png")

#Bandes son
rise = pygame.mixer.music.load("Projet Bataille Naval\Bandes son\Scott Buckley - The Rise.mp3")


"""Button"""
# (temp)Style du text
text = pygame.font.SysFont("Norwester", 30)


# Objets Rect
stats_rect = pygame.Rect((200, 580), (300, 100))
shop_rect = pygame.Rect((778, 580), (300, 100))
jouer_rect = pygame.Rect((440, 580), (400, 100))
option_rect = pygame.Rect((30, 30), (50, 50))
retour_rect = pygame.Rect((565, 605), (150, 50))



