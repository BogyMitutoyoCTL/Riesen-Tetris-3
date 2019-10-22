import pygame


class Music:
    def __init__(self):
        self.start = 0
        self.repeat = 0
        pygame.mixer.music.load('/home/pi/Riesen-Tetris-3/sounds/tetris-sound.mp3')
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play(0)
        pygame.time.wait(10000  )

pygame.init()
m = Music()
