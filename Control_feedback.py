import pygame

class Controller:
    def __init__(self):
        pygame.init()

        joystick = pygame.joystick.Joystick(0)
        joystick.init()

        self.joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
        self.listofpressedbuttons = []
        self.listofreleasedbuttons = []


    def pressed(self):
        self.get_joystick_buttons()
        temp = self.listofpressedbuttons
        self.listofpressedbuttons = []
        return temp

    def released(self):
        self.get_joystick_buttons()
        temp = self.listofreleasedbuttons
        self.listofreleasedbuttons = []
        return temp


    def get_joystick_buttons(self):
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_DOWN:
                    self.listofpressedbuttons += ["down"]
                if event.key == pygame.K_UP:
                    self.listofpressedbuttons += ["up"]
                if event.key == pygame.K_RIGHT:
                    self.listofpressedbuttons += ["right"]
                if event.key == pygame.K_LEFT:
                    self.listofpressedbuttons += ["left"]
            elif event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0:
                    self.listofpressedbuttons += ["A"]
                if event.button == 1:
                    self.listofpressedbuttons += ["B"]
                if event.button == 2:
                    self.listofpressedbuttons += ["X"]
                if event.button == 3:
                    self.listofpressedbuttons += ["Y"]
                if event.button == 4:
                    self.listofpressedbuttons += ["LB"]
                if event.button == 5:
                    self.listofpressedbuttons += ["RB"]
                if event.button == 6:
                    self.listofpressedbuttons += ["Back"]
                if event.button == 7:
                    self.listofpressedbuttons += ["Start"]
                if event.button == 8:
                    self.listofpressedbuttons += ["X_box"]
                if event.button == 9:
                    self.listofpressedbuttons += ["Left Joystick pressed"]
                if event.button == 10:
                    self.listofpressedbuttons += ["Right Joystick pressed"]
            elif event.type == pygame.JOYBUTTONUP:
                if event.button == 0:
                    self.listofreleasedbuttons += ["A"]
                if event.button == 1:
                    self.listofreleasedbuttons += ["B"]
                if event.button == 2:
                    self.listofreleasedbuttons += ["X"]
                if event.button == 3:
                    self.listofreleasedbuttons += ["Y"]
                if event.button == 4:
                    self.listofreleasedbuttons += ["LB"]
                if event.button == 5:
                    self.listofreleasedbuttons += ["RB"]
                if event.button == 6:
                    self.listofreleasedbuttons += ["Back"]
                if event.button == 7:
                    self.listofreleasedbuttons += ["Start"]
                if event.button == 8:
                    self.listofreleasedbuttons += ["X_Box"]
                if event.button == 9:
                    self.listofreleasedbuttons += ["Left Joystick released"]
                if event.button == 10:
                    self.listofreleasedbuttons += ["Right Joystick released"]
            elif event.type == pygame.JOYAXISMOTION:
                if event.axis == 0:
                    if event.value > 0.4:
                        self.listofpressedbuttons += ["right"]
                    elif event.value < -0.4:
                        self.listofpressedbuttons += ["left"]
                if event.axis == 1:
                    if event.value > 0.4:
                        self.listofpressedbuttons +=["down"]
                    if event.value < -0.4:
                        self.listofpressedbuttons +=["up"]


if __name__ == "__main__":
    c = Controller()
    while True:
        c.get_joystick_buttons()
        print(c.pressed())
        print(c.released())
        pygame.time.wait(50)
    done = False
