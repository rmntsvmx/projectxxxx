import pygame
import time
import random

pygame.init()

width = 1000
height = 800
block = 20


def draw_snake(snake_list):
    for coord in snake_list:
        pygame.draw.rect(window, (35, 123, 40), [coord[0], coord[1], block, block], 0)


window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake')

font = pygame.font.SysFont('Arial', 50)


def message(text, color):
    mess = font.render(text, True, color)
    window.blit(mess, [width // 4, height // 2])


def game():
    game_over = False

    x1 = width // 2
    y1 = height // 2
    x1_change = 0
    y1_change = 0
    foodx = round(random.randrange(0, width - block) / block) * block
    foody = round(random.randrange(0, height - block) / block) * block
    clock = pygame.time.Clock()

    len_of_snake = 1
    snake_list = []

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                pygame.quit()
            pygame.display.flip()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -20
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = 20
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -20
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = 20

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_over = True
        # if x1 > width:
        # x1 = 0
        # elif x1 <0:
        # x1 = width
        x1 += x1_change
        y1 += y1_change

        window.fill((0, 0, 0))
        pygame.draw.rect(window, (255, 0, 0), [foodx, foody, block, block], 0)
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > len_of_snake:
            del snake_list[0]

        for c in snake_list[:-1]:
            if c == snake_head:
                game_over == True

        draw_snake(snake_list)
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - block) / block) * block
            foody = round(random.randrange(0, height - block) / block) * block
            len_of_snake += 1
        snake = pygame.Rect(x1, y1, block, block)
        pygame.draw.rect(window, (35, 123, 40), snake, 0)
        pygame.display.update()
        clock.tick(18)

    message('Вы проиграли', (0, 100, 100))
    pygame.display.update()
    time.sleep(2)


game()
import pygame
import time
import random

pygame.init()

width = 1000
height = 800
block = 20
global c


def draw_snake(snake_list):
    for coord in snake_list:
        pygame.draw.rect(window, (35, 123, 40), [coord[0], coord[1], block, block], 0)


window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake')

font = pygame.font.SysFont('Arial', 50)


def message(text, color):
    mess = font.render(text, True, color)
    window.blit(mess, [width // 4, height // 2])


def game():
    game_over = False

    x1 = width // 2
    y1 = height // 2
    x1_change = 0
    y1_change = 0
    foodx = round(random.randrange(0, width - block) / block) * block
    foody = round(random.randrange(0, height - block) / block) * block
    clock = pygame.time.Clock()

    len_of_snake = 1
    snake_list = []

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                pygame.quit()
            pygame.display.flip()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -20
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = 20
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -20
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = 20

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_over = True
        # if x1 > width:
        # x1 = 0
        # elif x1 <0:
        # x1 = width
        x1 += x1_change
        y1 += y1_change

        window.fill((0, 0, 0))
        pygame.draw.rect(window, (255, 0, 0), [foodx, foody, block, block], 0)
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > len_of_snake:
            del snake_list[0]

        for c in snake_list[:-1]:
            if c == snake_head:
                game_over == True

        draw_snake(snake_list)
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - block) / block) * block
            foody = round(random.randrange(0, height - block) / block) * block
            len_of_snake += 1
        snake = pygame.Rect(x1, y1, block, block)
        pygame.draw.rect(window, (35, 123, 40), snake, 0)
        pygame.display.update()
        clock.tick(18)

    message('Вы проиграли', (0, 100, 100))
    pygame.display.update()
    time.sleep(2)


game()
