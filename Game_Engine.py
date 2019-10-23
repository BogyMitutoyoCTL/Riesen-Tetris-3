import Playground
import RandomBlock
import Ws2812Painter
import LED_Matrix_Maler
import time
import pygame
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
    playground.remove_block(currentBlock)
    x, y = currentBlock.position

    if y == 15:
        currentBlock = nextBlock
        y = 0
        nextBlock = objekt.get_random_block()
    for _ in range(4):
        buttons = controller.pressed()
        if "right" in buttons:
            x = x + 1
        if "left" in buttons:
            x = x - 1
        clock.tick(4)

    currentBlock.position = x, y + 1
    playground.put_block(currentBlock)

    painter.paint(playground)
