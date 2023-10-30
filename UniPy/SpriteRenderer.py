from .Component import *
from .Vector import *
from .Sprite import *
import pygame

class SpriteRenderer(Component):
    def __init__(self, sprite = None):
        super(SpriteRenderer, self).__init__()
        self.name = "SpriteRenderer"
        self.sprite = sprite

    def Render(self, screen):
        if self.sprite != None:
            self.sprite.img = pygame.transform.scale(self.sprite.img, Vector.ToList(self.transform.scale * self.sprite.PPU))
            screen.blit(self.sprite.img, (Vector.ToList(self.transform.position - self.transform.scale * self.sprite.PPU/2)))