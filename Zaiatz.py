import pygame
from pygame.draw import *

pygame.init()
pygame.display.set_caption('Body Кролитос')  # кастомное название окна
FPS = 30  # частота кадров

# Цвета
blue = (80, 208, 255)
black = (0, 0, 0)
grey = (184, 184, 184)
nedogrey = (120, 104, 104)
bur = (94, 73, 73)
bodyy = (145, 125, 125)
white = (255, 255, 255)
pink = (255,208,160)
red = (255 ,0 ,0)

# Разрешение окна 800x600
screen = pygame.display.set_mode((800, 600))

screen.fill((blue))  # заливка фона у этого мужчины

f1 = pygame.font.Font(None, 36)
text1 = f1.render('Body позитивный Заяц', 1, red)  # цвет шрифта

screen.blit(text1, (10, 50))


def draw_body(screen, x, y, width, height, color):
    '''
    Рисует тело зайца.
    surface - объект pygame.Surface
    x, y - координаты центра изображения
    width, height - ширина и высота изобажения
    color - цвет, заданный в формате, подходящем для pygame.Color
    '''
    ellipse(screen, color, (x - width // 2, y - height // 2, width, height))


def draw_head(surface, x, y, size, color):
    '''
    Рисует голову зайца.
    surface - объект pygame.Surface
    x, y - координаты центра изображения
    size - диаметр головы
    color - цвет, заданный в формате, подходящем для pygame.Color
    '''
    circle(surface, color, (x, y), size // 2)


def draw_ear(surface, x, y, width, height, color):
    '''
    Рисует уши зайца.
    surface - объект pygame.Surface
    x, y - координаты центра изображения
    width, height - ширина и высота изобажения
    color - цвет, заданный в формате, подходящем для pygame.Color
    '''
    ellipse(surface, color, (x - width // 2, y - height // 2, width, height))


def draw_leg(surface, x, y, width, height, color):
    '''
    Рисует лапы зайца.
    surface - объект pygame.Surface
    x, y - координаты центра изображения
    width, height - ширина и высота изобажения
    color - цвет, заданный в формате, подходящем для pygame.Color
    '''
    ellipse(surface, color, (x - width // 2, y - height // 2, width, height))


def draw_eye(surface, x, y, width, height, color):
    '''
    Рисует глаза зайца.
    surface - объект pygame.Surface
    x, y - координаты центра изображения
    width, height - ширина и высота изобажения
    color - цвет, заданный в формате, подходящем для pygame.Color
    '''
    ellipse(surface, color, (x - width // 2, y - height // 2, width, height))


def draw_os(surface, x, y, width, height, color):
    '''
    Рисует рот зайца.
    surface - объект pygame.Surface
    x, y - координаты центра изображения
    width, height - ширина и высота изобажения
    color - цвет, заданный в формате, подходящем для pygame.Color
    '''
    ellipse(surface, color, (x - width // 2, y - height // 2, width, height))


# Отрисовка зайца
draw_body(screen, 400, 410, 350, 300, white)  # тело кроля

draw_ear(screen, 360, 100, 60, 140, pink)  # левое ухо
draw_ear(screen, 440, 100, 60, 140, pink)  # правое ухо

draw_head(screen, 400, 200, 180, white)  # голова кроля

draw_leg(screen, 240, 340, 80, 50, pink)  # левая верхняя лапа
draw_leg(screen, 560, 340, 80, 50, pink)  # правая верхняя лапа

draw_leg(screen, 317, 550, 100, 80, pink)  # левая нижняя лапа
draw_leg(screen, 485, 550, 100, 80, pink)  # правая нижняя лапа

draw_eye(screen, 363, 180, 15, 10, black)  # правый зрачок
draw_eye(screen, 438, 180, 15, 10, black)  # левый зрачок

draw_os(screen, 400, 230, 40, 40, grey)  # рот

draw_ear(screen, 396, 218, 7, 15, white)  # верхний левый зуб
draw_ear(screen, 405, 218, 7, 15, white)  # верхний правый зуб
draw_ear(screen, 405, 242, 7, 15, white)  # нижний левый зуб
draw_ear(screen, 396, 242, 7, 15, white)  # нижний правый зуб

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()