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
                self.coordinate_system[0]=list_of_columns

    def print(self):
        print("Start")
        for h in range(0, self.height):
            print(self.coordinate_system[h])
        print("End")

    def collieds(self, tetrisblock):

        drei_mal_drei_feld = tetrisblock.orientations[tetrisblock.orientation]
        feld_linker_rand, feld_oberer_rand = tetrisblock.position

        # Ermitteln der 9 Ergebnisfarben nach der Multiplikation
        resulting_colors = []
        row_number_of_tetrisblock = 0
        for zeile_aus_feld in drei_mal_drei_feld:
            column_number_of_zeile = 0
            for spalte_aus_feld_null_oder_eins in zeile_aus_feld:
                position_in_coordinate_system_x = feld_linker_rand + column_number_of_zeile
                position_in_coordinate_system_y = feld_oberer_rand + row_number_of_tetrisblock
                color_at_that_position = self.coordinate_system[position_in_coordinate_system_y][position_in_coordinate_system_x]
                if spalte_aus_feld_null_oder_eins == 0:
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
        es_gab_eine_kollision = False # Annahme
        for farbe in resulting_colors:
            if farbe == BLACK:
                pass
            else :
                es_gab_eine_kollision = es_gab_eine_kollision or True
        return es_gab_eine_kollision

if __name__ == "__main__":
    playground = Playground(width=10, height=20)
    for i in range(0, 10):
        for o in range(0,20):
            playground.coordinate_system[o][i] = BLACK
    r=playground.collieds(Tetrisblock.L)
    print(r)
