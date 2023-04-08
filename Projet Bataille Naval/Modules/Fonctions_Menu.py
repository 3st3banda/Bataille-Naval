"""Import"""
import pygame

def bouton_clique(button, event):
    """
        button -> objet: Rect
        event -> Event

        Défini si l'utilisateur à cliquer sur la surface Rect
    """
    clique = False
    if event.type == pygame.MOUSEBUTTONDOWN:
        if button.collidepoint(event.pos):
            clique = True
    return clique


def redimention(images):
    """
        images -> list: [(image initiale, coordonnées(x, y) voulu)]
        
        Prend une liste d'images et les redimentionnent avec la taille voulu
    """
    img_redim = []
    for i in range(len(images)):
        if images[i][1] == False:
            img_redim.append(images[i][0])
        else:
            img_redim.append(pygame.transform.scale(images[i][0], images[i][1]))
    return img_redim


def affiche_images(screen, images):
    """
        screen -> Surface
        images -> list:
            [(image à afficher, 
            Taille souhaité de l'image -> (x, y) ou False: si on ne désire pas redimentionné l'image
            Position de l'image dans la fenetre -> (x, y)
            )]

        Affiche l'ensemble des images
    """
    img_resize = redimention(images)
    for i in range(len(img_resize)):
        screen.blit(img_resize[i], images[i][2])
    

def fond_noir_transp(screen):
    """
        screen -> Surface

        Asombrissement de la fenetre
    """
    # Création d'une surface noire avec un alpha 
    fond_noir = pygame.Surface((screen.get_width(), screen.get_height()), pygame.SRCALPHA)
    fond_noir.fill((0, 0, 0, 230))
    screen.blit(fond_noir, (0, 0))
    pygame.display.flip()



