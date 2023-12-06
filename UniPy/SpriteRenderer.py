from .Component import *
from .Vector import *
from .Sprite import *
import pygame

class SpriteRenderer(Component):
    def __init__(self, sprite:Sprite = None):
        super(SpriteRenderer, self).__init__()
        self.name = "SpriteRenderer"
        self.sprite = sprite

    def Render(self, screen:pygame.Surface):
        if self.sprite != None:
            #TODO Set Flip
            #self.sprite.img = pygame.transform.flip(self.sprite.img, self.transform.scale.x < 0, self.transform.scale.y < 0)
            self.sprite.img = pygame.transform.scale(self.sprite.img, Vector.ToList(Vector.Abs(self.transform.scale) * self.sprite.PPU))
            if self.transform.rotation == 0:
                screen.blit(self.sprite.img, (Vector.ToList(self.transform.position - self.transform.scale * self.sprite.PPU/2)))
            else:
                self.Rotate(screen, self.transform.rotation)
    
    #ref: https://stackoverflow.com/questions/4183208/how-do-i-rotate-an-image-around-its-center-using-pygame
    def Rotate(self, screen:pygame.Surface, angle:float):
        image = self.sprite.img
        pos = Vector.ToList(self.transform.position)
        originPos = (self.sprite.img.get_width()/2, self.sprite.img.get_height()/2)

        image_rect = image.get_rect(topleft = (pos[0] - originPos[0], pos[1]-originPos[1]))
        offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
    
        # roatated offset from pivot to center
        rotated_offset = offset_center_to_pivot.rotate(-angle)

        # roatetd image center
        rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

        # get a rotated image
        rotated_image = pygame.transform.rotate(image, angle)
        rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)

        # rotate and blit the image
        screen.blit(rotated_image, rotated_image_rect)