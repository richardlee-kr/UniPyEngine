from .AnimNode import *
from .AnimationClip import AnimationClip
from .Condition import *
from .Parameter import Parameter

'''
TODO
- Transition when animation end
'''

class AnimGraph:
    def __init__(self, animator, entry:AnimNode = None):
        self.animator = animator
        self.entryNode = entry
        self.currentNode = self.entryNode
        self.nodes = list()

# Add node to graph
    def AddNode(self, name:str, clip:AnimationClip) -> AnimNode:
        _node = AnimNode(name, clip)
        self.nodes.append(_node)
        if self.currentNode == None:
            self.entryNode = _node
            self.currentNode = _node
        return _node

# Add transition to node
    def AddTransition(self, fromNodeName:str, toNodeName:str, condition:Condition):
        _from:AnimNode = None
        _to:AnimNode  = None
        for node in self.nodes:
            if node.name == fromNodeName:
                _from = node
            if node.name == toNodeName:
                _to = node

        _from.AddTransition(_to, condition)

# Change Node
    def ChangeNode(self, targetNode:AnimNode):
        self.currentNode = targetNode

# Check whether animator transit
    def CheckTransition(self, paramName:str):
        for transition in self.currentNode.transitions:
            if transition.condition.targetParamName == paramName:
                shouldTransit = self.CheckCondition(self.GetParameter(paramName), self.currentNode.transitions)
                if shouldTransit:
                    self.ChangeNode(transition.toNode)

# Check whether condition to transit is true
    def CheckCondition(self, parameter:Parameter, transitions:list) -> bool:
        for transition in transitions:
            _condition:Condition = transition.condition
            if _condition.conditionType == ConditionType.EQUAL:
                return parameter.value == _condition.value
            elif _condition.conditionType == ConditionType.LESS:
                return parameter.value < _condition.value
            elif _condition.conditionType == ConditionType.LESS_EQUAL:
                return parameter.value <= _condition.value
            elif _condition.conditionType == ConditionType.BIGGER:
                return parameter.value > _condition.value
            elif _condition.conditionType == ConditionType.BIGGER_EQUAL:
                return parameter.value >= _condition.value
            elif _condition.conditionType == ConditionType.NOT:
                return parameter.value != _condition.value
            elif _condition.conditionType == ConditionType.TRIGGERED:
                parameter.value = False
                return True

    def GetParameter(self, name) -> Parameter:
        for param in self.animator.parameters:
            if param.name == name:
                return param