import Playground
import RandomBlock
import Ws2812Painter
import LED_Matrix_Maler
import pygame
import Startmenu
import Points
import Music
import Tetrisblock
import Control_feedback
import Sound
from Control_feedback import FakeController


def before_game(playground, painter, controller):
    s = Startmenu.Startmenu(playground)
    painter.paint(playground)
    while True:
        buttons = controller.pressed()
        if "Start" in buttons:
            playground.clear()
            painter.paint(playground)
            break


def play_game(playground, clock, painter, leonardo, controller, sound):
    objekt = RandomBlock.RandomBlock()
    currentBlock = objekt.get_random_block()
    nextBlock = objekt.get_random_block()
    points = Points.Points()
    Music.Music(0.3)
    playground.put_block(currentBlock)
    while True:
        leonardo.draw(str(points.points), nextBlock)

        for _ in range(4):
            future_block = control_request(controller, currentBlock)
            if playground.collieds(future_block):
                currentBlock, nextBlock = handle_collision(currentBlock, nextBlock, objekt, playground, points, sound)
            else:
                currentBlock.position = future_block.position
                currentBlock.orientation = future_block.orientation
            draw(currentBlock, painter, playground)
            clock.tick(points.points / 100 + 2)

        tryDown = FakeController()
        future_block = control_request(tryDown, currentBlock)
        if playground.collieds(future_block):
            currentBlock, nextBlock = handle_collision(currentBlock, nextBlock, objekt, playground, points, sound)
        else:
            currentBlock.position = future_block.position
            currentBlock.orientation = future_block.orientation


def handle_collision(currentBlock, nextBlock, objekt, playground, points, sound):
    handle_full_lines(playground, points, sound)
    if currentBlock.position[1] < 0:
        sound.game_over()
    else:
        playground.put_block(currentBlock)

        if currentBlock.position[1] < 5:
            sound.warning()
        else:
            sound.reached_limit()

        currentBlock = nextBlock
        nextBlock = objekt.get_random_block()

    return currentBlock, nextBlock


def draw(currentBlock, painter, playground):
    playground.put_block(currentBlock)
    painter.paint(playground)
    playground.remove_block(currentBlock)


def handle_full_lines(playground, points, sound):
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


def control_request(controller, currentBlock):
    buttons = controller.pressed()
    future_orientation = currentBlock.orientation
    future_x, future_y = currentBlock.position
    if "right" in buttons:
        future_x = future_x + 1
        print("right")
    if "left" in buttons:
        future_x = future_x - 1
        print("left")
    if "down" in buttons:
        future_y = future_y + 1
        print("down")
    if "B" in buttons:
        currentBlock.turnright()
        future_orientation = currentBlock.orientation
        currentBlock.turnleft()
    if "Y" in buttons:
        currentBlock.turnleft()
        future_orientation = currentBlock.orientation
        currentBlock.turnright()

    future_block = currentBlock.clone()
    future_block.position = future_x, future_y
    future_block.orientation = future_orientation
    return future_block


pygame.init()
background_colour = (255, 255, 255)
(width, height) = (300, 200)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tutorial 1')
screen.fill(background_colour)
pygame.display.flip()

clock = pygame.time.Clock()
leonardo = LED_Matrix_Maler.Painter()
tetrisblock = Tetrisblock.Tetrisblock
playground = Playground.Playground(10, 20)
controller = Control_feedback.Controller()
painter = Ws2812Painter.Ws2812Painter()
sound = Sound.Sound()

before_game(playground, painter, controller)
play_game(playground, clock, painter, leonardo, controller, sound)
