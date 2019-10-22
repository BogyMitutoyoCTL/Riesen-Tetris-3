import Playground
import RandomBlock
import Ws2812Painter
import time

playground = Playground.Playground(10, 20)

objekt = RandomBlock.RandomBlock()
RndBlock = objekt.get_random_block()

playground.current_block = RndBlock
x = Ws2812Painter.Ws2812Painter()
x.paint(playground)
time.sleep(100)
