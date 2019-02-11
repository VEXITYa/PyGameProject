#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *
import os
import pyganim

platform_width = 32
platform_height = 32
platform_color = "#ffffff"
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

class Ship(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((platform_width, platform_height))
        self.image.fill(Color(platform_color))
        self.image = image.load("%s/data/blocks/ship.png" % dir_icon)
        self.image.set_colorkey(Color(platform_color))
        self.rect = Rect(x, y, platform_width, platform_height)


class Shipvl(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((platform_width, platform_height))
        self.image.fill(Color(platform_color))
        self.image = image.load("%s/data/blocks/shipvl.png" % dir_icon)
        self.image.set_colorkey(Color(platform_color))
        self.rect = Rect(x, y, platform_width, platform_height)


class Shipvp(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((platform_width, platform_height))
        self.image.fill(Color(platform_color))
        self.image = image.load("%s/data/blocks/shipvp.png" % dir_icon)
        self.image.set_colorkey(Color(platform_color))
        self.rect = Rect(x, y, platform_width, platform_height)


class Shipv(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((platform_width, platform_height))
        self.image.fill(Color(platform_color))
        self.image = image.load("%s/data/blocks/shipv.png" % dir_icon)
        self.image.set_colorkey(Color(platform_color))
        self.rect = Rect(x, y, platform_width, platform_height)


class Finish(Block):
    def __init__(self, x, y):
        Block.__init__(self, x, y)
