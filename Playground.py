import time
import RandomBlock
import Tetrisblock
import Ws2812Painter

BLACK = (0, 0, 0)


#    Coordinate system
#    ----------> X
#    | 0/0              widht/0
#    |
#    |
#    |
#    v
#
#    Y
#
#
#
#      0/height             widht/height

class Playground:
    def __init__(self, width, height):
        self.coordinate_system = list()

        for row in range(height):
            rowlist = list()
            for column in range(width):
                rowlist.append(BLACK)

            self.coordinate_system.append(rowlist)

        self.height = height
        self.width = width


    def clear(self):
        self.coordinate_system = list()
        for row in range(self.height):
            rowlist = list()
            for column in range(self.width):
                rowlist.append(BLACK)

            self.coordinate_system.append(rowlist)

    def put_block(self, tetrisblock: Tetrisblock):
        c = tetrisblock.color
        tetris_x, tetris_y = tetrisblock.position

        templist = tetrisblock.orientations[tetrisblock.orientation]
        row_y = 0
        for row in templist:
            column_x = 0
            for column in row:
                if column == 1:
                    self.coordinate_system[row_y + tetris_y][column_x + tetris_x] = c
                column_x = column_x + 1
            row_y = row_y + 1

    def remove_block(self, tetrisblock: Tetrisblock):

        tetris_x, tetris_y = tetrisblock.position
        templist = tetrisblock.orientations[tetrisblock.orientation]
        row_x = 0
        for row in templist:
            column_x = 0
            for column in row:
                if column == 1:
                    self.coordinate_system[row_x + tetris_y][column_x + tetris_x] = BLACK
                column_x = column_x + 1
            row_x = row_x + 1