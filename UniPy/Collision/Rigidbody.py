# TODO Rigidbody
from ..Component import *
from ..Vector import *

class Rigidbody(Component):
    def __init__(self):
        super(Rigidbody, self).__init__()
        self.name = "Rigidbody"

        self.mass = 1
        self.drag = 0
        self.angularDrag = 0.05
        self.useGravity = True

        self.angularVelocity = Vector.zero
        self.velocity = Vector.zero

    def AddForce(self, force:Vector):
        pass