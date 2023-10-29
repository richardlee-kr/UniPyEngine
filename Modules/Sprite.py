import pygame

class Sprite:
    def __init__(self, source = None, PPU = 32):
        if source != None:
            self.source = source
            self.img = pygame.image.load(source)
        self.PPU = PPU