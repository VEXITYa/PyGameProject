#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *
import os
import pyganim

platform_width = 32
platform_height = 32
platform_color = "#ffffff"
dir_icon = os.path.dirname(__file__)  # Полный путь к каталогу с файлами


def load_image(name, colorkey=None):
    fullname = os.path.join('data/blocks', name)
    try:
        imageb = image.load(fullname)
        imageb = imageb.convert_alpha()
        if colorkey is not None:
            if colorkey is -1:
                colorkey = imageb.get_at((0, 0))
            imageb.set_colorkey(colorkey)
        return imageb
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)


class Block(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = load_image("block.png")
        self.rect = Rect(x, y, platform_width, platform_height)


class Pesok(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = load_image("pesok.png")
        self.rect = Rect(x, y, platform_width, platform_height)


class Kirpich(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = load_image("kirpich.png")
        self.rect = Rect(x, y, platform_width, platform_height)


class Ship(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = load_image("ship.png")
        self.rect = Rect(x, y, platform_width, platform_height)


class Shipvl(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = load_image("shipvl.png")
        self.rect = Rect(x, y, platform_width, platform_height)


class Shipvp(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = load_image("shipvp.png")
        self.rect = Rect(x, y, platform_width, platform_height)


class Shipv(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = load_image("shipv.png")
        self.rect = Rect(x, y, platform_width, platform_height)


class Finish(Block):
    def __init__(self, x, y):
        Block.__init__(self, x, y)
