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
        self.fill(BLACK)

    def fill(self, color):
        self.coordinate_system = list()
        for row in range(self.height):
            rowlist = list()
            for column in range(self.width):
                rowlist.append(color)

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
                    if tetris_x + column_x >= 0 and tetris_y + row_y >= 0:
                        if tetris_x + column_x < self.width and tetris_y + row_y < self.height:
                            self.coordinate_system[row_y + tetris_y][column_x + tetris_x] = color
                column_x = column_x + 1
            row_y = row_y + 1

    def set_pixel(self, x, y, color):
        self.coordinate_system[y][x] = color

    def remove_block(self, tetrisblock: Tetrisblock):

        tetris_x, tetris_y = tetrisblock.position
        templist = tetrisblock.orientations[tetrisblock.orientation]
        row_y = 0
        for row in templist:
            column_x = 0
            for column in row:
                if column == 1:
                    if tetris_x + column_x >= 0 and tetris_y + row_y >= 0:
                        if tetris_x + column_x < self.width and tetris_y + row_y < self.height:
                            self.coordinate_system[row_y + tetris_y][column_x + tetris_x] = BLACK
                column_x = column_x + 1
            row_y = row_y + 1

    def fullrow(self):
        list_of_full_lines = []
        for h in range(0, self.height):
            is_full = True
            for w in range(0, self.width):
                if self.coordinate_system[h][w] == BLACK:
                    is_full = False
                    break
            if is_full:
                list_of_full_lines.append(h)
        return list_of_full_lines

    def delete_line(self, line_numbers):
        for line_number in line_numbers:
            if line_number < self.height:
                for i in reversed(range(1, line_number + 1)):
                    self.coordinate_system[i] = self.coordinate_system[i - 1]
                list_of_columns = []
                for x in range(0, self.width):
                    list_of_columns.append(BLACK)
                self.coordinate_system[0] = list_of_columns

    def print(self):
        print("Start")
        for h in range(0, self.height):
            print(self.coordinate_system[h])
        print("End")

    def collieds(self, tetrisblock):
        # Create a second shadow playgound
        bordersize = 7
        shadow = Playground(width=bordersize + 10 + bordersize, height=bordersize + 20 + bordersize)
        shadow.fill(RED)
        for y in range(bordersize - 4, bordersize + 20):
            for x in range(bordersize, bordersize + 10):
                shadow.set_pixel(x, y, BLACK)
        # copy original
        for original_y in range(0, 20):
            for original_x in range(0, 10):
                original_color = self.coordinate_system[original_y][original_x]
                shadow.set_pixel(original_x + bordersize, original_y + bordersize, original_color)

        three_by_three_field = tetrisblock.orientations[tetrisblock.orientation]
        left_field_side, top_field_side = tetrisblock.position

        # Ermitteln der 9 Ergebnisfarben nach der Multiplikation
        resulting_colors = []
        row_number_of_tetrisblock = 0
        for line_out_of_field in three_by_three_field:
            column_number_of_zeile = 0
            for colum_out_of_field_zero_or_one in line_out_of_field:
                position_in_shadow_system_x = left_field_side + column_number_of_zeile + bordersize
                position_in_shadow_system_y = top_field_side + row_number_of_tetrisblock + bordersize
                color_at_that_position = shadow.coordinate_system[position_in_shadow_system_y][
                    position_in_shadow_system_x]
                if colum_out_of_field_zero_or_one == 0:
                    # Jede Farbe multipliziert mit 0 ergibt schwarz
                    resulting_colors += [BLACK]
                else:
                    if color_at_that_position == BLACK:
                        # Schwarz multipliziert mit jeder Zahl ergibt schwarz
                        resulting_colors += [BLACK]
                    else:
                        # Nicht-Schwarz multipliziert mit 1 ergibt die gleiche Farbe wieder
                        resulting_colors += color_at_that_position
                column_number_of_zeile += 1
            row_number_of_tetrisblock += 1

        # Jetzt haben wir 9 Farben in resulting_colors
        there_was_a_collision = False  # Annahme
        for farbe in resulting_colors:
            if farbe == BLACK:
                pass
            else:
                there_was_a_collision = there_was_a_collision or True
        return there_was_a_collision


if __name__ == "__main__":
    playground = Playground(10, 20)
    playground.clear()

    L = Tetrisblock.L
    L.position = (3, -3)
    assert False == playground.collieds(L)
    L.position = (0, -3)
    assert False == playground.collieds(L)
    L.position = (-1, -3)
    assert True == playground.collieds(L)
    L.position = (8, -3)
    assert False == playground.collieds(L)
    L.position = (9, -3)
    assert True == playground.collieds(L)
    L.position = (0, 17)
    assert False == playground.collieds(L)
    L.position = (0, 18)
    assert True == playground.collieds(L)


    I=Tetrisblock.I
    I.position = (-2, -4)
    assert True == playground.collieds(I)
    I.position = (-1, -4)
    assert False == playground.collieds(I)
    I.position = (8, -4)
    assert False == playground.collieds(I)
    I.position = (9, -4)
    assert True == playground.collieds(I)
    I.position = (-2, 16)
    assert True == playground.collieds(I)
    I.position = (-1, 16)
    assert False == playground.collieds(I)
    I.position = (-1, 17)
    assert True == playground.collieds(I)
    I.position = (8, 17)
    assert True == playground.collieds(I)
    I.position = (8, 16)
    assert False == playground.collieds(I)
    I.position = (9, 16)
    assert True == playground.collieds(I)

    I.turnleft()
    I.position = (3, -6)
    assert True == playground.collieds(I)
    I.position = (3, -5)
    assert False == playground.collieds(I)
    I.position = (3, 18)
    assert False == playground.collieds(I)
    I.position = (3, 19)
    assert True == playground.collieds(I)

    I.turnright()
    I.turnright()
    I.position = (3, -7)
    assert True == playground.collieds(I)