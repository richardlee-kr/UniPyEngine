from .Component import *
from .Vector import *
from math import *

class Transform(Component):
    def __init__(self):
        self.name = "Transform"
        self.position = Vector.zero
        self.rotation = 0
        self.scale = Vector.one
        self.parent = None
        self.child = list()
        self.childCount = len(self.child)
        self.right = Vector.right
        self.up = Vector.up

    def Translate(self, v):
        self.position += v

    def Rotate(self, angle):
        self.rotation += angle % 360
        self.right = Vector(math.cos(math.radians(angle)),math.sin(math.radians(angle)))
        self.up = Vector(-1 * math.sin(math.radians(angle)), math.cos(math.radians(angle)))