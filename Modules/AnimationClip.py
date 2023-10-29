from Modules.Transition import *
import pygame

class AnimationClip:
    def __init__(self, clock, fps):
        self.frames = list()
        self.currentFrame = 0
        self.clock = clock
        self.fps = fps
        self.transitions = list()

        self.timer = 0

    def AddTransition(self, transition):
        self.transitions.append(transition)
    
    def Play(self):
        self.timer += self.clock.get_time() / 1000
        print(self.currentFrame)
        if self.timer >= 1/self.fps:
            self.timer = 0
            self.currentFrame = (self.currentFrame+1) % 4