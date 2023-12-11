from ..Vector import *
from ..Transform import *

class RectTransform(Transform):
    def __init__(self):
        super(RectTransform, self).__init__()
        self.name = "RectTransform"

        self.width = 100
        self.height = 100