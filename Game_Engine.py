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
from Highscore import Highscore


def start_screen(playground, painter, controller):
    s = Startmenu.Startmenu(playground)
    painter.paint(playground)
    while True:
        buttons = controller.pressed()
        if "Start" in buttons:
            playground.clear()
            painter.paint(playground)
            break


def game_over_screen(playground, leonardo, points, sounds, controller):
    h = Highscore("highscore.txt", leonardo, sounds)
    h.handle_highscore("name", points.points)

    while True:
        buttons = controller.pressed()
        if "Start" in buttons:
            playground.clear()
            painter.paint(playground)
            break


def play_game(playground, clock, painter, leonardo, controller, sound):
    objekt = RandomBlock.RandomBlock()
    current_block = objekt.get_random_block()
    next_block = objekt.get_random_block()
    points = Points.Points()
    sounds = Sound.Sound()
    walkman = Music.Music(0.3)
    walkman.start()
    playground.put_block(current_block)
    game_over = False
    while not game_over:
        leonardo.draw(str(points.points), next_block)

        for _ in range(4):
            future_block, moved_down = control_request(controller, current_block)
            if playground.collieds(future_block):
                game_over = handle_collision(current_block, playground, points, sound, moved_down)
                if moved_down:
                    current_block = next_block
                    next_block = objekt.get_random_block()
            else:
                current_block.position = future_block.position
                current_block.orientation = future_block.orientation
            draw(current_block, painter, playground)
            clock.tick((16.5 / 10000) * points.points + 3.5)

        try_down = FakeController()
        future_block, moved_down = control_request(try_down, current_block)
        if playground.collieds(future_block):
            game_over = handle_collision(current_block, playground, points, sound, moved_down)
            if moved_down:
                current_block = next_block
                next_block = objekt.get_random_block()
        else:
            current_block.position = future_block.position
            current_block.orientation = future_block.orientation
            handle_full_lines(playground, points, sounds)

    walkman.stop()

    game_over_screen(playground, leonardo, points, sounds, controller)


def handle_collision(currentBlock, playground, points, sound, moved_down):
    handle_full_lines(playground, points, sound)
    if currentBlock.position[1] < 0:
        sound.game_over()
        return True
    else:
        if moved_down:
            playground.put_block(currentBlock)

        if currentBlock.position[1] < 5:
            sound.warning()
        else:
            sound.reached_limit()

    return False


def draw(current_block, painter, playground):
    playground.put_block(current_block)
    painter.paint(playground)
    playground.remove_block(current_block)


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


def control_request(controller, current_block):
    buttons = controller.pressed()
    future_orientation = current_block.orientation
    future_x, future_y = current_block.position
    block_moved_down = False
    if "right" in buttons:
        future_x = future_x + 1
        print("right")
    if "left" in buttons:
        future_x = future_x - 1
        print("left")
    if "down" in buttons:
        future_y = future_y + 1
        block_moved_down = True
    if "B" in buttons:
        current_block.turnright()
        future_orientation = current_block.orientation
        current_block.turnleft()
    if "Y" in buttons:
        current_block.turnleft()
        future_orientation = current_block.orientation
        current_block.turnright()

    future_block = current_block.clone()
    future_block.position = future_x, future_y
    future_block.orientation = future_orientation
    return future_block, block_moved_down


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

while True:
    start_screen(playground, painter, controller)
    play_game(playground, clock, painter, leonardo, controller, sound)
