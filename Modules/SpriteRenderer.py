from Modules.Component import *
from Modules.Vector import *
from Sprite import *
import pygame

class SpriteRenderer(Component):
    def __init__(self, sprite = None):
        self.name = "SpriteRenderer"
        self.sprite = sprite

    def Render(self, screen):
        if self.sprite != None:
            screen.blit(self.sprite.img, (Vector.ToList(self.transform.position - Vector.one * self.sprite.PPU/2)))