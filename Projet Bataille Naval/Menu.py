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
# pygame.mixer.music.play(10000, 1.9, 10000)


"""Affichage d'une page (Avec des images redimensionées)"""
"""
    Page actuel -> [
        (image,
        Taille souhaité de l'image -> (x, y) ou False: si on ne désire pas redimensionné l'image
        Position de l'image dans la fenetre -> (x, y)
        )
    ]
"""
menu = [
    # Images
    (img, (screen.get_width(), screen.get_height()), (0, 0)),   #Fond d'écran
    (icone_jeu, False, (490, 0)),            #Logo
    (icone_option1, (50, 50), (30, 30)),        #Icone option
    (button_jouer, (400, 100), (440, 580)),     #Bouton Jouer
    (button_stats, (300, 100), (180, 580)),     #Bouton Stats
    (button_shop, (300, 100), (798, 580)),      #Bouton Shop
    (title, False, (340, 470))                  #Image Titre
            
]


option = [
    #Images
    (button_retour, False, (565, 605)),     #Bouton Retour
]


jouer = [
    # Images
    (img, (screen.get_width(), screen.get_height()), (0, 0)),   #Fond d'écran
    (icone_jeu, False, (490, 0)),            #Logo
    (icone_option1, (50, 50), (30, 30)),        #Icone option
    (button_retour, False, (565, 605))     #Bouton Retour
]


stats = [
    # Images
    (img, (screen.get_width(), screen.get_height()), (0, 0)),   #Fond d'écran
    (icone_jeu, False, (490, 0)),            #Logo
    (icone_option1, (50, 50), (30, 30)),       #Icone option
    (button_retour, False, (565, 605)),     #Bouton Retour
]


shop = [
        # Images
    (img, (screen.get_width(), screen.get_height()), (0, 0)),   #Fond d'écran
    (icone_jeu, False, (490, 0)),            #Logo
    (icone_option1, (50, 50), (30, 30)),     #Icone option
    (button_retour, False, (565, 605)),     #Bouton Retour
]
"""Défini si une page est actif ou non"""
menu_actif = True
option_actif = False
jouer_actif = False
stats_actif = False
shop_actif = False


"""Affichage du menu"""
affichage(screen, menu)

pygame.display.update()

"""Boucle Des Events"""
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False
        elif bouton_clique(jouer_rect, event, menu_actif):
            anime_button(screen, button_jouer2, (440, 580))
            affichage(screen, jouer)
            menu_actif = False
            option_actif = False
            jouer_actif = True
        elif bouton_clique(stats_rect, event, menu_actif):
            anime_button(screen, button_stats2, (180, 580))
            affichage(screen, stats)
            menu_actif = False
            option_actif = False
            stats_actif = True
        elif bouton_clique(option_rect, event, True):
            anime_button(screen, icone_option2, (30, 30))
            fond_noir_transp(screen)
            affichage(screen, option)
            menu_actif = False
            option_actif = True
            jouer_actif = False
        elif bouton_clique(retour_rect, event, True):
            anime_button(screen, button_retour2, (565, 605))
            affichage(screen, menu)
            menu_actif = True
            option_actif = False
            jouer_actif = False
            stats_actif = False
            shop_actif = False
        elif bouton_clique(shop_rect, event, menu_actif):
            anime_button(screen, button_shop2, (798, 580))
            affichage(screen, shop)
            menu_actif = False
            option_actif = False
            shop_actif = True

pygame.quit()

