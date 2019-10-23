from luma.core.interface.serial import spi, noop
from luma.core.legacy import text
from luma.core.legacy.font import proportional, SINCLAIR_FONT
from luma.core.render import canvas
from luma.led_matrix.device import max7219


class Maler():

    def draw(self, points, block):
        serial = spi(port=0, device=0, gpio=noop())
        device = max7219(serial, cascaded=4, block_orientation=-90,
                         rotate=2, blocks_arranged_in_reverse_order=False)
        msg = str(points)
        with canvas(device) as draw:
            text(draw, (0, 0), msg, fill="white", font=proportional(SINCLAIR_FONT))
            self.put_block(block,draw)

    def put_block(self, tetrisblock, draw):


        tetris_x=26
        tetris_y=0
        templist = tetrisblock.orientations[tetrisblock.orientation]
        row_y = 0
        for row in templist:
            column_x = 0
            for column in row:
                if column == 1:
                    gesamt_x = tetris_x + column_x * 2
                    gesamt_y = tetris_y + row_y * 2
                    draw.rectangle((gesamt_x, gesamt_y, gesamt_x + 1, gesamt_y + 1), fill="white")
                column_x = column_x + 1
            row_y = row_y + 1

#Leonardo = Maler()
#Leonardo.draw(20, RandomBlock.RandomBlock().get_random_block())
#time.sleep(5)
