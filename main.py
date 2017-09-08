# bin/env python3
import pygame  # ne pas tout importer !!
# display, mixer, draw, event, image, mouse, time

# # import de me propres modules
# import game
# import draw
# import load

pygame.init()  # init de tous les modules
window = pygame.display.set_mode((640, 480)) # création d'une fenêtre
#fond = pygame.image.load("background.jpg").convert() # charger une image
brick = pygame.image.load("brick.png").convert_alpha() # charger une image avec fond transparent
floor = pygame.image.load("floor.png").convert_alpha()
#image.set_colorkey((255,255,255)) # rendre le blanc (valeur RGB : 255,255,255) de l'image transparent
#fenetre.blit(brick, (320,240)) # coller une image sur la fenêtre

map = [["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
       [" ", " ", " ", " ", " ", " ", "#", " ", " ", "#", " ", " ", " ", " ", " "],
       ["#", " ", " ", "#", "#", " ", "#", " ", "#", "#", " ", "#", " ", " ", "#"],
       ["#", " ", "#", " ", " ", "#", "#", " ", " ", " ", " ", "#", "#", "#", "#"],
       ["#", " ", " ", " ", " ", "#", " ", "#", " ", "#", "#", "#", " ", "#", "#"],
       ["#", " ", " ", "#", " ", "#", " ", "#", " ", " ", " ", "#", " ", " ", " "],
       ["#", " ", "#", "#", " ", "#", " ", " ", "#", "#", " ", " ", " ", "#", " "],
       ["#", " ", "#", "#", " ", " ", "#", " ", " ", "#", "#", "#", " ", "#", " "],
       ["#", " ", " ", " ", "#", " ", " ", "#", " ", " ", " ", " ", "#", " ", " "],
       ["#", "#", "#", " ", " ", "#", " ", "#", "#", "#", " ", "#", "#", " ", "#"],
       ["#", " ", " ", "#", " ", "#", " ", "#", " ", "#", " ", " ", " ", " ", "#"],
       ["#", "#", " ", "#", " ", "#", "#", " ", " ", "#", "#", "#", " ", "#", "#"],
       ["#", " ", " ", " ", " ", " ", " ", " ", "#", "#", " ", " ", " ", "#", "#"],
       ["#", " ", "#", " ", "#", " ", "#", " ", " ", " ", " ", "#", " ", " ", " "],
       ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
]

tile_size = 20

num_line = 0
for line in map:
    num_column = 0
    for case in line:
        x = num_column * tile_size
        y = num_line * tile_size
        if case == "#":
            window.blit(brick, (x,y))
        elif case == " ":
            window.blit(floor, (x,y))
        num_column += 1
    num_line += 1

pygame.display.flip() # mettre à jour la fenêtre


# Boucle principale
continuer = 1
while continuer:
    continuer = int(input())

# if __name__ == "__main__":
    # do stuff
