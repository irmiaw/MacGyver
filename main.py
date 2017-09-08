# bin/env python3
import pygame  # ne pas tout importer !!
# display, mixer, draw, event, image, mouse, time

# # import de me propres modules
# import game
# import draw
# import load

tile_size = 40

class MacGyver:
    x=0
    y=1 * tile_size



pygame.init()  # init de tous les modules
window = pygame.display.set_mode((15 * tile_size, 15 * tile_size)) # création d'une fenêtre
#fond = pygame.image.load("background.jpg").convert() # charger une image
brick = pygame.image.load("brick.png").convert_alpha() # charger une image avec fond transparent
floor = pygame.image.load("floor.png").convert_alpha()
mac_gyver = pygame.image.load("mac_gyver.png").convert_alpha()
guardian = pygame.image.load("murdoc.png").convert_alpha()
brick = pygame.transform.scale2x(brick)
floor = pygame.transform.scale2x(floor)
#image.set_colorkey((255,255,255)) # rendre le blanc (valeur RGB : 255,255,255) de l'image transparent
#fenetre.blit(brick, (320,240)) # coller une image sur la fenêtre

# '#': brick
# ' ': floor
# '.': guardian

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
       ["#", " ", "#", " ", "#", " ", "#", " ", " ", " ", " ", "#", " ", " ", "."],
       ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
]


num_line = 0
for line in map:
    num_column = 0
    for case in line:
        x = num_column * tile_size
        y = num_line * tile_size

        if case == "#":
            window.blit(brick, (x,y))
        elif case == " " or case == ".":
            window.blit(floor, (x,y))

        if case == ".":
            window.blit(guardian, (x,y))
        num_column += 1
    num_line += 1

window.blit(mac_gyver, (MacGyver.x ,MacGyver.y))


pygame.display.flip() # mettre à jour la fenêtre


# Boucle principale
continuer = 1
while continuer:
    continuer = int(input())

# if __name__ == "__main__":
    # do stuff
