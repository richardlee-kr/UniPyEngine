import pygame

class Scene:
    def __init__(self, name:str, screen:pygame.Surface):
        self.sceneName = name
        self.screen = screen
        self.hierarchy = list()

    def FindObject(self, name:str) :
        for object in self.hierarchy:
            if object.name == name:
                return object
        return None

    def Update(self):
        for object in self.hierarchy:
            if object.transform.relativePosition.x > 1080 + 20 or object.transform.relativePosition.x < 0 - 20 or object.transform.relativePosition.y > 720 + 20 or object.transform.relativePosition.y < 0 - 20:
                object.DestroyFrom(self)
                continue

            #print(len(self.hierarchy))
            #object.Update()
            for comp in object.components:
                object.GetComponent(comp.name).Update(self.screen)
            '''
            try:
                object.GetComponent("Rigidbody").Update()
            except:
                pass
            try:
                object.GetComponent("Animator").Update()
            except:
                pass
            try:
                object.GetComponent("BoxCollider").Update(self.screen)
            except:
                pass
            try:
                object.GetComponent("CircleCollider").Update(self.screen)
            except:
                pass
            try:
                object.GetComponent("Image").Update(self.screen)
            except:
                pass
            try:
                object.GetComponent("Text").Update(self.screen)
            except:
                pass
            try:
                object.GetComponent("Button").Update(self.screen)
            except:
                pass
            try:
                object.GetComponent("SpriteRenderer").Update(self.screen)
            except:
                continue
            '''