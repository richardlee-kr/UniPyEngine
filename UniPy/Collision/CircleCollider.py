from .Collider import *
from .CircleBound import *

class CircleCollider(Collider):
    def __init__(self, radius = 1):
        super(CircleCollider, self).__init__()
        self.name = "CircleCollider"
        self.bounds = CircleBound(Vector.zero+self.offset, radius)
        self.radius = radius
