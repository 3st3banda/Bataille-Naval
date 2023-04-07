"""Import"""
import pygame
import random
from Modules.Initialisation import *
from Modules.Fonctions_Menu import *

"""Pygame Setup"""
pygame.init()

# Choisi une Image Aléatoirement
images = [img]
image = random.choice(images)

#Initialisation de la fenetre
pygame.display.set_caption("Bataille naval")
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_icon(icone_jeu)

# Redimention de l'image par rapport à la fenetre
image_resized = pygame.transform.scale(image, (screen.get_width(), screen.get_height()))
icone_resized = pygame.transform.scale(icone_jeu,  (60, 60))

# Lancement de la Music
# pygame.mixer.music.play(10000, 1.9, 4000)

# Afichage du fond et du Titre
screen.blit(image_resized, (0, 0))
screen.blit(title, redimention(screen))

#(temp) Affichage des Textes
screen.blit(Title, [60, 10])
screen.blit(icone_resized, [0, 0])

"""Button (Temp)"""
pygame.draw.rect(screen, (139, 235, 249), jouer)
pygame.draw.rect(screen, (136, 220, 249), barre)
pygame.draw.rect(screen, (27, 6, 199), option)
pygame.draw.rect(screen, (27, 6, 199), stats)
pygame.draw.rect(screen, (27, 6, 199), shop)

#(temp) Affichage des Textes
screen.blit(textoption, [400, 20])
screen.blit(textstats, [550, 20])
screen.blit(textshop, [700, 20])
screen.blit(textJouer, [600, 620])

pygame.display.update()
pygame.display.flip()

"""Boucle Principale"""
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False
        elif bouton_clique(jouer, event):
            anime_button(screen, play_button, [600, 620], color_button)
            pygame.mixer.music.play(10000, 1.9, 4000)
        elif bouton_clique(option, event):
            anime_button(screen, option_button, [400, 20], color_button)
        elif bouton_clique(stats, event):
            anime_button(screen, stats_button, [550, 20], color_button)
        elif bouton_clique(shop, event):
            anime_button(screen, shop_button, [700, 20], color_button)

pygame.quit()

