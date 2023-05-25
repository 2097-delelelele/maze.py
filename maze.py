from pygame import*
mixer.init()
font.init()
window = display.set_mode((700,500))
display.set_caption('Лабиринт')

class  GameSprite():
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player (GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= speed
        if keys_pressed[K_RIGHT] and self.rect.x < 625:
            self.rect.x += speed
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= speed
        if keys_pressed[K_DOWN] and self.rect.y < 400:
            self.rect.y += speed
class Enemy  (GameSprite):
    direction = 'left'
    def update(self):
        if self.direction == 'left' :
            self.rect.x -= speed
        if self.direction == 'right' :
            self.rect.x += speed
        if self.rect.x <= 530:
            self.direction = 'right'
        if self.rect.x >= 625:
            self.direction ='left'
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3,  wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self. rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

background = transform.scale(image.load('background.jpg'), (700, 500))
cyborg = Enemy('cyborg.png',630, 200,  5)
hero = Player('hero.png',480, 70, 5)
treasure = GameSprite('treasure.png',630, 10, 5)
w1 = Wall(154, 205, 50, 100, 20, 450, 10)
w2 = Wall(154, 205, 50, 100, 480, 350, 10)
w3 = Wall(154, 205, 50, 100, 20, 10, 380)
mixer.music.load('jungles.ogg')
mixer.music.play()
font = font.SysFont("Arial",70)
winer = font.render('YOU WIN',True,(255,0,0))
win = mixer.Sound('money.ogg')
lose = font.render('YOU LOSE!',True,(255,0,0))
were = mixer.Sound('kick.ogg')
clock = time.Clock()
FPS = 60
speed = 2
game = True
fin = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if fin != True:
       
        window.blit(background, (0, 0))
        cyborg.reset()
        hero.reset()
        treasure.reset()
        hero.update()
        cyborg.update()
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        if sprite.collide_rect(hero,cyborg) or sprite.collide_rect(hero, w1) or  sprite.collide_rect(hero, w2) or sprite.collide_rect(hero, w3):
            fin = True
            window.blit(lose, (200, 200))
            were.play()
        if sprite.collide_rect(hero, treasure):
            window.blit(winer, (200, 200))
            fin = True
            money.play()
    display.update()
    clock.tick(FPS)


        
