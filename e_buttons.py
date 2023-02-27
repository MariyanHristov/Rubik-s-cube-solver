from c_rectangle import Button
from enum import Enum


class MovementButtons(Enum):
    UP_BUTTON = Button(650, 400, 'U')
    UP_PRIME_BUTTON = Button(700, 400, 'U\'')
    FRONT_BUTTON = Button(650, 450, 'F')
    FRONT_PRIME_BUTTON = Button(700, 450, 'F\'')
    DOWN_BUTTON = Button(650, 500, 'D')
    DOWN_PRIME_BUTTON = Button(700, 500, 'D\'')
    LEFT_BUTTON = Button(550, 450, 'L')
    LEFT_PRIME_BUTTON = Button(600, 450, 'L\'')
    RIGHT_BUTTON = Button(750, 450, 'R')
    RIGHT_PRIME_BUTTON = Button(800, 450, 'R\'')
    BACK_BUTTON = Button(850, 450, 'B')
    BACK_PRIME_BUTTON = Button(900, 450, 'B\'')


class AlgorithmButtons(Enum):
    START_BUTTON = Button(825, 200, 'PC Solve', length=150)
    SCRAMBLE_BUTTON = Button(825, 320, 'Scramble', length=150)
    MANUAL_SOLVE_BUTTON = Button(825, 260, 'Solve yourself', length=150)
    SHOW_PATH_BUTTON = Button(750, 500, 'Show your solution so far', length=225)


def draw(show_movement=False, show_algorithm=True):
    if show_movement:
        for button in MovementButtons:
            button.value.draw()
    if show_algorithm:
        for button in AlgorithmButtons:
            button.value.draw()
