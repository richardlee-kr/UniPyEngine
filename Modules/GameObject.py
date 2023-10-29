from Modules.Transform import *

class GameObject:
    def __init__(self, name):
        self.name = name
        self.transform = Transform()
        self.components = list()
        self.components.append(self.transform)
    
    def AddComponent(self, cmpnt):
        self.components.append(cmpnt)
        cmpnt.gameObject = self
        cmpnt.transform = self.transform

    def GetComponent(self, cmpnt):
        for item in self.components:
            if cmpnt == item.name:
                return item