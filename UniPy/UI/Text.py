import pygame
from ..Component import *
from ..Vector import *
from ..UniColor import *

class Text(Component):
    def __init__(self, text:str = ""):
        super(Text, self).__init__()
        self.name = "Text"

        self.text = text
        self.fontName = "arial"
        self.fontSize = 30
        self.bold = False
        self.italic = False
        self.fontColor = UniColor.white

    def Update(self, screen):
        self.font = pygame.font.SysFont(self.fontName, self.fontSize, self.bold, self.italic)

        text = self.font.render(self.text, True, self.fontColor)
        text_rect = text.get_rect(center=Vector.ToList(self.transform.relativePosition))

        screen.blit(text, text_rect)