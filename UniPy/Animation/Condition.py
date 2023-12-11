from enum import Enum

class ConditionType(Enum):
    LESS = 0
    LESS_EQUAL = 1
    EQUAL = 2
    BIGGER_EQUAL = 3
    BIGGER = 4
    NOT = 5
    TRIGGERED = 6

class Condition:
    def __init__(self, targetParamName:str, type:str):
        self.targetParamName = targetParamName
        self.type = type
        self.conditionType = ConditionType.EQUAL
        self.value = None

        if self.type == "int" or "float":
            self.value = 0
        if self.type == "bool" or "trigger":
            self.value = True

