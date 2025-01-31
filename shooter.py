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


        hits = pygame.sprite.spritecollide(player, enemies, True)
        for hit in hits:
            player.hp -= 20
            if player.hp <= 0:
                game_over = True
                running = False


        hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
        for hit in hits:
            score += 10
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
        draw_text(window, "Вы проиграли!", 50, WIDTH // 2, HEIGHT // 3, (255, 0, 0))
        draw_text(window, "Возврат в меню...", 30, WIDTH // 2, HEIGHT // 2, (255, 255, 255))
        pygame.display.flip()
        pygame.time.delay(3000)  

    pygame.display.set_mode((600, 600)) 
    main_menu()
