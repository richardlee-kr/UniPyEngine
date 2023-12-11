import pygame

class AudioClip:
    def __init__(self, source:str):
        self.sound = pygame.mixer.Sound(source)
        
        
    def Play(self, flag:int = 0):
        self.sound.play(flag)
    def Stop(self):
        self.sound.stop()