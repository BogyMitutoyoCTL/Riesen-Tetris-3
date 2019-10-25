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


def get_block_after_action(current_block, action):
    future_block = current_block.clone()  # type: Tetrisblock.Tetrisblock
    if action == "right":
        future_block.moveright()
    if action == "left":
        future_block.moveleft()
    if action == "down":
        future_block.movedown()
    if action == "B":
        future_block.turnright()
    if action == "Y":
        future_block.turnleft()
    return future_block


def switch_blocks(next_block, points):
    points.new_block()
    return next_block, RandomBlock.RandomBlock().get_random_block()


def play_game(playground, clock, painter, leonardo, controller: Control_feedback.Controller, sound):
    objekt = RandomBlock.RandomBlock()
    current_block = objekt.get_random_block()
    next_block = objekt.get_random_block()
    points = Points.Points()
    sounds = Sound.Sound()
    walkman = Music.Music(0.3)
    walkman.start()
    playground.put_block(current_block)
    game_over = False
    in_pause = False
    action_counter = 0
    while not game_over:
        actions = controller.pressed()
        if in_pause is False and "Pause" in actions:
            in_pause = True
        else:
            if "Pause" in actions:
                in_pause = False

        if not in_pause:
            leonardo.draw(str(points.points), next_block)
            for action in actions:
                future_block = get_block_after_action(current_block, action)
                executable = not playground.collieds(future_block)
                if action == "down":
                    if executable:
                        current_block = future_block

                    else:
                        playground.put_block(current_block)
                        full_line_count = handle_full_lines(playground, points, sound)
                        if current_block.y + full_line_count < 0:
                            game_over = True
                            sounds.game_over()
                        else:
                            if current_block.y < 5:
                                sound.warning()
                            else:
                                sound.reached_limit()
                            current_block, next_block = switch_blocks(next_block, points)

                else:
                    if executable:
                        current_block = future_block
            draw(current_block, painter, playground)
            clock.tick((16.5 / 10000) * points.points + 3.5)

            action_counter += 1
            if action_counter == 4:
                controller.add_action("down")
                action_counter = 0
        else:
            leonardo.write_text("Pause...")
            pygame.time.delay(200)

    walkman.stop()

    game_over_screen(playground, leonardo, points, sounds, controller)


def draw(current_block, painter, playground):
    playground.put_block(current_block)
    painter.paint(playground)
    playground.remove_block(current_block)


def handle_full_lines(playground, points, sound: Sound.Sound):
    line_numbers = playground.fullrow()
    line_count = len(line_numbers)

    if line_count > 0:
        playground.delete_line(line_numbers)
        points.lines(line_count)
        sound.play_sound_for_lines(line_count)
    return line_count


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
