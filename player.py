#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *
import pyganim
import os
import blocks

move_speed = 4
extra_move_speed = 2.5  # ускорение
width = 16
height = 16
color = "#888888"
jump_power = 9
extra_jump = 1  # дополнительная сила прыжка
gravity = 0.35  # Сила, которая будет тянуть нас вниз
anim_delay = 0.1  # скорость смены кадров
extra_anim_delay = 0.05  # скорость смены кадров при ускорении
dir_icon = os.path.dirname(__file__)  # Полный путь к каталогу с файлами

anim_r = [('%s/data/Hero/r1.png' % dir_icon),
                   ('%s/data/Hero/r2.png' % dir_icon),
                   ('%s/data/Hero/r3.png' % dir_icon),
                   ('%s/data/Hero/r4.png' % dir_icon),
                   ('%s/data/Hero/r5.png' % dir_icon)]
anim_l = [('%s/data/Hero/l1.png' % dir_icon),
                  ('%s/data/Hero/l2.png' % dir_icon),
                  ('%s/data/Hero/l3.png' % dir_icon),
                  ('%s/data/Hero/l4.png' % dir_icon),
                  ('%s/data/Hero/l5.png' % dir_icon)]
anim_jumpl = [('%s/data/Hero/jl.png' % dir_icon, 0.1)]
anim_jumpr = [('%s/data/Hero/jr.png' % dir_icon, 0.1)]
anim_jump = [('%s/data/Hero/jr.png' % dir_icon, 0.1)]
anim_stay = [('%s/data/Hero/r1.png' % dir_icon, 0.1)]


class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х
        self.startY = y
        self.yvel = 0  # скорость вертикального перемещения
        self.onGround = False  # На земле ли я
        self.image = Surface((width, height))
        self.image.fill(Color(color))
        self.rect = Rect(x, y, width, height)
        self.image.set_colorkey(Color(color))

        boltAnim = []
        boltAnimSuperSpeed = []
        for anim in anim_r:
            boltAnim.append((anim, anim_delay))
            boltAnimSuperSpeed.append((anim, extra_anim_delay))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()
        self.boltAnimRightSuperSpeed = pyganim.PygAnimation(boltAnimSuperSpeed)
        self.boltAnimRightSuperSpeed.play()

        boltAnim = []
        boltAnimSuperSpeed = [] 
        for anim in anim_l:
            boltAnim.append((anim, anim_delay))
            boltAnimSuperSpeed.append((anim, extra_anim_delay))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()
        self.boltAnimLeftSuperSpeed = pyganim.PygAnimation(boltAnimSuperSpeed)
        self.boltAnimLeftSuperSpeed.play()
        
        self.boltAnimStay = pyganim.PygAnimation(anim_stay)
        self.boltAnimStay.play()
        self.boltAnimStay.blit(self.image, (0, 0))
        
        self.boltAnimJumpLeft = pyganim.PygAnimation(anim_jumpl)
        self.boltAnimJumpLeft.play()
        
        self.boltAnimJumpRight = pyganim.PygAnimation(anim_jumpr)
        self.boltAnimJumpRight.play()
        
        self.boltAnimJump = pyganim.PygAnimation(anim_jump)
        self.boltAnimJump.play()
        self.winner = False

    def update(self, left, right, up, running, platforms):
        
        if up:
            if self.onGround:
                self.yvel = -jump_power
                if running and (left or right):
                    self.yvel -= extra_jump
                self.image.fill(Color(color))
                self.boltAnimJump.blit(self.image, (0, 0))
                       
        if left:
            self.xvel = -move_speed
            self.image.fill(Color(color))
            if running:
                self.xvel -= extra_move_speed
                if not up:
                    self.boltAnimLeftSuperSpeed.blit(self.image, (0, 0))
            else:
                if not up:
                    self.boltAnimLeft.blit(self.image, (0, 0))
            if up:
                    self.boltAnimJumpLeft.blit(self.image, (0, 0))
 
        if right:
            self.xvel = move_speed  # Право = x + n
            self.image.fill(Color(color))
            if running:
                self.xvel += extra_move_speed
                if not up:
                    self.boltAnimRightSuperSpeed.blit(self.image, (0, 0))
            else:
                if not up:
                    self.boltAnimRight.blit(self.image, (0, 0)) 
            if up:
                    self.boltAnimJumpRight.blit(self.image, (0, 0))

        if not(left or right):  # стоим, когда нет указаний идти
            self.xvel = 0
            if not up:
                self.image.fill(Color(color))
                self.boltAnimStay.blit(self.image, (0, 0))
            
        if not self.onGround:
            self.yvel += gravity
            
        self.onGround = False
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        self.rect.x += self.xvel  # переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms)
   
    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if sprite.collide_mask(self, p):  # если есть пересечение платформы с игроком
                if isinstance(p, blocks.Ship) or isinstance(p, blocks.Shipv) \
                        or isinstance(p, blocks.Shipvp) or isinstance(p, blocks.Shipvl):
                    self.die()  # умираем
                else:
                    if xvel > 0:
                        self.rect.right = p.rect.left

                    if xvel < 0:
                        self.rect.left = p.rect.right

                    if yvel > 0:
                        self.rect.bottom = p.rect.top
                        self.onGround = True
                        self.yvel = 0                  # энергия падения пропадает

                    if yvel < 0:
                        self.rect.top = p.rect.bottom
                        self.yvel = 0                  # энергия прыжка пропадает

    def teleporting(self, goX, goY):
        self.rect.x = goX
        self.rect.y = goY
        
    def die(self):
        time.wait(1000)
        self.teleporting(self.startX, self.startY)  # перемещаемся в начальные координаты
