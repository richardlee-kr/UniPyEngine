from .Scene import *
from ..Collision import *

class SceneManager:
    def __init__(self):
        self.sceneList = list()
        self.currentScene:Scene = None
        self.index = 0

    def AddScene(self, scene:Scene):
        self.sceneList.append(scene)
        if self.currentScene == None:
            self.currentScene = self.sceneList[0]
            self.index = 0

    def LoadScene(self, index:int):
        if index < 0:
            index = 0
        if index > len(self.sceneList):
            index = len(self.sceneList)
        self.currentScene = self.sceneList[index]
        self.index = index
        pygame.display.set_caption(self.currentScene.sceneName)