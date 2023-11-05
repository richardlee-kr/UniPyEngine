from .Bound import *
from ..Vector import *

class BoxBound(Bound):
    def __init__(self, center, size):
        super(BoxBound, self).__init__(center)
        self.size = size
        # TODO bad operand type for unary -: Vector
        #self.points = ((center+Vector(-size,-size)), center+Vector(-size,size), center+Vector(size,size), center+Vector(size,-size))