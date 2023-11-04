from multiprocessing import Process, Queue

class Scene:
    def __init__(self, name, screen):
        self.sceneName = name
        self.screen = screen
        self.hierarchy = list()
        self.process = list()

    def Update(self):
        for object in self.hierarchy:
            try:
                object.GetComponent("SpriteRenderer").Render(self.screen)
                object.GetComponent("Animator").Update()
            except:
                continue