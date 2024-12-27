import pygame
import random

pygame.init()

WIDTH = 600
HEIGHT = 400
SPEED = 5
window = pygame.display.set_mode((WIDTH, HEIGHT))
back = pygame.image.load('starfield.png').convert()
back_rect = back.get_rect()
player_img = pygame.image.load('rocket.png').convert()
meteor_img = pygame.image.load('meteor.png').convert()
lazer_img = pygame.image.load('laser.png').convert()
clock = pygame.time.Clock()
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface((50, 50))
        self.image = player_img
        self.image = pygame.transform.scale(player_img, (50, 60))
        self.image.set_colorkey((0, 0, 0))
        self.radius = 27
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
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
        if self.rect.right > WIDTH - 5:
            self.rect.right = WIDTH - 5
        if self.rect.left < 5:
            self.rect.left = 5

    def shot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        wh = random.randrange(20, 90)
        self.image = meteor_img
        self.image = pygame.transform.scale(meteor_img, (wh, wh))
        self.image.set_colorkey((0, 0, 0))
        self.radius = wh/2
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(WIDTH - self.rect.width)
        self.rect.bottom = random.randrange(-120, -60)
        self.speedy = random.randrange(1, 6)
        self.speedx = random.randrange(-2, 3)

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-120, -60)
            self.speedy = random.randrange(1, 6)
            self.speedx = random.randrange(-2, 3)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = lazer_img
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
for i in range(7):
    m = Enemy()
    all_sprites.add(m)
    enemies.add(m)

score = 0
font_name = pygame.font.match_font('comis sans')
def draw_text(win, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    win.blit(text_surface, text_rect)
    
game_over = False


while not game_over:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shot()
    all_sprites.update()

    hits = pygame.sprite.spritecollide(player, enemies, True, pygame.sprite.collide_circle)

    for hit in hits:
        player.hp -= hit.radius
        if player.hp <= 0:
            game_over = True
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)
        
    hits2 = pygame.sprite.groupcollide(enemies, bullets, True, True)
    for hit in hits2:
        score += 1
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)
    window.fill((0,0,0))
    window.blit(back, back_rect)
    all_sprites.draw(window)
    draw_text(window, str(score), 25, WIDTH/2, 20)
    draw_text(window, str(player.hp), 20, WIDTH/2, 40)
    pygame.display.update()


pygame.quit()
        
