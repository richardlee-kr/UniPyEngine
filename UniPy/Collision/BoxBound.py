from .Bound import *

class BoxBound(Bound):
    def __init__(self, center:Vector, size:Vector):
        super(BoxBound, self).__init__(center)
        self.size = size
        self.points = (center+Vector(-size.x,-size.y), center+Vector(-size.x,size.y), center+Vector(size.x,size.y), center+Vector(size.x,-size.y))