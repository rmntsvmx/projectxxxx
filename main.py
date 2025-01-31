import pygame
import sys

from button import ImageButton

pygame.init()

WIDTH, HEIGHT = 600, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu")
main_background = pygame.image.load("background.jpg")
main_background = pygame.transform.scale(main_background, (WIDTH, HEIGHT))

rocket_button = ImageButton(WIDTH / 2 - (297 / 4), 300, 297 / 2, 128 / 2, 'Метеориты', 'button1.png', 'button12.png',
                            'click.mp3')
snake_button = ImageButton(WIDTH / 2 - (297 / 4), 200, 297 / 2, 128 / 2, 'Змейка', 'button1.png', 'button12.png',
                           'click.mp3')
exit_button = ImageButton(WIDTH / 2 - (297 / 4), 500, 297 / 2, 128 / 2, 'Выход', 'button1.png', 'button12.png',
                          'click.mp3')
wordle_button = ImageButton(WIDTH / 2 - (297 / 4), 400, 297 / 2, 128 / 2, 'Вордли', 'button1.png', 'button12.png',
                            'click.mp3')


def main_menu():
    pygame.init()
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(main_background, (0, 0))

        font = pygame.font.Font(None, 72)
        text_surface = font.render("СБОРНИК ИГР", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH / 2, 100))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            wordle_button.check_hover(pygame.mouse.get_pos())
            rocket_button.check_hover(pygame.mouse.get_pos())
            exit_button.check_hover(pygame.mouse.get_pos())
            snake_button.check_hover(pygame.mouse.get_pos())

        if event.type == pygame.USEREVENT and event.button == snake_button:
            snake_game()

        if event.type == pygame.USEREVENT and event.button == rocket_button:
            rocket_game()

        if event.type == pygame.USEREVENT and event.button == exit_button:
            running = False


        wordle_button.handle_event(event)
        wordle_button.draw(screen)


        rocket_button.handle_event(event)
        rocket_button.draw(screen)


        exit_button.handle_event(event)
        exit_button.draw(screen)


        snake_button.handle_event(event)
        snake_button.draw(screen)
        pygame.display.flip()


def snake_game():
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
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Menu")
    main_background = pygame.image.load("background.jpg")
    main_background = pygame.transform.scale(main_background, (WIDTH, HEIGHT))


def rocket_game():
    import pygame
    import random

    pygame.init()

    WIDTH = 600
    HEIGHT = 400
    SPEED = 5
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Shooter')
    back = pygame.image.load('starfield.jpg').convert()
    back_rect = back.get_rect()
    player_img = pygame.image.load('rocket.jpg').convert()
    meteor_img = pygame.image.load('meteor.jpg').convert()
    lazer_img = pygame.image.load('laser.jpg').convert()
    clock = pygame.time.Clock()

    class Player(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.transform.scale(player_img, (50, 60))
            self.image.set_colorkey((0, 0, 0))
            self.rect = self.image.get_rect()
            self.rect.centerx = WIDTH / 2
            self.rect.bottom = HEIGHT - 5
            self.speedx = 0
            self.hp = 100

        def update(self):
            self.speedx = 0
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_LEFT]:
                self.speedx = -5
            if keystate[pygame.K_RIGHT]:
                self.speedx = 5
            self.rect.x += self.speedx
            if self.rect.right > WIDTH:
                self.rect.right = WIDTH
            if self.rect.left < 0:
                self.rect.left = 0

        def shot(self):
            bullet = Bullet(self.rect.centerx, self.rect.top)
            all_sprites.add(bullet)
            bullets.add(bullet)

    class Enemy(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.transform.scale(meteor_img, (random.randint(20, 90), random.randint(20, 90)))
            self.image.set_colorkey((0, 0, 0))
            self.rect = self.image.get_rect()
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randint(1, 8)
            self.speedx = random.randint(-3, 3)

        def update(self):
            self.rect.y += self.speedy
            self.rect.x += self.speedx
            if self.rect.top > HEIGHT or self.rect.left < -25 or self.rect.right > WIDTH + 25:
                self.rect.x = random.randrange(WIDTH - self.rect.width)
                self.rect.y = random.randrange(-100, -40)
                self.speedy = random.randint(1, 8)

    class Bullet(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.transform.scale(lazer_img, (10, 20))
            self.image.set_colorkey((0, 0, 0))
            self.rect = self.image.get_rect()
            self.rect.bottom = y
            self.rect.centerx = x
            self.speedy = -10

        def update(self):
            self.rect.y += self.speedy
            if self.rect.bottom < 0:
                self.kill()

    all_sprites = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)

    for i in range(8):
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)

    score = 0
    font = pygame.font.Font(None, 36)

    def draw_text(surf, text, size, x, y, color=(255, 255, 255)):
        font = pygame.font.Font(None, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surface, text_rect)

    running = True
    game_over = False

    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shot()

        all_sprites.update()

        # Проверка столкновений
        hits = pygame.sprite.spritecollide(player, enemies, True)
        for hit in hits:
            player.hp -= 20
            if player.hp <= 0:
                game_over = True
                running = False

        # Проверка попадания пуль по врагам
        hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
        for hit in hits:
            score += 10
            enemy = Enemy()
            all_sprites.add(enemy)
            enemies.add(enemy)

        # Рендер
        window.blit(back, back_rect)
        all_sprites.draw(window)
        draw_text(window, f"Score: {score}", 25, WIDTH // 2, 10)
        draw_text(window, f"HP: {player.hp}", 25, WIDTH // 2, 40)
        pygame.display.flip()

    # Экран поражения
    if game_over:
        window.fill((0, 0, 0))
        draw_text(window, "Вы проиграли!", 50, WIDTH // 2, HEIGHT // 3, (255, 0, 0))
        draw_text(window, "Возврат в меню...", 30, WIDTH // 2, HEIGHT // 2, (255, 255, 255))
        pygame.display.flip()
        pygame.time.delay(3000)  # Ожидание 3 секунды

    # Возврат в главное меню
    pygame.display.set_mode((600, 600))  # Восстановление размеров окна для меню
    main_menu()




if __name__ == "__main__":
    main_menu()
