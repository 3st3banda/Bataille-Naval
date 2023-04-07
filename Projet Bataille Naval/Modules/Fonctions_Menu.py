"""Import"""
import pygame

"""Button (Temp)"""
def bouton_clique(button, event):
    clique = False
    if event.type == pygame.MOUSEBUTTONDOWN:
        if button.collidepoint(event.pos):
            clique = True
    return clique


def anime_button(screen, button, pos_button, RGB_button):
    pygame.draw.rect(screen, RGB_button[0], button[0])
    screen.blit(button[1], pos_button)
    pygame.display.flip()
    pygame.time.wait(250)
    pygame.draw.rect(screen, RGB_button[1], button[0])
    screen.blit(button[1], pos_button)
    pygame.display.flip()
    pygame.time.wait(150)


def redimention(screen, ):
    width = int(int((screen.get_width()) - 600 )//2)
    return (width, 250)



