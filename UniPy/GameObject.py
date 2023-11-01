from .Transform import *

class GameObject:
    def __init__(self, name):
        self.name = name
        self.layer = "Default"
        self.tag = "Untagged"
        self.transform = Transform()
        self.components = list()
        self.AddComponent(self.transform)
    
    def AddComponent(self, cmpnt):
        self.components.append(cmpnt)
        cmpnt.gameObject = self
        cmpnt.transform = self.transform

    def GetComponent(self, cmpnt):
        for item in self.components:
            if cmpnt == item.name:
                return item