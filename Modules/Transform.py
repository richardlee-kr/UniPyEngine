from Modules.Component import *
from Modules.Vector import *

class Transform(Component):
    def __init__(self):
        self.position = Vector.zero
        self.rotation = 0
        self.parent = None
        self.child = list()