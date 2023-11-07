class Scene:
    def __init__(self, name, screen):
        self.sceneName = name
        self.screen = screen
        self.hierarchy = list()

    def Update(self):
        for object in self.hierarchy:
            if object.transform.position.x > 1080 + 20 or object.transform.position.x < 0 - 20 or object.transform.position.y > 720 + 20 or object.transform.position.y < 0 - 20:
                self.hierarchy.remove(object)

            object.Update()
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
                pass
            try:
                object.GetComponent("CircleCollider").Update(self.screen)
            except:
                continue