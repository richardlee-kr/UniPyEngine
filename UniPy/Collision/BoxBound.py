from .Bound import *

class BoxBound(Bound):
    def __init__(self, center, size):
        super(BoxBound, self).__init__(center)
        self.size = size