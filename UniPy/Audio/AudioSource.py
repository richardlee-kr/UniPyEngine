from .AudioClip import *
from ..Component import *

class AudioSource(Component):
    def __init__(self):
        super(AudioSource, self).__init__()
        self.name = "AudioSource"

        self.clip:AudioClip = None
        self.loop = False
        self.volume = 1.0

    def set_volume(self, value:float):
        self.volume = value
        self.clip.sound.set_volume(value)

    def Play(self):
        self.clip.Play()
    def Stop(self):
        self.clip.Stop()