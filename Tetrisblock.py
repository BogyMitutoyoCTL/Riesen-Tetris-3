class Tetrisblock:
    def __init__(self, alphalist):
        self.color = (100, 0, 20)
        self.posotion = (3, 5)
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
        self.orientation +=1
        if self.orientation == 4:
            self.orientation = 0
    def turnleft(self):
        self.orientation -=1
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
      [0, 0, 0]]])

Z=Tetrisblock(
    [[[0,0,0],
      [1,1,0],
      [0,1,1]],

     [[0,0,1],
      [0,1,1],
      [0,1,0]],

     [[1,1,0],
      [0,1,1],
      [0,0,0]],

     [[0,1,0],
      [1,1,0],
      [1,0,0]]])

T=Tetrisblock(
    [[[1,1,1],
      [0,1,0],
      [0,0,0]],

     [[1,0,0],
      [1,1,0],
      [1,0,0]],

     [[0,0,0],
      [0,1,0],
      [1,1,1]],

     [[0,0,1],
      [0,1,1],
      [0,0,1]]])

Lr=Tetrisblock(
    [[[1,1,0],
      [1,0,0],
      [1,0,0]],

     [[0,0,0],
      [1,0,0],
      [1,1,1]],

     [[0,0,1],
      [0,0,1],
      [0,1,1]],

     [[1,1,1],
      [0,0,1],
      [0,0,0]]])

Zr=Tetrisblock(
    [[[0,0,0],
      [0,1,1],
      [1,1,0]],

     [[0,1,0],
      [0,1,1],
      [0,0,1]],

     [[0,1,1],
      [1,1,0],
      [0,0,0]],

     [[1,0,0],
      [1,1,0],
      [0,1,0]]])

I=Tetrisblock(
    [[[0,1,0,0],
      [0,1,0,0],
      [0,1,0,0],
      [0,1,0,0]],

    [[0,0,0,0],
     [0,0,0,0],
     [1,1,1,1],
     [0,0,0,0]],

    [[0,0,1,0],
     [0,0,1,0],
     [0,0,1,0],
     [0,0,1,0]],

    [[0,0,0,0],
     [1,1,1,1],
     [0,0,0,0],
     [0,0,0,0]]])

B=Tetrisblock(
    [[[0,0,0,0],
    [0,1,1,0],
    [0,1,1,0],
    [0,0,0,0]],

    [[0,0,0,0],
    [0,1,1,0],
    [0,1,1,0],
    [0,0,0,0]],

    [[0,0,0,0],
    [0,1,1,0],
    [0,1,1,0],
    [0,0,0,0]],

    [[0,0,0,0],
    [0,1,1,0],
    [0,1,1,0],
    [0,0,0,0]]])

Blocklist=[L,Z,T,Lr,Zr,I,B]

