from .Animation import *
from .Audio import *
from .Collision import *
from .UI import *

from .Camera import *
from .Component import *
from .GameObject import *
from .Scene import *
from .Sprite import *
from .SpriteRenderer import *
from .Transform import *
from .UniColor import *
from .Vector import *

import pygame
from pygame.locals import *

WIDTH = 400
HEIGHT = 500
FPS = 30

flags = DOUBLEBUF

pygame.init()
clock = pygame.time.Clock()
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT), flags, 8)
pygame.event.set_allowed([QUIT, KEYDOWN, KEYUP])
SCREEN.set_alpha(None)

scene = Scene("Test", SCREEN)
physics = Physics(scene)
pygame.display.set_caption(scene.sceneName)