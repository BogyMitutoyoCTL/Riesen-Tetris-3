import pygame

class Controller:
    def __init__(self):
        self.running = True
        self.joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
        for joystick in self.joysticks:
            joystick.init()
        self.listofpressedbuttons = []
        self.listofreleasedbuttons = []
        self.remember_keyboard = []

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

   # def joystick_simple_press(self):
        # wenn Taste gedrückt gehalten wird
            # solange es "True" ist schleife den output --> einen dauer output

    def get_joystick_buttons(self):
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.remember_keyboard += ["down"]
                if event.key == pygame.K_UP:
                    self.listofpressedbuttons += ["B"]
                if event.key == pygame.K_RIGHT:
                    self.listofpressedbuttons += ["right"]
                if event.key == pygame.K_LEFT:
                    self.listofpressedbuttons+= ["left"]
                if event.key == pygame.K_RETURN:
                    self.listofpressedbuttons += ["Start"]
                if event.key == pygame.K_SPACE:
                    self.listofpressedbuttons += ["Pause"]
            elif event.type == pygame.KEYUP:
                try:
                    if event.key == pygame.K_DOWN:
                        self.remember_keyboard.remove("down")
                    if event.key == pygame.K_UP:
                        self.remember_keyboard.remove("B")
                    if event.key == pygame.K_RIGHT:
                        self.remember_keyboard.remove("right")
                    if event.key == pygame.K_LEFT:
                        self.remember_keyboard.remove("left")
                    if event.key == pygame.K_RETURN:
                        self.remember_keyboard.remove("Start")
                except ValueError:
                    pass
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
                    self.listofreleasedbuttons += ["Pause"]
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
                        if  "right" not in self.listofpressedbuttons:
                            self.listofpressedbuttons += ["right"]
                    elif event.value < -0.4:
                        if "left" not in self.listofpressedbuttons:
                            self.listofpressedbuttons += ["left"]
                if event.axis == 1:
                    if event.value > 0.4:
                        if  "down" not in self.listofpressedbuttons:
                            self.listofpressedbuttons += ["down"]
                    if event.value < -0.4:
                        if "up" not in self.listofpressedbuttons:
                            self.listofpressedbuttons += ["up"]

            elif event.type == pygame.JOYHATMOTION:
                if event.value[0] == 1:
                    self.listofpressedbuttons += ["right"]
                elif event.value[0] == -1:
                    self.listofpressedbuttons += ["left"]
                if event.value[1] == 1:
                    self.listofpressedbuttons += ["up"]
                elif event.value[1] == -1:
                    self.listofpressedbuttons += ["down"]
        self.listofpressedbuttons += self.remember_keyboard
        # print(self.remember_keyboard)

    def add_action(self, action):
        self.listofpressedbuttons += [action]


if __name__ == "__main__":
    background_colour = (255, 255, 255)
    (width, height) = (300, 200)
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Tutorial 1')
    screen.fill(background_colour)
    pygame.display.flip()
    running = True
    c = Controller()
    while c.running:
        c.get_joystick_buttons()
        c.pressed()
        c.released()
        pygame.time.wait(5)
    print("Ende")
