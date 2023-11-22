from ..Component import *

# TODO: Transition and Graph
class Animator(Component):
    def __init__(self):
        super(Animator, self).__init__()
        self.name = "Animator"
        self.entry = None
        self.states = list()
        self.parameters = list()
        self.animations = list()
        self.transitions = list()
        self.currentClip = None
        self.isPlaying = True

    def Play(self): self.isPlaying = True
    def Stop(self): self.isPlaying = False
    
    def SetClip(self, clip):
        self.currentClip = clip
        self.currentClip.renderer = self.gameObject.GetComponent("SpriteRenderer")

    def Update(self):
        if self.isPlaying:
            self.currentClip.Play()
