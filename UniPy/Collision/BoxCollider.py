from .Collider import *
from .BoxBound import *

class BoxCollider(Collider):
    def __init__(self, size = Vector(1,1)):
        super(BoxCollider, self).__init__()
        self.name = "BoxCollider"
        self.bounds = BoxBound(Vector.zero+self.offset, size)
        self.size = size