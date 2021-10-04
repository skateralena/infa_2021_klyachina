import pygame
from pygame.draw import*

pygame.init()
FPS = 30
screen = pygame.display.set_mode((400, 400))

def draw_house(x, y):
    rect(screen, (255, 0, 255), (x, y, 200, 200))
    rect(screen, (0, 0, 255), (x, y, 200, 200), 5)
    polygon(screen, (255, 255, 0), [(x, y), (x+100, y-50), (x+200, y), (x, y)])
    polygon(screen, (0, 255, 0), [(x, y), (x + 100, y - 50), (x + 200, y), (x, y)], 5)
    circle(screen, (0, 255, 0), (x+100, y + 75), 50)
    circle(screen, (255, 255, 255), (x + 100, y + 75), 50, 5)

clock = pygame.time.Clock()
finished = False

for i in range(0, 300):
    x = i
    y = i % 100
    if y < 50:
        y += 200
    else: y = 300 - y
    draw_house(x, y)
    pygame.display.update()
    clock.tick(100)


#draw_house(100, 100)
pygame.display.update()

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
