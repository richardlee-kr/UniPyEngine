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
from .Color import *

import asyncio
import pygame
WIDTH = 1080
HEIGHT = 720
FPS = 120

pygame.init()
clock = pygame.time.Clock()
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))

scene = Scene("Maverick Gunner", SCREEN)
physics = Physics(scene)
pygame.display.set_caption(scene.sceneName)