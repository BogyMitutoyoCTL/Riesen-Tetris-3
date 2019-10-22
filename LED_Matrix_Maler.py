import time

from luma.core.interface.serial import spi, noop
from luma.core.legacy import text
from luma.core.legacy.font import proportional, SINCLAIR_FONT
from luma.core.render import canvas
from luma.led_matrix.device import max7219


def demo():
    # create matrix device
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=4, block_orientation=-90,
                     rotate=2, blocks_arranged_in_reverse_order=False)

    msg = "Test"
    with canvas (device) as draw:
        text(draw, (0,0), msg, fill="white", font=proportional(SINCLAIR_FONT))
    time.sleep(10)
if __name__ == "__main__":



    try:
        demo()
    except KeyboardInterrupt:
        pass