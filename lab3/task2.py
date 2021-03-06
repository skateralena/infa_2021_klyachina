import pygame
from pygame.draw import *

def transform(t, a, b):
    # для каждого элемента x из t вычислить ax+b и возвратить, как tuple
    return tuple(x * a + b for x in t)

def p(x, y, ax, bx, ay, by):
    return (x * ax + bx, y * ay + by)

def house(dest, brightness = 1, scale = 1):
    rect(dest, 'white', (0, 0, 600, 700))
    color = (40 * brightness, 34 * brightness, 10 * brightness)
    rect(dest, color, (33 * scale, 144 * scale, 417 * scale, 566 * scale))

    t = (0, 145, 60, 100, 420, 100, 490, 145, 0, 145)
    x = transform(t[::2], scale, 0)
    y = transform(t[1::2], scale, 0)
    polygon(dest, 'black', tuple(zip(x, y)))

    color = (26 * brightness, 26 * brightness, 26 * brightness)
    rect(dest, color, (93 * scale, 60 * scale, 17 * scale, 62 * scale))
    rect(dest, color, (282 * scale, 71 * scale, 13 * scale,30 * scale))
    color = (51 * brightness, 51 * brightness, 51 * brightness)
    ellipse(dest, color, (31 * scale, 2 * scale, 600 * scale, 74 * scale))
    color = (26 * brightness, 26 * brightness, 26 * brightness)
    rect(dest, color, (117 * scale, 0 * scale, 30 * scale, 130 * scale))
    rect(dest, color, (385 * scale, 42 * scale, 15 * scale, 86 * scale))

    color = (72 * brightness, 62 * brightness, 55 * brightness)
    rect(dest, color, (63 * scale, 146 * scale, 46 * scale, 214 * scale))
    rect(dest, color, (145 * scale, 146 * scale, 46 * scale, 214 * scale))
    rect(dest, color, (247 * scale, 146 * scale, 46 * scale, 214 * scale))
    rect(dest, color, (355 * scale, 146 * scale, 46 * scale, 214 * scale))

    color = (26 * brightness, 26 * brightness, 26 * brightness)
    rect(dest, color, (17 * scale, 290 * scale, 455 * scale, 26 * scale))
    rect(dest, color, (3 * scale, 316 * scale, 14 * scale, 51 * scale))
    rect(dest, color, (472 * scale, 316 * scale, 14 * scale, 51 * scale))
    rect(dest, color, (57 * scale, 316 * scale, 26 * scale, 51 * scale))
    rect(dest, color, (134 * scale, 316 * scale, 26 * scale, 51 * scale))
    rect(dest, color, (211 * scale, 316 * scale, 26 * scale, 51 * scale))
    rect(dest, color, (301 * scale, 316 * scale, 26 * scale, 51 * scale))
    rect(dest, color, (389 * scale, 316 * scale, 26 * scale, 51 * scale))
    rect(dest, color, (0 * scale, 366 * scale, 498 * scale, 58 * scale))

    color = (43 * brightness, 17 * brightness, 0 * brightness)
    rect(dest, color, (80 * scale, 550 * scale, 80 * scale, 100 * scale))
    rect(dest, color, (206 * scale, 550 * scale, 80 * scale, 100 * scale))
    color = (212 * brightness, 170 * brightness, 0 * brightness)
    rect(dest, color, (325 * scale, 550 * scale, 80 * scale, 100 * scale))


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
    screen = pygame.display.set_mode((500, 650))

    rect(screen, (102, 102, 102), (0, 0, 500, 300))
    circle(screen, (255, 255, 255), (415, 75), 45)
    ellipse(screen, (26, 26, 26), (250, 165, 300, 50))


    surf1 = pygame.Surface((225, 206))
    surf2 = pygame.Surface((225, 206))
    surfHouse1 = pygame.Surface((565, 700))

    ghost(surf1, 1, 0.6, 1)
    #ghost(screen, 0.5, 0.5, 1)
    ghost(surf2, 0.5, 0.5, -1)
    screen.blit(surf1, (350, 480), special_flags=pygame.BLEND_ADD)
    #screen.blit(surf2, (0, 0), special_flags=pygame.BLEND_ADD)
    house(surfHouse1, 1, 0.6)
    surfHouse1.set_colorkey('white')
    surfHouse1.set_alpha(500)
    screen.blit(surfHouse1, (0, 80), special_flags=pygame.BLEND_ALPHA_SDL2)

    ellipse(screen, (77, 77, 77), (200, 55, 300, 50))
    ellipse(screen, (77, 77, 77), (300, 110, 400, 50))

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
