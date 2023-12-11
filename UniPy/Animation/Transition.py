from .Condition import Condition

class Transition:
    def __init__(self, fromNode, toNode, _condition:Condition):
        self.fromNode = fromNode
        self.toNode = toNode
        self.condition = _condition