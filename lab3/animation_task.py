import pygame
from pygame.draw import *

def main():
    pygame.init()

    FPS = 30
    screen = pygame.display.set_mode((500, 650))

    background(screen)

    surf1 = pygame.Surface((225, 206))
    surf2 = pygame.Surface((225, 206))
    surf3 = pygame.Surface((225, 206))
    surfHouse1 = pygame.Surface((565, 700))

    ghost(surf1, 0.6, 1)
    surf1.set_colorkey('green')
    surf1.set_alpha(255)
    ghost(surf2, 0.3, 1)
    surf2.set_colorkey('green')
    surf2.set_alpha(200)
    ghost(surf3, 0.3, -1)
    surf3.set_colorkey('green')
    surf3.set_alpha(200)
    screen.blit(surf1, (350, 480), special_flags=pygame.BLEND_ALPHA_SDL2)
    screen.blit(surf2, (320, 500), special_flags=pygame.BLEND_ALPHA_SDL2)
    screen.blit(surf2, (400, 400), special_flags=pygame.BLEND_ALPHA_SDL2)
    screen.blit(surf2, (420, 430), special_flags=pygame.BLEND_ALPHA_SDL2)
    screen.blit(surf3, (50, 530), special_flags=pygame.BLEND_ALPHA_SDL2)
    screen.blit(surf3, (70, 560), special_flags=pygame.BLEND_ALPHA_SDL2)

    #screen.blit(surf2, (0, 0), special_flags=pygame.BLEND_ADD)
    #house(surfHouse1, 1, 0.3)
    house(surfHouse1, 0.3)
    surfHouse1.set_colorkey('green')
    surfHouse1.set_alpha(200)
    screen.blit(surfHouse1, (160, 226), special_flags=pygame.BLEND_ALPHA_SDL2)
    surfHouse1.set_alpha(150)
    screen.blit(surfHouse1, (350, 132), special_flags=pygame.BLEND_ALPHA_SDL2)
    surfHouse1.set_alpha(500)
    screen.blit(surfHouse1, (0, 294), special_flags=pygame.BLEND_ALPHA_SDL2)

    ellipse(screen, (77, 77, 77), (300, 105, 400, 40))
    #rect(screen, (0, 0, 0), (0, 0, 100, 100))
    animation(screen, 100)


def animation(screen, FPS):
    #rect(screen, (0, 0, 0), (0, 0, 100, 100))
    surf1 = pygame.Surface((225, 206))
    surf1.set_colorkey('green')
    surf1.set_alpha(255)

    surf2 = pygame.Surface((225, 206))
    surf2.set_colorkey('green')
    surf2.set_alpha(200)

    surf3 = pygame.Surface((225, 206))
    surf3.set_colorkey('green')
    surf3.set_alpha(200)

    surfHouse1 = pygame.Surface((565, 700))

    surfHouse1.set_colorkey('green')
    surfHouse1.set_alpha(200)

    clock = pygame.time.Clock()
    finished = False
    for i in range(0, 500):
        x = i
        background(screen)
        clouds(screen, x, 0)
        ghost(surf1, 0.6 + 0.001*i, 1)
        screen.blit(surf1, (350 - x, 480), special_flags=pygame.BLEND_ALPHA_SDL2)
        ghost(surf2, 0.3-0.0005*i, 1)
        screen.blit(surf2, (320-0.1*i, 500), special_flags=pygame.BLEND_ALPHA_SDL2)
        ghost(surf3, 0.3+0.001*i, -1)
        screen.blit(surf3, (50 + 1.5*x, 530), special_flags=pygame.BLEND_ALPHA_SDL2)
        screen.blit(surf3, (70 + x, 560), special_flags=pygame.BLEND_ALPHA_SDL2)
        if i % 400 < 200:
            surfHouse1.set_alpha(300 - x % 200)
        else:
            surfHouse1.set_alpha(100 + x % 200)
        house(surfHouse1, 0.3)
        screen.blit(surfHouse1, (160, 226), special_flags=pygame.BLEND_ALPHA_SDL2)
        surfHouse1.set_alpha(150)
        house(surfHouse1, 0.3)
        screen.blit(surfHouse1, (350, 132), special_flags=pygame.BLEND_ALPHA_SDL2)

        pygame.display.update()
        clock.tick(FPS)
        #rect(screen, (0, 0, 0), (0, 0, 100, 100))

    pygame.display.update()
    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

    pygame.quit()

def background(dest):
    """
    Функция рисует задний фон
    :param dest: поверхность, на которой будет нарисован фон
    :return:
    """
    rect(dest, (0, 0, 0), (0, 0, 500, 650))
    rect(dest, (102, 102, 102), (0, 0, 500, 300))
    circle(dest, (255, 255, 255), (415, 73), 45)

def clouds(dest, x, y):
    ellipse(dest, (51, 51, 51), (x + 10, y + 75, 380, 40))
    ellipse(dest, (77, 77, 77), (x + 200, y + 55, 300, 45))
    ellipse(dest, (77, 77, 77), (x + 80, y + 280, 450, 40))
    ellipse(dest, (26, 26, 26), (x + 250, y + 165, 300, 50))
    ellipse(dest, (26, 26, 26), (x + 210, y + 333, 400, 50))
    ellipse(dest, (42, 42, 42), (x -150, y + 373, 400, 45))

def ghost(dest, scale = 1, flip = 1):
    """
    Функция рисует привидение
    :param dest: поверхность, на которой будет отрисовано привидение
    :param scale: масштаб привидения, относительно исходного
    :param flip: принимает значение -1, если изображение отражено, и +1, если исходное
    :return:
    """
    rect(dest, 'green', (0, 0, 225, 206))

    #отрисовка тела привидения
    t = (55, 46, 121, 21, 135, 24, 167, 51, 169, 52, 198, 80, 214, 90, 221, 97, 224, 111, 225, 127, 220, 134,
         212, 136, 199, 139, 192, 143, 187, 155, 185, 164, 176, 179, 151, 180, 138, 176, 123, 183, 108, 198,
         98, 204, 89, 207, 81, 205, 65, 184, 57, 179, 37, 168, 29, 169, 2, 173, 0, 173, 0, 170, 10, 155,
         16, 136, 32, 112, 39, 99, 41, 94, 49, 78, 55, 46)
    color = (179, 179, 179)
    ax = scale * flip
    bx = 225 * scale if flip < 0 else 0
    ay = scale
    by = 0
    x = transform(t[::2], ax, bx)
    y = transform(t[1::2], ay, by)
    polygon(dest, color, tuple(zip(x, y)))
    circle(dest, color, p(92, 38, ax, bx, ay, by), 38 * scale)

    #глаза привидения
    color = (135, 205, 222)
    circle(dest, color, p(70, 31, ax, bx, ay, by), 10 * scale)
    circle(dest, color, p(102, 27, ax, bx, ay, by), 10 * scale)
    color = "black"
    circle(dest, color, p(67, 32, ax, bx, ay, by), 4 * scale)
    circle(dest, color, p(99, 27, ax, bx, ay, by), 3.4 * scale)
    color = (255, 255, 255)
    t = (69, 31, 69, 29, 75, 25, 77, 25, 77, 28, 71, 31, 69, 31)
    x = transform(t[::2], ax, bx)
    y = transform(t[1::2], ay, by)
    polygon(dest, color, tuple(zip(x, y)))
    t = (100, 26, 100, 24, 106, 20, 108, 20, 108, 22, 102, 26, 100, 26)
    x = transform(t[::2], ax, bx)
    y = transform(t[1::2], ay, by)
    polygon(dest, color, tuple(zip(x, y)))

def transform(t, a, b):
    """
    Функция преобразует координаты
    :param t: исходные коотдинаты
    :param a: увеличение координаты
    :param b: сдвиг
    :return:
    """
    # для каждого элемента x из t вычислить ax+b и возвратить, как tuple
    return tuple(x * a + b for x in t)

def p(x, y, ax, bx, ay, by):
    """
    Функция преобразует координаты для правильного масштабирования
    """
    return (x * ax + bx, y * ay + by)

def house(dest, scale = 1):
    """
    Функция рисует дом
    :param dest: поверхность, на которую он отображается
    :param scale: масштаб
    :return:
    """
    rect(dest, 'green', (0, 0, 600, 700))
    color = (40, 34, 10)
    rect(dest, color, (33 * scale, 144 * scale, 417 * scale, 566 * scale))

    t = (0, 145, 60, 100, 420, 100, 490, 145, 0, 145)
    x = transform(t[::2], scale, 0)
    y = transform(t[1::2], scale, 0)
    polygon(dest, 'black', tuple(zip(x, y)))

    #отрисовка труб + облако дыма(если надо)
    color = (26, 26, 26)
    rect(dest, color, (93 * scale, 60 * scale, 17 * scale, 62 * scale))
    rect(dest, color, (282 * scale, 71 * scale, 13 * scale, 30 * scale))
    #color = (51, 51, 51)
    #ellipse(dest, color, (31 * scale, 2 * scale, 600 * scale, 74 * scale))
    color = (26, 26, 26)
    rect(dest, color, (117 * scale, 0 * scale, 30 * scale, 130 * scale))
    rect(dest, color, (385 * scale, 42 * scale, 15 * scale, 86 * scale))

    #отрисовка окон верхнего этажа
    color = (72, 62, 55)
    rect(dest, color, (63 * scale, 146 * scale, 46 * scale, 214 * scale))
    rect(dest, color, (145 * scale, 146 * scale, 46 * scale, 214 * scale))
    rect(dest, color, (247 * scale, 146 * scale, 46 * scale, 214 * scale))
    rect(dest, color, (355 * scale, 146 * scale, 46 * scale, 214 * scale))

    #отрисовка балкончика
    color = (26, 26, 26)
    rect(dest, color, (17 * scale, 290 * scale, 455 * scale, 26 * scale))
    rect(dest, color, (3 * scale, 316 * scale, 14 * scale, 51 * scale))
    rect(dest, color, (472 * scale, 316 * scale, 14 * scale, 51 * scale))
    rect(dest, color, (57 * scale, 316 * scale, 26 * scale, 51 * scale))
    rect(dest, color, (134 * scale, 316 * scale, 26 * scale, 51 * scale))
    rect(dest, color, (211 * scale, 316 * scale, 26 * scale, 51 * scale))
    rect(dest, color, (301 * scale, 316 * scale, 26 * scale, 51 * scale))
    rect(dest, color, (389 * scale, 316 * scale, 26 * scale, 51 * scale))
    rect(dest, color, (0 * scale, 366 * scale, 498 * scale, 58 * scale))

    #отрисовка окон первого этажа
    color = (43, 17, 0)
    rect(dest, color, (80 * scale, 550 * scale, 80 * scale, 100 * scale))
    rect(dest, color, (206 * scale, 550 * scale, 80 * scale, 100 * scale))
    color = (212, 170, 0)
    rect(dest, color, (325 * scale, 550 * scale, 80 * scale, 100 * scale))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()