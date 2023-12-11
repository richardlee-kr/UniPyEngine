from ..Component import *
from .AnimGraph import *
from .Parameter import *
from .AnimationClip import *

class Animator(Component):
    def __init__(self):
        super(Animator, self).__init__()
        self.name = "Animator"

        self.animGraph = AnimGraph(self)
        self.parameters = list() #[Parameter]s

        self.currentClip = None
        self.isPlaying = True
        self.AddParameter("unconditional", "trigger")

    def Play(self): self.isPlaying = True
    def Stop(self): self.isPlaying = False
    
# Set currentClip
    def SetClip(self, clip: AnimationClip):
        self.currentClip = clip
        self.currentClip.renderer = self.gameObject.GetComponent("SpriteRenderer")

    def Update(self, screen):
        if self.currentClip != self.animGraph.currentNode.clip:
            self.SetClip(self.animGraph.currentNode.clip)
        if self.isPlaying:
            #print("Playing")
            self.currentClip.Play()
            if self.currentClip.isFinished == True:
                print("Finished")
                self.CheckTransition("unconditional")

# Add elements
    def AddParameter(self, name:str, type:str):
        self.parameters.append(Parameter(name, type))

    def AddNode(self, name:str, clip:AnimationClip):
        _node = self.animGraph.AddNode(name, clip)
        if self.currentClip == None:
            self.SetClip(self.animGraph.currentNode.clip)
        del _node

    def AddTransition(self, fromNodeName:str, toNodeName:str, condition:Condition):
        self.animGraph.AddTransition(fromNodeName, toNodeName, condition)

# Set Paramter in Animator
    def SetBool(self, paramName:str, value:bool):
        for param in self.parameters:
            if param.type == "bool" and param.name == paramName:
                param.value = value
                self.CheckTransition(param.name)

    def SetInt(self, paramName:str, value:int):
        for param in self.parameters:
            if param.type == "int" and param.name == paramName:
                param.value = value
                self.CheckTransition(param.name)

    def SetFloat(self, paramName:str, value:float):
        for param in self.parameters:
            if param.type == "float" and param.name == paramName:
                param.value = value
                self.CheckTransition(param.name)

    def SetTrigger(self, paramName:str):
        for param in self.parameters:
            if param.type == "trigger" and param.name == paramName:
                self.CheckTransition(param.name)

# Check whether animator transit
    def CheckTransition(self, paramName:str):
        self.animGraph.CheckTransition(paramName)
