import pygame

class Sprite:
    def __init__(self, source, PPU = 32):
        self.source = source
        self.img = pygame.image.load(source)
        self.PPU = PPU