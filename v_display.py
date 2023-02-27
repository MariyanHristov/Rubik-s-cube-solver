import pygame
import json
from e_colour import Colour

pygame.init()
pygame.display.set_caption('Rubik\'s Cube Solver - Mariyan Hristov - 2023')
display = pygame.display.set_mode([1000, 700])
display.fill(Colour.BACKGROUND_COLOUR.value)
algortihm_box = pygame.Surface.subsurface(display, (100, 550), (900, 150))

def save():
    file = open('buttons.json', 'w+')
    data = {
        "solving": pc_solving,
        "scrambled": scrambled,
        "can_solve_yourself": can_solve_yourself,
        "can_press_solve_yourself": can_press_solve_yourself,
        "scrambled_path": scrambled_path,
        "manual_solve_path": manual_solve_path
    }
    json.dump(data, file, indent = 4)


def load(key):
    file = open('buttons.json', 'r')
    data = json.load(file)
    return data[key] if key in data else default[key]


default = {
    "solving": False,
    "scrambled": False,
    "can_solve_yourself": False,
    "can_press_solve_yourself": False,
    "scrambled_path": '',
    "manual_solve_path": ''
}

pc_solving = load("solving")
scrambled = load("scrambled")
scrambled_path = load("scrambled_path")
can_press_solve_yourself = load("can_press_solve_yourself")
can_solve_yourself = load("can_solve_yourself")
manual_solve_path = load("manual_solve_path")

def draw():
    import v_cubes
    import e_buttons
    if scrambled:
        display_text(display, Colour.BLACK.value, 100, 550,
                     20, 'Scrambled! Path: ' + scrambled_path)
    v_cubes.draw()
    if not pc_solving:
        e_buttons.draw()
    if can_solve_yourself:
        e_buttons.draw(True)
    pygame.display.update()


def display_text(display, color, x, y, size, str):
    font = pygame.font.SysFont('Times New Roman', size)

    # create a text suface object, on which text is drawn on it.
    text = font.render(str, True, color,  Colour.BACKGROUND_COLOUR.value)
    textRect = text.get_rect()

    textRect.topleft = (x, y)
    display.blit(text, textRect)
