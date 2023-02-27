import pygame
import sys

import a_solver as solver
import v_display as display
import v_cubes as cubes

from tkinter import *
from tkinter import messagebox
from c_rectangle import Rectangle
from e_colour import Colour
from e_buttons import MovementButtons, AlgorithmButtons, draw
from a_movements import Movement


def quit():
    cubes.save()
    display.save()
    pygame.quit()
    sys.exit()


def execute_button_action(mouse: Rectangle):
    if not display.scrambled:
        if mouse.intersects(AlgorithmButtons.SCRAMBLE_BUTTON.value):
            solver.scramble()
    if display.scrambled:
        if mouse.intersects(AlgorithmButtons.MANUAL_SOLVE_BUTTON.value):
            display.can_solve_yourself = True
            draw(show_movement=True)
        elif mouse.intersects(AlgorithmButtons.START_BUTTON.value):
            question = messagebox.askquestion(
                "Finalize", "Are you sure that you don't want to try to solve it yourself ?!")
            if (question == 'yes'):
                solver.solve()
            display.manual_solve_path = ""
    if display.can_solve_yourself:
        movement_button_intersected = None
        if mouse.intersects(MovementButtons.UP_BUTTON.value):
            Movement.type("up")
            display.manual_solve_path += "U"
            movement_button_intersected = True
        elif mouse.intersects(MovementButtons.UP_PRIME_BUTTON.value):
            Movement.type("up prime")
            display.manual_solve_path += "U\'"
            movement_button_intersected = True
        elif mouse.intersects(MovementButtons.FRONT_BUTTON.value):
            Movement.type("front")
            display.manual_solve_path += "F"
            movement_button_intersected = True
        elif mouse.intersects(MovementButtons.FRONT_PRIME_BUTTON.value):
            Movement.type("front prime")
            display.manual_solve_path += "F\'"
            movement_button_intersected = True
        elif mouse.intersects(MovementButtons.DOWN_BUTTON.value):
            Movement.type("down")
            display.manual_solve_path += "D"
            movement_button_intersected = True
        elif mouse.intersects(MovementButtons.DOWN_PRIME_BUTTON.value):
            Movement.type("down prime")
            display.manual_solve_path += "D\'"
            movement_button_intersected = True
        elif mouse.intersects(MovementButtons.LEFT_BUTTON.value):
            Movement.type("left")
            display.manual_solve_path += "L"
            movement_button_intersected = True
        elif mouse.intersects(MovementButtons.LEFT_PRIME_BUTTON.value):
            Movement.type("left prime")
            display.manual_solve_path += "L\'"
            movement_button_intersected = True
        elif mouse.intersects(MovementButtons.RIGHT_BUTTON.value):
            Movement.type("right")
            display.manual_solve_path += "R"
            movement_button_intersected = True
        elif mouse.intersects(MovementButtons.RIGHT_PRIME_BUTTON.value):
            Movement.type("right prime")
            display.manual_solve_path += "R\'"
            movement_button_intersected = True
        elif mouse.intersects(MovementButtons.BACK_BUTTON.value):
            Movement.type("back")
            display.manual_solve_path += "B"
            movement_button_intersected = True
        elif mouse.intersects(MovementButtons.BACK_PRIME_BUTTON.value):
            Movement.type("back prime")
            display.manual_solve_path += "B\'"
            movement_button_intersected = True
        elif mouse.intersects(AlgorithmButtons.SHOW_PATH_BUTTON.value):
            movement_button_intersected = False
            messagebox.showinfo("Current state of solution",
                                "Your solution so far : " + str(display.manual_solve_path))
        if solver.is_cube_solved() and movement_button_intersected:
            display.draw()
            messagebox.showinfo(
                "Congratulations!", "You just solved the cube! \n\n Your solution : " + str(display.manual_solve_path))
            display.manual_solve_path = ""


def play():
    while True:
        for event in pygame.event.get():
            if not display.pc_solving:
                match(event.type):
                    case pygame.QUIT:
                        quit()
                    case pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        mouse = Rectangle(
                            display.display, Colour.BLACK, mouse_x, mouse_y, 1, 1)
                        execute_button_action(mouse)
        display.draw()

if __name__ == "__main__":
    play()
