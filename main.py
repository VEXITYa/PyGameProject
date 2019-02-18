import pygame
from pygame import *
from player import *
from blocks import *


win_width = 1000
win_height = 700
display = (win_width, win_height)
background_color = "#57574d"

dir_files = os.path.dirname(__file__)


class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)


def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l+win_width / 2, -t+win_height / 2

    l = min(0, l)
    l = max(-(camera.width-win_width), l)
    t = max(-(camera.height-win_height), t)
    t = min(0, t)

    return Rect(l, t, w, h) 


def loadlevel(namefile):
    global playerX, playerY

    levelfile = open(('%s/data/levels/' + namefile) % dir_files)
    line = " "
    while line[0] != "/":
        line = levelfile.readline()
        if line[0] == "[":
            while line[0] != "]":
                line = levelfile.readline()
                if line[0] != "]":
                    endline = line.find("|")
                    level.append(line[0: endline])
                    
        if line[0] != "":
            commands = line.split()
            if len(commands) > 1:
                if commands[0] == "player":
                    playerX = int(commands[1])
                    playerY = int(commands[2])


def main():
    loadlevel('level2.txt')
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode(display)
    pygame.display.set_caption("8-bit game")
    bg = Surface((win_width, win_height))
    bg.fill(Color(background_color))
        
    left = right = False  # по умолчанию - стоим
    up = False
    running = False
    hero = Player(playerX, playerY)
    entities.add(hero)
           
    timer = pygame.time.Clock()
    x = y = 0
    for row in level:
        for col in row:
            if col == "B":
                pf = Block(x, y)
                entities.add(pf)
                platforms.append(pf)
            if col == "s":
                bd = Ship(x, y)
                entities.add(bd)
                platforms.append(bd)
            if col == "K":
                pf = Kirpich(x, y)
                entities.add(pf)
                platforms.append(pf)
            if col == "-":
                bd = Pesok(x, y)
                entities.add(bd)
                platforms.append(bd)
            if col == "v":
                bd = Shipv(x, y)
                entities.add(bd)
                platforms.append(bd)
            if col == ">":
                bd = Shipvp(x, y)
                entities.add(bd)
                platforms.append(bd)
            if col == "<":
                bd = Shipvl(x, y)
                entities.add(bd)
                platforms.append(bd)
   
            x += platform_width
        y += platform_height
        x = 0
    
    total_level_width = len(level[0]) * platform_width
    total_level_height = len(level) * platform_height
    pygame.mixer.music.load("data/music/Music.mp3")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)
    camera = Camera(camera_configure, total_level_width, total_level_height)

    while not hero.winner:
        for e in pygame.event.get():
            if e.type == QUIT:
                raise SystemExit
            if e.type == KEYDOWN and e.key == K_UP:
                up = True
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True
            if e.type == KEYDOWN and e.key == K_LSHIFT:
                running = True
            if e.type == KEYDOWN and e.key == K_SPACE:
                up = True
            if e.type == KEYDOWN and e.key == K_w:
                up = True
            if e.type == KEYDOWN and e.key == K_a:
                left = True
            if e.type == KEYDOWN and e.key == K_d:
                right = True
            if e.type == KEYDOWN and e.key == K_SPACE:
                up = True

            if e.type == KEYUP and e.key == K_UP:
                up = False
            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False
            if e.type == KEYUP and e.key == K_LSHIFT:
                running = False
            if e.type == KEYUP and e.key == K_SPACE:
                up = False
            if e.type == KEYUP and e.key == K_w:
                up = False
            if e.type == KEYUP and e.key == K_a:
                left = False
            if e.type == KEYUP and e.key == K_d:
                right = False
            if e.type == KEYUP and e.key == K_SPACE:
                up = False

        screen.blit(bg, (0, 0))
        animatedEntities.update()
        camera.update(hero)
        hero.update(left, right, up, running, platforms)
        for e in entities:
            screen.blit(e.image, camera.apply(e))
        pygame.display.update()
        timer.tick(60)


level = []
entities = pygame.sprite.Group()  # Все объекты
animatedEntities = pygame.sprite.Group()
platforms = []
if __name__ == "__main__":
    main()
