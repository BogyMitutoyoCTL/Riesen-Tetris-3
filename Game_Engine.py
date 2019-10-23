import Playground
import RandomBlock
import Ws2812Painter
# import LED_Matrix_Maler
import time
# import pygame
# import Points
# import Music
import Tetrisblock

# import Sound
# import control_feedback

playground = Playground.Playground(10, 20)

objekt = RandomBlock.RandomBlock()

currentBlock = objekt.get_random_block()
nextBlock = objekt.get_random_block()

playground.put_block(currentBlock)

painter = Ws2812Painter.Ws2812Painter()
painter.paint(playground)

# Wenn Start gedrückt wird muss ein Random Block von oben kommen
while True:
    # Ein Random Block wird in der Led-Matrix gemalt
    # Der Random Block kommt oben aufs Spielfeld
    # Ein neuer Random Block wird auf der Led-Matrix gezeichnet
    # Der Block fällt in einer Zeitspanne immer eine Reihe nach unten
    # Der Block fällt in einer Zeitspanne immer eine Reihe nach unten
    # ...
    # Der Block kommt unten an oder trifft auf einen anderen Block evtl. mit Sound
    # Wenn eine Reihe voll ist werden Punkte hinzugezählt
    # Das Spiel wird schneller, da es mehr Punkte gibt
    # Der Block von der Led-Matrix kommt aufs Spielfeld
    # kann er nicht mehr aufs Spielfeld, endet das Spiel. Wenn nicht, geht das Spiel weiter
    # Alles wiederholt sich

    playground.remove_block(currentBlock)
    x, y = currentBlock.position

    currentBlock.position = x, y + 1
    playground.put_block(currentBlock)
    time.sleep(1)

    painter.paint(playground)
