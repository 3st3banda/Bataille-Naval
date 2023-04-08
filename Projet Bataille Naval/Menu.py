"""Import"""
import pygame
from Modules.Initialisation import *
from Modules.Fonctions_Menu import *

"""Pygame Setup"""
pygame.init()


"""Initialisation de la fenetre"""
pygame.display.set_caption("Bataille naval")
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_icon(icone_jeu)

# Lancement de la Music
pygame.mixer.music.play(10000, 1.9, 10000)


"""Affichage des Images redimentionées"""
"""
    Images -> [
        (image,
        Taille souhaité de l'image -> (x, y) ou False: si on ne désire pas redimentionné l'image
        Position de l'image dans la fenetre -> (x, y)
        )
    ]
"""
menu1 = [
    # Images
    (img, (screen.get_width(), screen.get_height()), (0, 0)),   #Fond d'écran
    (icone_jeu, (60, 60), (610, 0)),            #Logo
    (icone_option1, (50, 50), (30, 30)),        #Icone option
    (button_jouer, (400, 100), (440, 580)),     #Bouton Jouer
    (button_stats, (300, 100), (200, 580)),     #Bouton Stats
    (button_shop, (300, 100), (778, 580)),      #Bouton Shop
    (title, (600, 231), (340, 245)),            #Titre (image)

    #Textes
    (Title, False, (580, 550)),     #Titre (texte)                 
    (textJouer, False, [610, 620]), #Texte Jouer
    (textstats, False, [320, 620]), #Texte Stats
    (textshop, False, [900, 620])   #Text Shop

]
affiche_images(screen, menu1)

pygame.display.update()
pygame.display.flip()

"""Boucle Des Events"""
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False
        elif bouton_clique(jouer_rect, event):
            fond_noir_transp(screen)
        elif bouton_clique(stats_rect, event):
            fond_noir_transp(screen)    
        elif bouton_clique(option_rect, event):
            fond_noir_transp(screen)    
        elif bouton_clique(shop_rect, event):
            fond_noir_transp(screen)

pygame.quit()

