import Playground
import RandomBlock
import Ws2812Painter
import LED_Matrix_Maler
import time
import pygame
import Startmenu
import Points
import Music
import Tetrisblock
import Control_feedback

import Sound



def before_game(playground, painter, controller):
    s = Startmenu.Startmenu(playground)
    painter.paint(playground)
    while True:
        buttons = controller.pressed()
        if "Start" in buttons:
            print("Start")
            playground.clear()
            painter.paint(playground)
            break


def play_game(playground, clock, painter, leonardo, controller, sound):
    objekt = RandomBlock.RandomBlock()
    currentBlock = objekt.get_random_block()
    nextBlock = objekt.get_random_block()
    points = Points.Points()
    music = Music.Music
    playground.put_block(currentBlock)
    music
    while True:

        leonardo.draw(str(points.points), nextBlock)

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
            if "B" in buttons:
                currentBlock.turnright()

            if "Y" in buttons:
                currentBlock.turnleft()

            playground.put_block(currentBlock)
            painter.paint(playground)
            playground.remove_block(currentBlock)
            clock.tick(4)
            c = playground.fullrow()
            if len(c) > 0:
                playground.delete_line(c)
                points.lines(len(c))
                if len(c) == 1:
                    sound.complete_line1()
                if len(c) == 2:
                    sound.complete_line2()
                if len(c) == 3:
                    sound.complete_line3()
                if len(c) == 4:
                    sound.complete_line4()

        if y == 15:
            currentBlock = nextBlock
            nextBlock = objekt.get_random_block()

        else:
            currentBlock.position = x, y + 1


pygame.init()
clock = pygame.time.Clock()
leonardo = LED_Matrix_Maler.Painter()
tetrisblock = Tetrisblock.Tetrisblock
playground = Playground.Playground(10, 20)
controller = Control_feedback.Controller()
painter = Ws2812Painter.Ws2812Painter()
sound = Sound.Sound()
before_game(playground, painter, controller)
play_game(playground, clock, painter, leonardo, controller, sound)
