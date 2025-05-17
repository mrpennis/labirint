from pygame import *

#создай окно игры
window = display.set_mode((700, 500))
display.set_caption('догонялки')

class game_sprite(sprite.Sprite):
    def __init__(self, x, y, p_image, speed):
        super().__init__()
        self.image = transform.scale(image.load(p_image), (65, 65))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Enemy(game_sprite):
    def update (self):
        if self.rect.x <= 400:
            self.direction = 'right'
        if self.rect.x >= 630:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color, width, height, x, y):
        self.image = Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


sprite1 = game_sprite(60, 60, 'hero.png', 10)
sprite2 = Enemy(80, 80, 'cyborg.png', 20)
WALL_COLOR = (60, 130, 54)

wall_1 = Wall(WALL_COLOR, 40, 200, 60, 60)
wall_2 = Wall(WALL_COLOR, 40, 200, 80, 80) 
wall_3 = Wall(WALL_COLOR, 50, 100, 85, 100)
#задай фон сцены
background = transform.scale(image.load('background.jpg'), (700, 500))
window.blit(background, (0, 0))
is_running = True
x1 = 100
y1 = 100
y2 = 100
x2 = 200

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

    



clock = time.Clock()
fps = 45
while is_running:
    for e in event.get():
        if e.type == QUIT:
            is_running = False
    window.blit(background, (0, 0))
    sprite1.draw()
    sprite2.draw()
    sprite2.update()
    wall_1.draw_wall()
    wall_2.draw_wall()
    wall_3.draw_wall()
    keys_pressed = key.get_pressed()
    if keys_pressed[K_w]:
        sprite1.rect.y = sprite1.rect.y - 10
    if keys_pressed[K_s]:
        sprite1.rect.y =sprite1.rect.y + 10
    if keys_pressed[K_a]:
        sprite1.rect.x = sprite1.rect.x - 10
    if keys_pressed[K_d]:
        sprite1.rect.x = sprite1.rect.x + 10
    if sprite1.rect.y <= 0:
        sprite1.rect.y = sprite1.rect.y + 10
    if sprite1.rect.x <= 0:
        sprite1.rect.x = sprite1.rect.x + 10
    if sprite1.rect.x >= 630:
        sprite1.rect.x = sprite1.rect.x - 10
    if sprite1.rect.y >= 430:
        sprite1.rect.y = sprite1.rect.y - 10
    if sprite2.rect.y <= 0:
        sprite2.rect.y = sprite2.rect.y + 10
    if sprite2.rect.x <= 0:
        sprite2.rect.x = sprite2.rect.x + 10
    if sprite2.rect.x >= 630:
        sprite2.rect.x = sprite2.rect.x - 10
    if sprite2.rect.y >= 430:
        sprite2.rect.y = sprite2.rect.y - 10
    
    
    display.update()
    clock.tick(fps)

    

#обработай событие «клик по кнопке "Закрыть окно"»