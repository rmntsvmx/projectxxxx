import pygame
import time
import random

pygame.init()

width = 600
height = 600
block = 50

font_large = pygame.font.SysFont('Arial', 60, bold=True)
font_medium = pygame.font.SysFont('Arial', 40, bold=True)
font_small = pygame.font.SysFont('Arial', 25)

green = (0, 177, 45)
light_green = (34, 191, 17)
red = (199, 5, 0)
white = (255, 255, 255)
black = (0, 0, 0)
gold = (255, 215, 0)

window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake')

font = pygame.font.SysFont('Arial', 50)

def message(text, color, x, y, font):
    mess = font.render(text, True, color)
    text_rect = mess.get_rect(center=(x, y))
    window.blit(mess, text_rect)


def draw_grid():
    for row in range(0, width, block):
        for col in range(0, height, block):
            rect_color = green if (row // block + col // block) % 2 == 0 else light_green
            pygame.draw.rect(window, rect_color, [row, col, block, block])


def draw_snake(snake_list):
    for coord in snake_list:
        pygame.draw.rect(window, (0, 24, 156), [coord[0], coord[1], block, block], 0)


def game_over_screen(score):
    window.fill(black)
    message("Вы проиграли!", red, width // 2, height // 3, font_large)
    message(f"Ваш счёт: {score}", gold, width // 2, height // 2, font_medium)
    message("Возврат в меню...", white, width // 2, height // 1.5, font_small)
    pygame.display.flip()
    time.sleep(2)


def game():
    x1 = width // 2
    y1 = height // 2
    x1_change = 0
    y1_change = 0
    foodx = round(random.randrange(0, width - block) / block) * block
    foody = round(random.randrange(0, height - block) / block) * block
    clock = pygame.time.Clock()

    snake_list = []
    len_of_snake = 1
    score = 0

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                pygame.quit()
            pygame.display.flip()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = block

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_over = True

        x1 += x1_change
        y1 += y1_change

        snake_head = [x1, y1]
        snake_list.append(snake_head)

        if len(snake_list) > len_of_snake:
            del snake_list[0]


        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - block) / block) * block
            foody = round(random.randrange(0, height - block) / block) * block
            len_of_snake += 1
            score += 1

        draw_grid()
        pygame.draw.rect(window, red, [foodx, foody, block, block], 0)
        draw_snake(snake_list)


        pygame.draw.rect(window, black, [0, 0, width, 40])
        message(f"Счёт: {score}", white, width // 10, 20, font_small)

        pygame.display.update()
        clock.tick(10)

    game_over_screen(score)


game()
