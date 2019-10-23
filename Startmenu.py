import time

import Playground
import Tetrisblock
import Ws2812Painter

playground = Playground.Playground(width=10, height=20)
square = Tetrisblock.B
square.position = (1, 4)
playground.put_block(square)
painter = Ws2812Painter.Ws2812Painter()
painter.paint(playground)
time.sleep(10)