from ..GameObject import *
from .RectTransform import *

class UI(GameObject):
    def __init__(self, name:str):
        self.name = name
        self.layer = "UI"
        self.tag = "Untagged"
        self.transform = RectTransform()
        self.components = list()
        self.AddComponent(self.transform)

    def Update(self):
        self.transform.Update()