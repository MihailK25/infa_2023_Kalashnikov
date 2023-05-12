import pygame
from pygame.draw import *

pygame.init()
FPS=30
screen = pygame.display.set_mode((400, 600))
#background
rect(screen, (0,255,247), (0,0,400,300))
rect(screen, (0,255,0), (0,300,400,300))
pygame.draw.circle(screen, (255,230,80), (385,75), 85 )
#tree
rect(screen, (255,255,255), (40,225,40,200))
ellipse(screen, (0,150,10),[-35, 220, 200, 95], 0)
ellipse(screen, (0,150,10),[5, 130, 110, 140], 0)
ellipse(screen, (0,150,10),[5, 290, 110, 80], 0)
ellipse(screen, (255,190,230),[70, 170, 30, 25], 0)
ellipse(screen, (255,190,230),[115, 260, 30, 25], 0)
ellipse(screen, (255,190,230),[-10, 255, 30, 25], 0)
ellipse(screen, (255,190,230),[70, 330, 30, 25], 0)
#unicorn
ellipse(screen, (255,255,255),[200, 400, 150, 60], 0)
rect(screen, (255,255,255), (300, 340, 35, 75))
ellipse(screen, (255,255,255), [295, 335, 80, 30])
ellipse(screen, (255,255,255), [300, 325, 50, 50])
polygon(screen, (255,115,220), ([315,325], [330,327], [328, 270]))
ellipse(screen, (255,115,220), [328, 340, 15,12])
rect(screen, (255,255,255), (220, 450, 13, 50))
rect(screen, (255,255,255), (240, 450, 13, 50))
rect(screen, (255,255,255), (290, 450, 13, 50))
rect(screen, (255,255,255), (310, 450, 13, 50))
#eye
ellipse(screen, (255,115,220), [328, 340, 15,12])
ellipse(screen, (0,0,0), [336, 344, 6,5])
polygon(screen, (255,255,255), ([338,345], [336,347], [333,344], [334, 342]))
#hair
ellipse(screen, (255,150,255), [295, 320, 30,12]) #pink
ellipse(screen, (150,255,255), [293, 327, 30,12]) #blue
ellipse(screen, (255,255,80), [285, 332, 30,12])  #yellow
ellipse(screen, (255,150,255), [281, 339, 30,12])
ellipse(screen, (255,150,255), [279, 346, 40,20])
ellipse(screen, (255,255,80), [277, 353, 38, 12])
ellipse(screen, (255,255,80), [280, 360, 35,25])
ellipse(screen, (150,255,255), [273, 367, 38,12])
ellipse(screen, (150,255,255), [268, 374, 45,18])
ellipse(screen, (255,150,255), [269, 381, 30,12])
ellipse(screen, (255,255,80), [267, 388, 40,20])
#tail
ellipse(screen, (255,150,255), [200, 400, 30,12]) #pink
ellipse(screen, (150,255,255), [198, 407, 30,12]) #blue
ellipse(screen, (255,255,80), [190, 412, 30,12])  #yellow
ellipse(screen, (255,150,255), [186, 419, 30,12])
ellipse(screen, (255,150,255), [184, 416, 40,20])
ellipse(screen, (255,255,80), [182, 433, 38, 12])
ellipse(screen, (255,255,80), [185, 440, 35,25])
ellipse(screen, (150,255,255), [178, 447, 38,12])
ellipse(screen, (150,255,255), [172, 454, 45,18])
ellipse(screen, (255,150,255), [174, 461, 30,12])
ellipse(screen, (255,255,80), [172, 468, 40,20])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()