

import Tetrisblock
import Ws2812Painter

BLACK = (0, 0, 0)
RED = (255, 0, 0)


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
        color = tetrisblock.color
        tetris_x, tetris_y = tetrisblock.position

        templist = tetrisblock.orientations[tetrisblock.orientation]
        row_y = 0
        for row in templist:
            column_x = 0
            for column in row:
                if column == 1:
                    self.coordinate_system[row_y + tetris_y][column_x + tetris_x] = color
                column_x = column_x + 1
            row_y = row_y + 1

    def set_pixel(self, x, y, color):
        self.coordinate_system[y][x] = color

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

    def fullrow(self):
        list_of_full_lines = []
        self.coordinate_system.index
        for h in range(0, self.height):
            is_full = True
            for w in range(0, self.width):
                if self.coordinate_system[h][w] == BLACK:
                    is_full = False
                    break
            if is_full:
                list_of_full_lines.append(h)
        return list_of_full_lines


playground = Playground(width=10, height=20)
for i in range(0, 10):
    playground.coordinate_system[5][i] = RED
print(playground.fullrow())
# tetrisblock=Tetrisblock.B
# tetrisblock.position = (6, 4)
# playground.put_block(tetrisblock)
# tetrisblock=Tetrisblock.Z

# playground.put_block(tetrisblock)
# ws2812painter= Ws2812Painter.Ws2812Painter()

# ws2812painter.paint(playground)
# time.sleep(3)
# playground.remove_block(tetrisblock)
# ws2812painter.paint(playground)

# time.sleep(100)
