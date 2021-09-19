import pygame
from pygame.draw import *

def main():
    pygame.init()

    FPS = 30
    screen = pygame.display.set_mode((400, 400))

    rect(screen, (200, 200, 200), (0, 0, 400, 400))
    circle(screen, (250, 250, 0), (200, 200), 100)
    circle(screen, (0, 0, 0), (200, 200), 100, 1)

    circle(screen, (250, 0, 0), (150, 180), 20)
    circle(screen, (0, 0, 0), (150, 180), 20, 1)
    circle(screen, (0, 0, 0), (150, 180), 8)

    circle(screen, (250, 0, 0), (250, 180), 15)
    circle(screen, (0, 0, 0), (250, 180), 15, 1)
    circle(screen, (0, 0, 0), (250, 180), 7)

    polygon(screen, (0, 0, 0), [(103, 117), (98, 124), (177, 174), (182, 167), (103, 117)])
    polygon(screen, (0, 0, 0), [(223, 174), (302, 144), (298, 136), (220, 165), (223, 174)])
    rect(screen, (0, 0, 0), (150, 250, 100, 20))

    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False

    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

    pygame.quit()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
