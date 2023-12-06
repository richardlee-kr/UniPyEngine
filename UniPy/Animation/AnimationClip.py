from ..Sprite import *
from ..SpriteRenderer import *
import pygame

class AnimationClip:
    def __init__(self, clock, fps):
        self.renderer = None
        self.frames = list()
        self.currentFrame = 0
        self.clock = clock
        self.fps = fps
        self.timer = 0

    def AddBySpriteSheet(self, sheet):
        size = sheet.img.get_height()
        count = int(sheet.img.get_width() / size)
        for i in range(count):
            rect = pygame.Rect((size*i,0,size,size))
            sprite = self.SplitSheet(sheet, rect)
            self.frames.append(sprite)

    def SplitSheet(self, sheet, rect):
        size = sheet.img.get_height()
        cropped = pygame.Surface(rect.size).convert()
        cropped.blit(sheet.img, (0,0), rect)

        sprite = Sprite()
        sprite.img = cropped
        sprite.PPU = size
        return sprite

    def AddBySpriteList(self, sprites):
        for item in sprites:
            self.frames.append(item)
    
    def Play(self):
        self.timer += self.clock.get_time() / 1000
        self.renderer.sprite = self.frames[self.currentFrame]
        if self.timer >= 1/self.fps:
            self.timer = 0
            self.currentFrame = (self.currentFrame+1) % len(self.frames)