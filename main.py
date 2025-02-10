import pygame
import sys
import sqlite3
import random
import time
from pymorphy2 import MorphAnalyzer

from button import ImageButton

pygame.init()

connection = sqlite3.connect('dop')
cursor = connection.cursor()
sq = cursor.execute('select snake from quest').fetchall()
sq = sq[0][0]

connection = sqlite3.connect('dop')
cursor = connection.cursor()
shq = cursor.execute('select shooter from quest').fetchall()
shq = shq[0][0]

connection = sqlite3.connect('dop')
cursor = connection.cursor()
wq = cursor.execute('select wordle from quest').fetchall()
wq = wq[0][0]

WIDTH, HEIGHT = 600, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu")
main_background = pygame.image.load("background.jpg")
main_background = pygame.transform.scale(main_background, (WIDTH, HEIGHT))



rocket_button = ImageButton(WIDTH / 2 - (297 / 4), 300, 297 / 2, 128 / 2, 'Метеориты', 'button1.png', 'button12.png')
snake_button = ImageButton(WIDTH / 2 - (297 / 4), 200, 297 / 2, 128 / 2, 'Змейка', 'button1.png', 'button12.png')
exit_button = ImageButton(WIDTH / 2 - (297 / 4), 500, 297 / 2, 128 / 2, 'Выход', 'button1.png', 'button12.png')
wordle_button = ImageButton(WIDTH / 2 - (297 / 4), 400, 297 / 2, 128 / 2, 'Вордли', 'button1.png', 'button12.png')
quest_button = ImageButton(150, 300, 60, 80,'', 'button1.png', 'button12.png')

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
            quest_button.check_hover(pygame.mouse.get_pos())

        if event.type == pygame.USEREVENT and event.button == snake_button:
            snake_game()

        if event.type == pygame.USEREVENT and event.button == rocket_button:
            rocket_game()

        if event.type == pygame.USEREVENT and event.button == wordle_button:
            wordle_game()

        if event.type == pygame.USEREVENT and event.button == quest_button:
            quest()

        if event.type == pygame.USEREVENT and event.button == exit_button:
            pygame.display.flip()
            pygame.quit()



        wordle_button.handle_event(event)
        wordle_button.draw(screen)

        quest_button.handle_event(event)
        quest_button.draw(screen)


        rocket_button.handle_event(event)
        rocket_button.draw(screen)


        exit_button.handle_event(event)
        exit_button.draw(screen)


        snake_button.handle_event(event)
        snake_button.draw(screen)
        pygame.display.flip()


def quest():
    pygame.init()
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(main_background, (0, 0))

        font = pygame.font.Font(None, 72)
        text_surface = font.render("ЗАДАНИЯ", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH / 2, 100))
        screen.blit(text_surface, text_rect)

        font = pygame.font.Font(None, 52)
        s = str(sq)
        text_surface = font.render("Яблоки: " + s + '/100', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH / 2, 200))
        screen.blit(text_surface, text_rect)

        font = pygame.font.Font(None, 52)
        sh = str(shq)
        text_surface = font.render("Очков за метеориты: " + sh + "/1000", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH / 2, 300))
        screen.blit(text_surface, text_rect)

        font = pygame.font.Font(None, 52)
        w = str(wq)
        text_surface = font.render("Очки за слова: " + w + '/1000', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH / 2, 400))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: 
                    running = False

        pygame.display.flip()

def snake_game():

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
        time.sleep(1.5)

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
                global sq
                if sq < 100:
                    sq += 1
                    a = cursor.execute('UPDATE quest SET snake = snake + 1')
                    connection.commit()



            draw_grid()
            pygame.draw.rect(window, red, [foodx, foody, block, block], 0)
            draw_snake(snake_list)

            message(f"Счёт: {score}", white, width // 10, 20, font_small)

            pygame.display.update()
            clock.tick(10) #cкорость змейки

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
    back = pygame.image.load('starfield.png').convert()
    back_rect = back.get_rect()
    player_img = pygame.image.load('rocket.png').convert()
    meteor_img = pygame.image.load('meteor.png').convert()
    lazer_img = pygame.image.load('laser.png').convert()
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

    for i in range(12): #количество метеоритов
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


        hits = pygame.sprite.spritecollide(player, enemies, True)
        for hit in hits:
            player.hp -= 20
            if player.hp <= 0:
                game_over = True
                running = False


        hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
        for hit in hits:
            score += 10
            global shq
            if shq < 1000:
                shq += 10
                a = cursor.execute('UPDATE quest SET shooter = shooter + 10')
                connection.commit()
            enemy = Enemy()
            all_sprites.add(enemy)
            enemies.add(enemy)


        window.blit(back, back_rect)
        all_sprites.draw(window)
        draw_text(window, f"Score: {score}", 25, WIDTH // 2, 10)
        draw_text(window, f"HP: {player.hp}", 25, WIDTH // 2, 40)
        pygame.display.flip()


    if game_over:
        window.fill((0, 0, 0))
        draw_text(window, "Вы проиграли!", 50, WIDTH // 2, 100, (255, 0, 0))
        draw_text(window, f"Score: {score}", 35, WIDTH // 2, 175, (255, 215, 0))
        draw_text(window, "Возврат в меню...", 35, WIDTH // 2, 250, (255, 255, 255))
        pygame.display.flip()
        pygame.time.delay(1500)


    pygame.display.set_mode((600, 600))
    main_menu()


def wordle_game():
    pygame.init()

    WIDTH, HEIGHT = 800, 900
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GRAY = (200, 200, 200)
    GREEN = (106, 170, 100)
    YELLOW = (201, 180, 88)
    DARK_GRAY = (120, 124, 126)
    LIGHT_BLUE = (52, 152, 219)
    ROWS = 6
    COLS = 5
    LETTER_SIZE = 70
    SPACING = 10
    FONT_SIZE = 40
    KEYBOARD_HEIGHT = 200

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Wordle")

    try:
        font = pygame.font.Font("arial.ttf", FONT_SIZE)
        score_font = pygame.font.Font("arial.ttf", 30)
        info_font = pygame.font.SysFont("Arial", 20)
    except:
        font = pygame.font.SysFont("Arial", FONT_SIZE)
        score_font = pygame.font.SysFont("Arial", 30)
        info_font = pygame.font.SysFont("Arial", 20)

    try:
        with open("russian.txt", "r", encoding="windows-1251") as file:
            all_words = [word.strip().upper() for word in file if len(word.strip()) == 5]
    except UnicodeDecodeError:
        print("Ошибка: Неверная кодировка файла. Убедитесь, что файл сохранен в кодировке Windows-1251.")
        exit()

    morph = MorphAnalyzer()

    def is_noun_in_nominative(word):
        parsed = morph.parse(word.lower())[0]
        return 'NOUN' in parsed.tag and 'nomn' in parsed.tag

    russian_words = [word for word in all_words if is_noun_in_nominative(word)]

    current_guess = []
    guesses = [[] for _ in range(ROWS)]
    current_row = 0
    score = 0
    game_over = False
    correct_word = random.choice(russian_words).upper()
    russian_letters = "ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ"
    keyboard_status = {letter: GRAY for letter in russian_letters}

    def draw_grid():
        for row in range(ROWS):
            for col in range(COLS):
                x = col * (LETTER_SIZE + SPACING) + (WIDTH - COLS * (LETTER_SIZE + SPACING)) // 2
                y = row * (LETTER_SIZE + SPACING) + 100
                rect = pygame.Rect(x, y, LETTER_SIZE, LETTER_SIZE)
                color = GRAY
                if len(guesses[row]) > col:
                    color = guesses[row][col][1]
                pygame.draw.rect(screen, color, rect, border_radius=10)
                pygame.draw.rect(screen, BLACK, rect, 3, border_radius=10)

    def draw_letters():
        for row in range(ROWS):
            for col in range(len(guesses[row])):
                letter, color = guesses[row][col]
                x = col * (LETTER_SIZE + SPACING) + (WIDTH - COLS * (LETTER_SIZE + SPACING)) // 2 + LETTER_SIZE // 2
                y = row * (LETTER_SIZE + SPACING) + 100 + LETTER_SIZE // 2
                text = font.render(letter, True, WHITE)
                screen.blit(text, text.get_rect(center=(x, y)))

    def check_guess():
        nonlocal current_row, game_over, score
        guess = ''.join(current_guess).upper()
        if guess.lower() not in [word.lower() for word in russian_words]:
            return False
        temp_correct = list(correct_word)
        guess_result = []
        for i, letter in enumerate(guess):
            if letter == correct_word[i]:
                guess_result.append((letter, GREEN))
                keyboard_status[letter] = GREEN
                temp_correct[i] = None
                score += 10
            else:
                guess_result.append((letter, DARK_GRAY))
        for i, (letter, color) in enumerate(guess_result):
            if color == DARK_GRAY and letter in temp_correct:
                guess_result[i] = (letter, YELLOW)
                if keyboard_status[letter] != GREEN:
                    keyboard_status[letter] = YELLOW
                temp_correct.remove(letter)
                score += 5
            elif color == DARK_GRAY:
                keyboard_status[letter] = DARK_GRAY
        guesses[current_row] = guess_result
        current_row += 1
        if guess == correct_word:
            game_over = True
            score += 200
        elif current_row >= ROWS:
            game_over = True
        return True

    def draw_score():
        score_text = score_font.render(f"Очки: {score}", True, LIGHT_BLUE)
        screen.blit(score_text, (10, 10))

    def new_game():
        nonlocal current_guess, guesses, current_row, correct_word, game_over, score, keyboard_status
        current_guess = []
        guesses = [[] for _ in range(ROWS)]
        current_row = 0
        correct_word = random.choice(russian_words).upper()
        game_over = False
        score = 0
        keyboard_status = {letter: GRAY for letter in russian_letters}

    def draw_game_over():
        global wq  
        screen.fill(BLACK)
        result_text = "ПОБЕДА!" if any(
            ''.join([g[0] for g in guess]) == correct_word for guess in guesses) else "ПОРАЖЕНИЕ!"
        text_surface = font.render(result_text, True, RED)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
        screen.blit(text_surface, text_rect)
        word_surface = font.render(f"Загаданное слово: {correct_word}", True, YELLOW)
        word_rect = word_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20))
        screen.blit(word_surface, word_rect)
        score_surface = font.render(f"Счет: {score}", True, GREEN)
        score_rect = score_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 90))
        screen.blit(score_surface, score_rect)
        timer_surface = font.render("Возврат в меню...", True, WHITE)
        timer_rect = timer_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 150))
        screen.blit(timer_surface, timer_rect)


        if wq < 1000:
            connection = sqlite3.connect('dop')
            cursor = connection.cursor()
            new_score = min(wq + score, 1000)
            cursor.execute('UPDATE quest SET wordle = ?', (new_score,))
            connection.commit()
            connection.close()
            wq = new_score

        pygame.display.flip()
        pygame.time.wait(3000)
        pygame.display.set_mode((600, 600))
        main_menu()

    def draw_keyboard():
        keyboard_layout = [
            "ЙЦУКЕНГШЩЗХЪ",
            "ФЫВАПРОЛДЖЭ",
            "ЯЧСМИТЬБЮ"
        ]
        key_width = 40
        key_height = 50
        start_x = (WIDTH - (key_width * 12 + SPACING * 11)) // 2
        start_y = HEIGHT - KEYBOARD_HEIGHT + 20
        for row_index, row in enumerate(keyboard_layout):
            for col_index, letter in enumerate(row):
                x = start_x + col_index * (key_width + SPACING)
                y = start_y + row_index * (key_height + SPACING)
                rect = pygame.Rect(x, y, key_width, key_height)
                shadow_rect = pygame.Rect(x + 3, y + 3, key_width, key_height)
                pygame.draw.rect(screen, BLACK, shadow_rect, border_radius=8)
                pygame.draw.rect(screen, keyboard_status[letter], rect, border_radius=8)
                pygame.draw.rect(screen, BLACK, rect, 2, border_radius=8)
                text = info_font.render(letter, True, WHITE)
                screen.blit(text, text.get_rect(center=(x + key_width // 2, y + key_height // 2)))

    running = True
    while running:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if game_over:
                    if event.key == pygame.K_SPACE:
                        new_game()
                else:
                    if event.key == pygame.K_BACKSPACE and len(current_guess) > 0:
                        current_guess.pop()
                    elif event.key == pygame.K_RETURN and len(current_guess) == COLS:
                        if check_guess():
                            current_guess = []
                    else:
                        char = event.unicode.upper()
                        if char in russian_letters and len(current_guess) < COLS:
                            current_guess.append(char)

        draw_grid()
        draw_letters()
        draw_score()
        draw_keyboard()


        if not game_over:
            for i, letter in enumerate(current_guess):
                x = i * (LETTER_SIZE + SPACING) + (WIDTH - COLS * (LETTER_SIZE + SPACING)) // 2 + LETTER_SIZE // 2
                y = current_row * (LETTER_SIZE + SPACING) + 100 + LETTER_SIZE // 2
                text = font.render(letter, True, WHITE)
                screen.blit(text, text.get_rect(center=(x, y)))

        if game_over:
            draw_game_over()

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main_menu()
