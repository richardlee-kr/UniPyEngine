from .Bound import *

class BoxBound(Bound):
    def __init__(self, center, rect):
        super(BoxBound, self).__init__(center)
        self.box = rect