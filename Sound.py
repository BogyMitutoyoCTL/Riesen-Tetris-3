import pygame


class Sound:
    def __init__(self):
        self.volume = 1.0

    def play(self, filename, channel_number=1):
        channel = pygame.mixer.Channel(channel_number)
        sound = pygame.mixer.Sound(filename)
        channel.set_volume(self.volume)
        channel.play(sound)

    def complete_line1(self):
        self.play('./sounds/complete_line1.wav', 0)

    def complete_line2(self):
        self.play('./sounds/complete_line1.wav', 0)

    def complete_line3(self):
        self.play('./sounds/complete_line3.wav', 0)

    def complete_line4(self):
        self.play('./sounds/complete_line4.wav', 0)

    def reached_limit(self):
        self.play('./sounds/reached_limit.wav', 1)

    def reached_score(self):
        self.play('./sounds/reached_score.wav', 2)

    def game_over(self):
        self.play('./sounds/game_over.wav', 0)

    def warning(self):
        self.play('./sounds/warning.wav', 3)

    def speed_increase(self):
        self.play('./sounds/speed_increase.wav', 4)

    def new_highscore(self):
        self.play('./sounds/new_highscore.wav', 2)

    def set_volume(self, volume):
        self.volume = volume

    def play_sound_for_lines(self, line_count):
        if line_count == 1:
            self.complete_line1()
        if line_count == 2:
            self.complete_line2()
        if line_count == 3:
            self.complete_line3()
        if line_count == 4:
            self.complete_line4()
