from ..Component import *
from .Text import *
from .Image import *

class Button(Component):
    def __init__(self, action = None):
        super(Button, self).__init__()
        self.name = "Button"
        self.action = action

        self.normalColor = UniColor.white
        self.hoverColor = (200,200,200)

        self.isClicked = False

    def Update(self, screen):
        image:Image = self.gameObject.GetComponent("Image")
        #print(self.transform.relativePosition)
        click = pygame.mouse.get_pressed()
        if self.IsMouseHover():
            image.color = self.hoverColor
            if click[0] == 1 and self.isClicked == False:
                self.isClicked = True
                print("buttonClicked")
                if self.action != None:
                    self.action()
            if click[0] == 0 and self.isClicked == True:
                self.isClicked = False
        else:
            image.color = self.normalColor

    
    def IsMouseHover(self) -> bool:
        mousePos = pygame.mouse.get_pos()

        if self.transform.relativePosition.x - self.transform.width/2 *32 < mousePos[0] < self.transform.relativePosition.x + self.transform.width/2 *32:
            if self.transform.relativePosition.y - self.transform.height/2 *32 < mousePos[1] < self.transform.relativePosition.y + self.transform.height/2 *32:
                return True
        return False