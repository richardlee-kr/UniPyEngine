from multiprocessing import Process, Queue

class Scene:
    def __init__(self, name, screen):
        self.sceneName = name
        self.screen = screen
        self.hierarchy = list()

    def Update(self):
        for object in self.hierarchy:
            try:
                object.GetComponent("SpriteRenderer").Render(self.screen)
            except:
                pass
            try:
                object.GetComponent("Animator").Update()
            except:
                pass
            try:
                object.GetComponent("BoxCollider").Update(self.screen)
            except:
                continue
            try:
                object.GetComponent("CircleCollider").Update(self.screen)
            except:
                continue