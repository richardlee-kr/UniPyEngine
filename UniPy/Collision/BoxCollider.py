from .Collider import *
from .BoxBound import *
from ..UniColor import *
import pygame

class BoxCollider(Collider):
    def __init__(self, size = Vector(1,1)):
        super(BoxCollider, self).__init__()
        self.name = "BoxCollider"
        self.bounds = BoxBound(Vector.zero+self.offset, size)
        self.size = size

    def Update(self, screen):
        if self.isVisible:
            self.Draw(screen)

    def Draw(self, screen):
        pygame.draw.rect(screen, Color.green, [self.transform.position.x-self.size.x/2, self.transform.position.y-self.size.y/2, self.size.x, self.size.y], 1)