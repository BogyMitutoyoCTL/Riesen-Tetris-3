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

painter = Ws2812Painter.Ws2812Painter()
painter.paint(playground)
time.sleep(100)

