from .Scene import *
from ..Collision import *
'''
TODO SceneManagement; LoadScene(Change Scene)
'''
class SceneManager:
    def __init__(self):
        self.sceneList = list()
        self.currentScene:Scene = None

    def AddScene(self, scene:Scene):
        self.sceneList.append(scene)

    def LoadScene(self, index:int):
        self.currentScene = self.sceneList[index]