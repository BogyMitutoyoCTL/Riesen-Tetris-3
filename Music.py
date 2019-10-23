
import pygame


class Music:
    def __init__(self, volume):
        self.start = 0
        self.repeat = 0
        self.volume =volume
        pygame.mixer.music.load('./sounds/Tetris_theme.ogg')
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(0)
