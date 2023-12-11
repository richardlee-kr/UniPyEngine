class Parameter:
    def __init__(self, name:str, type:str):
        self.name = name
        self.type = type
        self.value = None

        if self.type == "int" or "float":
            self.value = 0
        if self.type == "bool" or "trigger":
            self.value = False