from .AnimationClip import AnimationClip
from .Transition import *

class AnimNode:
    def __init__(self, name:str, clip:AnimationClip = None):
        self.name = name
        self.transitions = list()
        self.clip = clip

    def AddTransition(self, toNode, condition:Condition):
        self.transitions.append(Transition(self, toNode, condition))
