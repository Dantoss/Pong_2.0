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
    def update_left(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0: self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 375: self.rect.y += self.speed
    def update_right(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0: self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 375: self.rect.y += self.speed



mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()

clock = time.Clock()
FPS = 60

num_fire = 0
rel_time = False

window = display.set_mode((700, 500))
display.set_caption("Пинг понг")
background = transform.scale(image.load("galaxy.jpg"), (700, 500))
player = Player('racket.jpeg',0, 200, 50, 120, 15)
player2 = Player('racket.jpeg',650, 200, 50, 120, 15)
ball = GameSprite('ball.jpeg',350, 100, 50, 50, 15)

speed_x = 3
speed_y = -3

font.init()
font1 = font.SysFont('Arial', 36)

won1_text = font1.render(f'Выиграл первый', 1, (255,255,255))
won2_text = font1.render(f'Выиграл второй', 1, (255,255,255))

win_height = 500

game = True
finish = False           
while game:
    for e in event.get():
        if e.type == QUIT: game = False
    if finish != True:
        window.blit(background, (0, 0))
        player.reset()
        player.update_left()
        player2.reset()
        player2.update_right()
        ball.reset()
        ball.update()
        clock.tick(FPS)
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.x >= 650:
            window.blit(won1_text,(300,300))
            game = False
        if ball.rect.x <= 0:
            window.blit(won2_text,(300,300))
            game = False
        if ball.rect.y > win_height or ball.rect.y < 0:
            speed_y *= -1

        if sprite.collide_rect(player , ball) or sprite.collide_rect(player2 , ball): 
            speed_x *= -1
        # lost_text = font1.render(f'Пропущено: {lost}', 1, (255,255,255))
        # kill_text = font1.render(f'Убито: {killed}', 1, (255,255,255))
        # reload_text = font1.render('ПЕРЕЗАРЯДКА', 1, (255,255,255))
        # window.blit(lost_text,(0,0))
        # window.blit(kill_text,(0,30))
        

    display.update()
