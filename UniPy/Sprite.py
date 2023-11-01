import pygame

class Sprite:
    def __init__(self, source = None):
        if source != None:
            self.source = source
            self.img = pygame.image.load(source)
            self.PPU = self.img.get_height()