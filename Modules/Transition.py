class Transition:
    def __init__(self, _from, _to):
        self._from = _from
        self._to = _to
        self.condition = dict()
    
    def AddCondition(self, condition):
        self.condition[condition.name] = condition