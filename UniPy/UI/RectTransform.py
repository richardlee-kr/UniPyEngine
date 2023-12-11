from ..Vector import *
from ..Transform import *

class RectTransform(Transform):
    def __init__(self):
        super(RectTransform, self).__init__()
        self.name = "RectTransform"

        self.width = 2
        self.height = 1

    def Update(self, screen):
        super(RectTransform, self).Update(screen)
        self.transform.scale = Vector(self.width,self.height)