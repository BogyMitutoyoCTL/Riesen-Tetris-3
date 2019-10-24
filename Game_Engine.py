import Playground
import RandomBlock
import Ws2812Painter
import LED_Matrix_Maler
import time
import pygame
import Startmenu
# import Points
# import Music
import Tetrisblock
import control_feedback

# import Sound
# import control_feedback
clock = pygame.time.Clock()
leonardo = LED_Matrix_Maler.Painter()
tetrisblock = Tetrisblock.Tetrisblock
playground = Playground.Playground(10, 20)

objekt = RandomBlock.RandomBlock()
controller = control_feedback.Controller()
currentBlock = objekt.get_random_block()
nextBlock = objekt.get_random_block()

playground.put_block(currentBlock)

painter = Ws2812Painter.Ws2812Painter()
s = Startmenu(playground)

painter.paint(playground)
time.sleep(3)
playground.clear()
playground = Playground.Playground(10, 20)
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
    leonardo.draw(20, nextBlock)

    x, y = currentBlock.position

    for _ in range(4):
        buttons = controller.pressed()

        if "right" in buttons:
            x = x + 1
            print("right")

        if "left" in buttons:
            x = x - 1
            print("left")

        if "down" in buttons:
            y = y + 1
            print("down")

        playground.put_block(currentBlock)
        painter.paint(playground)
        playground.remove_block(currentBlock)
        clock.tick()

    if y == 15:
        currentBlock = nextBlock
        nextBlock = objekt.get_random_block()
    else:
        currentBlock.position = x, y + 1
