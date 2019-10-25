import pygame


class Music:
    def __init__(self, volume):
        self.volume = volume

    def start(self):
        pygame.mixer.music.load('./sounds/Tetris_theme.ogg')
        pygame.mixer.music.set_volume(self.volume)
        pygame.mixer.music.play(0)

    def stop(self):
        pygame.mixer.music.stop()
