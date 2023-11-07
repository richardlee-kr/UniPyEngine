from .Component import *
from .GameObject import *
from .Transform import *
from .Vector import *
from .SpriteRenderer import *
from .Sprite import *
from .Animation import *
from .Collision import *
from .Scene import *
from .Camera import *
from .UniColor import *

import asyncio
import pygame
from pygame.locals import *

WIDTH = 1080
HEIGHT = 720
FPS = 30

flags = DOUBLEBUF

pygame.init()
clock = pygame.time.Clock()
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT), flags, 8)
pygame.event.set_allowed([QUIT, KEYDOWN, KEYUP])
SCREEN.set_alpha(None)

scene = Scene("Maverick Gunner", SCREEN)
physics = Physics(scene)
pygame.display.set_caption(scene.sceneName)