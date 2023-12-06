from .Collider import *
from .CircleBound import *
from ..UniColor import *
import pygame

class CircleCollider(Collider):
    def __init__(self, radius = 1):
        super(CircleCollider, self).__init__()
        self.name = "CircleCollider"
        self.bounds = CircleBound(Vector.zero+self.offset, radius)
        self.radius = radius

    def Update(self, screen:pygame.Surface):
        if self.isVisible:
            self.Draw(screen)

    def Draw(self, screen:pygame.Surface):
        pygame.draw.circle(screen, UniColor.green, [self.transform.position.x, self.transform.position.y], self.radius, 1)