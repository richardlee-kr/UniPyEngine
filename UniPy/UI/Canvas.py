import pygame
from ..Component import *
from .UI import *

class Canvas(Component):
    def __init__(self, screen:pygame.Surface):
        super(Canvas, self).__init__()
        self.name = "Canvas"

        self.screenWidth = screen.get_width()
        self.screenHeight = screen.get_height()