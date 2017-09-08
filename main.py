#! /usr/bin/env python3
# coding: utf-8

import pygame  # ne pas tout importer !!
# display, mixer, draw, event, image, mouse, time

# # import de me propres modules
# import game
# import draw
# import load

pygame.init()  # init de tous les modules
fenetre = pygame.display.set_mode((640, 480)) # création d'une fenêtre
fond = pygame.image.load("background.jpg").convert() # charger une image
perso = pygame.image.load("perso.png").convert_alpha() # charger une image avec fond transparent
image.set_colorkey((255,255,255)) # rendre le blanc (valeur RGB : 255,255,255) de l'image transparent
fenetre.blit(fond, (0,0)) # coller une image sur la fenêtre
pygame.display.flip() # mettre à jour la fenêtre


# Boucle principale
continuer = 1
while continuer:
    continuer = int(input())

# if __name__ == "__main__":
    # do stuff
