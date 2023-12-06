from .Collider import *
from .BoxBound import *
from ..UniColor import *
import pygame

class BoxCollider(Collider):
    def __init__(self, size = Vector(1,1)):
        super(BoxCollider, self).__init__()
        self.name = "BoxCollider"
        self.bounds = BoxBound(Vector.zero+self.offset, size)
        self.size = size

    def Update(self, screen:pygame.Surface):
        if self.isVisible:
            self.Draw(screen)

    def Draw(self, screen:pygame.Surface):
        #rect = pygame.draw.rect(screen, UniColor.green, [self.transform.position.x-self.size.x/2, self.transform.position.y-self.size.y/2, self.size.x, self.size.y], 1)
        self.Rotate(screen)

    def Rotate(self, screen:pygame.Surface):
        # define a surface (RECTANGLE)  
        image_orig = pygame.Surface((self.size.x , self.size.y))  
        # for making transparent background while rotating an image  
        image_orig.set_colorkey(UniColor.black)  
        # fill the rectangle / surface with green color  
        image_orig.fill(UniColor.green)  
        image_orig.fill(UniColor.black, image_orig.get_rect().inflate(-2,-2))
        # creating a copy of orignal image for smooth rotation  
        image = image_orig.copy()  
        image.set_colorkey(UniColor.black)  
        # define rect for placing the rectangle at the desired position  
        rect = image.get_rect()  
        rect.center = (self.transform.position.x, self.transform.position.y)  

        # making a copy of the old center of the rectangle  
        old_center = rect.center 
        new_image = pygame.transform.rotate(image_orig , self.transform.rotation)  
        rect = new_image.get_rect()  
        # set the rotated rectangle to the old center  
        rect.center = old_center  
        # drawing the rotated rectangle to the screen  
        screen.blit(new_image , rect)  