from .Transform import *
from .Scene import Scene

class GameObject:
    def __init__(self, name:str):
        self.name = name
        self.layer = "Default"
        self.tag = "Untagged"
        self.transform = Transform()
        self.components = list()
        self.AddComponent(self.transform)
    
    def AddComponent(self, cmpnt:Component):
        self.components.append(cmpnt)
        cmpnt.gameObject = self
        cmpnt.transform = self.transform

    def GetComponent(self, cmpnt:Component) -> Component:
        for item in self.components:
            if cmpnt == item.name:
                return item

    def Update(self):
        self.transform.Update()

    def DestroyFrom(self, scene:Scene):
        scene.hierarchy.remove(self)
        del self

    @staticmethod
    def Instantiate(scene, object, pos:Vector, rot:float):
        scene.hierarchy.append(object)
        object.transform.position = pos
        object.transform.Rotate(rot)