import random

import v_display as display
from a_movements import Movement

from e_colour import Colour
import collections.abc
collections.Iterable = collections.abc.Iterable
collections.Mapping = collections.abc.Mapping
collections.MutableSet = collections.abc.MutableSet
collections.MutableMapping = collections.abc.MutableMapping
from rubik_solver import utils
import pygame


def solve():
    display.display_text(display.display, Colour.BLACK.value, 100, 600, 20, 'Solving, please wait...')
    pygame.display.update()

    # convert cube to string
    from v_cubes import cube_to_string
    cube_string = cube_to_string()

    # solve cube
    solve_steps = utils.solve(cube_string, 'Kociemba') if not is_cube_solved() else []
    solution_text = 'Solved! Solution: ' + ''.join(str(step) for step in solve_steps)
    display.display_text(display.display, Colour.BLACK.value, 100, 650, 20, solution_text)
    pygame.display.update()
    execute_solution_steps(solve_steps)

    display.pc_solving = False
    display.scrambled = False


def scramble():
    display.scrambled = True
    scrambled_combination = " "
    shuffles = random.randint(21, 23)
    display.algortihm_box.fill(Colour.BACKGROUND_COLOUR.value)
    for _ in range(0, shuffles):
        turn = random.randint(0, 11)
        match(turn):
            case 0:
                Movement.type("up")
                scrambled_combination += "2" if scrambled_combination[-1] == "U" else "U"
            case 1:
                Movement.type("up prime")
                scrambled_combination = scrambled_combination[:-1] + "2" if scrambled_combination[-2:] == "U\'" else scrambled_combination + "U\'"
            case 2:
                Movement.type("down")
                scrambled_combination +="2" if scrambled_combination[-1] == "D" else "D"
            case 3:
                Movement.type("down prime")
                scrambled_combination = scrambled_combination[:-1] + "2" if scrambled_combination[-2:] == "D\'" else scrambled_combination + "D\'"
            case 4:
                Movement.type("left")
                scrambled_combination +="2" if scrambled_combination[- 1] == "L" else "L"
            case 5:
                Movement.type("left prime")
                scrambled_combination = scrambled_combination[:-1] + "2" if scrambled_combination[-2:] == "L\'" else scrambled_combination + "L\'"
            case 6:
                Movement.type("right")
                scrambled_combination += "2" if scrambled_combination[-1] == "R"  else "R"
            case 7:
                Movement.type("right prime")
                scrambled_combination = scrambled_combination[:-1] + "2" if scrambled_combination[-2:] == "R\'" else scrambled_combination + "R\'"
            case 8:
                Movement.type("back")
                scrambled_combination += "2" if scrambled_combination[- 1] == "B" else "B"
            case 9:
                Movement.type("back prime")
                scrambled_combination = scrambled_combination[:-1] + "2" if scrambled_combination[-2:] == "B\'" else scrambled_combination + "B\'"
            case 10:
                Movement.type("front")
                scrambled_combination +="2" if scrambled_combination[-1] == "F"  else "F"
            case 11:
                Movement.type("front prime")
                scrambled_combination = scrambled_combination[:-1] + "2" if scrambled_combination[-2:] == "B\'" else scrambled_combination + "F\'"
        display.draw()                       
    text_to_display = 'Scrambled! Path: ' + scrambled_combination
    display.scrambled_path = scrambled_combination
    display.display_text(display.display, Colour.BLACK.value, 100, 550, 20, text_to_display)
    pygame.display.update()


def execute_solution_steps(solve_steps):  
    for step in solve_steps:
        match(step):
            case 'U':
                Movement.type("up")
            case 'U2':
                Movement.type("up")
                Movement.type("up")
            case 'U\'':
                Movement.type("up prime")
            case 'D':
                Movement.type("down")
            case 'D2':
                Movement.type("down")
                Movement.type("down")
            case 'D\'':
                Movement.type("down prime")
            case 'L':
                Movement.type("left")
            case 'L2':
                Movement.type("left")
                Movement.type("left")
            case 'L\'':
                Movement.type("left prime")
            case 'R':
                Movement.type("right")
            case 'R2':
                Movement.type("right")
                Movement.type("right")
            case 'R\'':
                Movement.type("right prime")
            case 'F':
                Movement.type("front")
            case 'F2':
                Movement.type("front")
                Movement.type("front")
            case 'F\'':
                Movement.type("front prime")
            case 'B':
                Movement.type("back")
            case 'B2':
                Movement.type("back")
                Movement.type("back")
            case 'B\'':
                Movement.type("back prime")
        display.draw()


def is_cube_solved():
    from v_cubes import char_cube, clean_char_cube
    if all(char_cube[side] == clean_char_cube[side] for side in range(0, 6)):
        display.scrambled = False
        display.pc_solving = False
        display.can_solve_yourself = False
        display.can_press_solve_yourself = True
        return True
    else:
        return False
