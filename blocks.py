#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *
import os
import pyganim

platform_width = 32
platform_height = 32
platform_color = "#000000"
dir_icon = os.path.dirname(__file__)  # Полный путь к каталогу с файлами
            
 
class Block(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((platform_width, platform_height))
        self.image.fill(Color(platform_color))
        self.image = image.load("%s/data/blocks/block.png" % dir_icon)
        self.image.set_colorkey(Color(platform_color))
        self.rect = Rect(x, y, platform_width, platform_height)


class Pesok(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((platform_width, platform_height))
        self.image.fill(Color(platform_color))
        self.image = image.load("%s/data/blocks/pesok.png" % dir_icon)
        self.image.set_colorkey(Color(platform_color))
        self.rect = Rect(x, y, platform_width, platform_height)


class Kirpich(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((platform_width, platform_height))
        self.image.fill(Color(platform_color))
        self.image = image.load("%s/data/blocks/kirpich.png" % dir_icon)
        self.image.set_colorkey(Color(platform_color))
        self.rect = Rect(x, y, platform_width, platform_height)


class Plosko(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((platform_width, platform_height))
        self.image.fill(Color(platform_color))
        self.image = image.load("%s/data/blocks/plosko.png" % dir_icon)
        self.image.set_colorkey(Color(platform_color))
        self.rect = Rect(x, y, platform_width, platform_height)


class Ploskoship(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((platform_width, platform_height))
        self.image.fill(Color(platform_color))
        self.image = image.load("%s/data/blocks/plosko_ship.png" % dir_icon)
        self.image.set_colorkey(Color(platform_color))
        self.rect = Rect(x, y, platform_width, platform_height)


class Ship(Block):
    def __init__(self, x, y):
        Block.__init__(self, x, y)
        self.image = image.load("%s/data/blocks/ship.png" % dir_icon)


class Shipverx(Block):
    def __init__(self, x, y):
        Block.__init__(self, x, y)
        self.image = image.load("%s/data/blocks/shipv.png" % dir_icon)


class Finish(Block):
    def __init__(self, x, y):
        Block.__init__(self, x, y)
