from random import randint


class Tetrisblock:
    def __init__(self, alphalist, color):
        self.color = color
        self.position = (-1, -1)
        self.orientations = alphalist
        self.orientation = 0

    @property
    def x(self) -> int:
        return self.position[0]

    @property
    def y(self) -> int:
        return self.position[1]

    def showme(self):
        templist = self.orientations[self.orientation]
        for row in templist:
            for colum in row:
                if colum == 1:
                    print("x", end="")
                else:
                    print(" ", end="")
            print()
        print()

    def turnright(self):
        self.orientation += 1
        if self.orientation == 4:
            self.orientation = 0

    def turnleft(self):
        self.orientation -= 1
        if self.orientation == -1:
            self.orientation = 3

    def clone(self):
        temp = Tetrisblock(None, None)
        temp.color = self.color
        temp.position = self.position
        temp.orientations = self.orientations
        temp.orientation = self.orientation
        return temp

    def random_orientation(self):
        self.orientation = randint(0, 3)

   # def random_color(self):
    #    color_list = list(
     #       [(0, 255, 255), (255, 0, 255), (0, 255, 0), (0, 0, 255), (255, 0, 0), (255, 255, 0), (255, 127, 39)])
      #  number_of_colors = len(color_list)
       # self.color = color_list[randint(0, number_of_colors - 1)]

    def moveright(self):
        self.position = self.x + 1, self.y

    def moveleft(self):
        self.position = self.x - 1, self.y

    def movedown(self):
        self.position = self.x, self.y+1


L = Tetrisblock(
    [[[1, 1, 0, ],
      [0, 1, 0, ],
      [0, 1, 0]],

     [[0, 0, 0],
      [1, 1, 1],
      [1, 0, 0]],

     [[0, 1, 0],
      [0, 1, 0],
      [0, 1, 1]],

     [[0, 0, 1],
      [1, 1, 1],
      [0, 0, 0]]], (0, 255, 255))

Z = Tetrisblock(
    [[[0, 0, 0],
      [1, 1, 0],
      [0, 1, 1]],

     [[0, 0, 1],
      [0, 1, 1],
      [0, 1, 0]],

     [[1, 1, 0],
      [0, 1, 1],
      [0, 0, 0]],

     [[0, 1, 0],
      [1, 1, 0],
      [1, 0, 0]]], (255, 0, 255))

T = Tetrisblock(
    [[[1, 1, 1],
      [0, 1, 0],
      [0, 0, 0]],

     [[1, 0, 0],
      [1, 1, 0],
      [1, 0, 0]],

     [[0, 0, 0],
      [0, 1, 0],
      [1, 1, 1]],

     [[0, 0, 1],
      [0, 1, 1],
      [0, 0, 1]]], (0, 255, 0))

Lr = Tetrisblock(
    [[[1, 1, 0],
      [1, 0, 0],
      [1, 0, 0]],

     [[0, 0, 0],
      [1, 0, 0],
      [1, 1, 1]],

     [[0, 0, 1],
      [0, 0, 1],
      [0, 1, 1]],

     [[1, 1, 1],
      [0, 0, 1],
      [0, 0, 0]]], (0, 0, 255))

Zr = Tetrisblock(
    [[[0, 0, 0],
      [0, 1, 1],
      [1, 1, 0]],

     [[0, 1, 0],
      [0, 1, 1],
      [0, 0, 1]],

     [[0, 1, 1],
      [1, 1, 0],
      [0, 0, 0]],

     [[1, 0, 0],
      [1, 1, 0],
      [0, 1, 0]]], (255, 0, 0))

I = Tetrisblock(
    [[[0, 1, 0, 0],
      [0, 1, 0, 0],
      [0, 1, 0, 0],
      [0, 1, 0, 0]],

     [[0, 0, 0, 0],
      [0, 0, 0, 0],
      [1, 1, 1, 1],
      [0, 0, 0, 0]],

     [[0, 0, 1, 0],
      [0, 0, 1, 0],
      [0, 0, 1, 0],
      [0, 0, 1, 0]],

     [[0, 0, 0, 0],
      [1, 1, 1, 1],
      [0, 0, 0, 0],
      [0, 0, 0, 0]]], (255, 255, 0))

B = Tetrisblock(
    [[[1, 1],
      [1, 1]],

     [[1, 1],
      [1, 1]],

     [[1, 1],
      [1, 1]],

     [[1, 1],
      [1, 1]]], (255, 135,15))

Blocklist = [L, Z, T, Lr, Zr, I, B]
