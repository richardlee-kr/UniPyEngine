from .Bound import *

class CircleBound(Bound):
    def __init__(self, center:Vector, radius:float):
        super(CircleBound, self).__init__(center)
        self.radius = radius