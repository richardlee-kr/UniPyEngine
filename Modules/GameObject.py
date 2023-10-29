from Modules.Transform import *

class GameObject:
    def __init__(self):
        self.name = "_"
        self.components = list()
        self.transform = Transform()
    
    def AddComponent(self, cmpnt):
        self.components.append(cmpnt)
        cmpnt.gameObject = self
        cmpnt.transform = self.transform