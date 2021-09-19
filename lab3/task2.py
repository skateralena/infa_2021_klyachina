import pygame
from pygame.draw import *

def transform(t, a, b):
    # для каждого элемента x из t вычислить ax+b и возвратить, как tuple
    return tuple(x * a + b for x in t)

def p(x, y, ax, bx, ay, by):
    return (x * ax + bx, y * ay + by)

def ghost(dest, brightness = 1, scale = 1, flip = 1):
    t = (55, 46, 121, 21, 135, 24, 167, 51, 169, 52, 198, 80, 214, 90, 221, 97, 224, 111, 225, 127, 220, 134,
         212, 136, 199, 139, 192, 143, 187, 155, 185, 164, 176, 179, 151, 180, 138, 176, 123, 183, 108, 198,
         98, 204, 89, 207, 81, 205, 65, 184, 57, 179, 37, 168, 29, 169, 2, 173, 0, 173, 0, 170, 10, 155,
         16, 136, 32, 112, 39, 99, 41, 94, 49, 78, 55, 46)
    color = (brightness * 179, brightness * 179, brightness * 179)
    ax = scale * flip
    bx = 225 * scale if flip < 0 else 0
    ay = scale
    by = 0
    x = transform(t[::2], ax, bx)
    y = transform(t[1::2], ay, by)
    polygon(dest, color, tuple(zip(x, y)))
    circle(dest, color, p(92, 38, ax, bx, ay, by), 38 * scale)

    color = (brightness * 135, brightness * 205, brightness * 222)
    circle(dest, color, p(70, 31, ax, bx, ay, by), 10 * scale)
    circle(dest, color, p(102, 27, ax, bx, ay, by), 10 * scale)
    color = "black"
    circle(dest, color, p(67, 32, ax, bx, ay, by), 3 * scale)
    circle(dest, color, p(98, 26, ax, bx, ay, by), 3 * scale)
    color = (brightness * 255, brightness * 255, brightness * 255)
    t = (68, 31, 68, 29, 75, 25, 77, 25, 77, 28, 71, 31, 68, 31)
    x = transform(t[::2], ax, bx)
    y = transform(t[1::2], ay, by)
    polygon(dest, color, tuple(zip(x, y)))
    t = (100, 26, 100, 24, 106, 20, 108, 20, 108, 22, 102, 26, 100, 26)
    x = transform(t[::2], ax, bx)
    y = transform(t[1::2], ay, by)
    polygon(dest, color, tuple(zip(x, y)))

def main():
    pygame.init()

    FPS = 30
    screen = pygame.display.set_mode((400, 400))

    surf1 = pygame.Surface((225, 206))
    surf2 = pygame.Surface((225, 206))

    ghost(surf1, 0.8, 1, 1)
    #ghost(screen, 0.5, 0.5, 1)
    ghost(surf2, 0.5, 0.5, -1)
    screen.blit(surf1, (0, 0), special_flags=pygame.BLEND_ADD)
    screen.blit(surf2, (0, 0), special_flags=pygame.BLEND_ADD)

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
