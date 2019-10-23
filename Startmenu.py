
import time

import Playground
import Tetrisblock
import Ws2812Painter

playground = Playground.Playground(width=10, height=20)

square = Tetrisblock.B
square.position = (1, 4)
playground.put_block(square)

square = Tetrisblock.Zr
square.position = (4, 1)
playground.put_block(square)

square = Tetrisblock.L
square.position = (6, 5)
square.turnleft()
playground.put_block(square)

square = Tetrisblock.I
square.position = (1, 12)
square.turnleft()
playground.put_block(square)

square = Tetrisblock.Lr
square.position = (1, 15)
square.turnleft()
square.turnleft()
playground.put_block(square)

square = Tetrisblock.T
square.position = (6, 14)
playground.put_block(square)

square = Tetrisblock.B
square.position = (6, 17)
playground.put_block(square)

playground.set_pixel(0, 8, (255, 0, 0))
playground.set_pixel(0, 9, (255, 0, 0))
playground.set_pixel(0, 10, (255, 0, 0))
playground.set_pixel(0, 11, (255, 0, 0))
playground.set_pixel(1, 8, (255, 0, 0))
playground.set_pixel(1, 10, (255, 0, 0))
playground.set_pixel(2, 8, (255, 0, 0))
playground.set_pixel(2, 9, (255, 0, 0))
playground.set_pixel(2, 10, (255, 0, 0))

playground.set_pixel(3, 8, (0, 0, 255))
playground.set_pixel(3, 9, (0, 0, 255))
playground.set_pixel(3, 10, (0, 0, 255))
playground.set_pixel(3, 11, (0, 0, 255))
playground.set_pixel(4, 11, (0, 0, 255))

playground.set_pixel(5, 9, (0, 255, 0))
playground.set_pixel(5, 10, (0, 255, 0))
playground.set_pixel(5, 11, (0, 255, 0))
playground.set_pixel(6, 8, (0, 255, 0))
playground.set_pixel(6, 10, (0, 255, 0))
playground.set_pixel(7, 9, (0, 255, 0))
playground.set_pixel(7, 10, (0, 255, 0))
playground.set_pixel(7, 11, (0, 255, 0))

playground.set_pixel(7, 8, (255, 127, 39))
playground.set_pixel(8, 9, (255, 127, 39))
playground.set_pixel(8, 10, (255, 127, 39))
playground.set_pixel(8, 11, (255, 127, 39))
playground.set_pixel(9, 8, (255, 127, 39))

painter = Ws2812Painter.Ws2812Painter()
painter.paint(playground)
time.sleep(10000)
