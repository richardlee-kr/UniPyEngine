from ..Component import *
from ..GameObject import *
from ..Vector import *
from .Bound import *

class Collider(Component):
    def __init__(self):
        super(Collider, self).__init__()
        self.name = "Collider"
        self.offset = Vector.zero
        self.bounds = None
        self.isTrigger = False
        self.isVisible = True

    #TODO Trigger callback
    def OnTriggerEnter(self, func):
        other = GameObject("asdf") #TODO other should be objects that is overlapped by this gameObject
        func(other)
    def OnTriggerStay(self, func):
        print("TriggerStay")
    def OnTriggerExit(self, func):
        print("TriggerExit")