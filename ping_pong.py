from pygame import *
from random import randint, uniform
from time import time as timer
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, w, h, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w, h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.killed = 0
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0: self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 375: self.rect.y += self.speed



mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()

clock = time.Clock()
FPS = 60

num_fire = 0
rel_time = False

window = display.set_mode((700, 500))
display.set_caption("Шутер")
background = transform.scale(image.load("galaxy.jpg"), (700, 500))
player = Player('racket.jpeg',0, 200, 50, 120, 15)

font.init()
font1 = font.SysFont('Arial', 36)

game = True
finish = False           
while game:
    for e in event.get():
        if e.type == QUIT: game = False
    if finish != True:
        window.blit(background, (0, 0))
        player.reset()
        player.update()
        clock.tick(FPS)
        
        # lost_text = font1.render(f'Пропущено: {lost}', 1, (255,255,255))
        # kill_text = font1.render(f'Убито: {killed}', 1, (255,255,255))
        # reload_text = font1.render('ПЕРЕЗАРЯДКА', 1, (255,255,255))
        # window.blit(lost_text,(0,0))
        # window.blit(kill_text,(0,30))
        

    display.update()