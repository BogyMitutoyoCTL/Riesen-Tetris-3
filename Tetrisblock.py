class Tetrisblock:
    def __init__(self, alphalist, color):
        self.color = color
        self.position = (0, 0)
        self.orientations = alphalist
        self.orientation = 0

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
        if self.orientation == 0:
            self.orientation = 3


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
      [1, 1]]], (255, 127, 39))

Blocklist = [L, Z, T, Lr, Zr, I, B]
