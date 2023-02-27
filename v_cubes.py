from v_display import display, pygame
from c_rectangle import Side
from e_colour import Colour
import json


def save():
    file = open('cubes.json', 'w+')
    data = {
        "char cube": char_cube
    }
    json.dump(data, file, indent = 4)


def load():
    file = open('cubes.json', 'r')
    data = json.load(file)
    return data["char cube"] if "char cube" in data else clean_char_cube


clean_char_cube = [[['b'] * 3] * 3,
                   [['r'] * 3] * 3,
                   [['g'] * 3] * 3,
                   [['o'] * 3] * 3,
                   [['w'] * 3] * 3,
                   [['y'] * 3] * 3]

char_cube = load()

graphics_cube = [Side(Colour.BLUE.value, 125, 200, 50),
                 Side(Colour.RED.value, 300, 200, 50),
                 Side(Colour.GREEN.value, 475, 200, 50),
                 Side(Colour.ORANGE.value, 650, 200, 50),
                 Side(Colour.WHITE.value, 300, 375, 50),
                 Side(Colour.YELLOW.value, 300, 25, 50)]

clean_graphics_cube = [Side(Colour.BLUE.value, 125, 200, 50),
                       Side(Colour.RED.value, 300, 200, 50),
                       Side(Colour.GREEN.value, 475, 200, 50),
                       Side(Colour.ORANGE.value, 650, 200, 50),
                       Side(Colour.WHITE.value, 300, 375, 50),
                       Side(Colour.YELLOW.value, 300, 25, 50)]


def draw():
    cube_to_graphics()
    for s in range(0, 6):
        # side
        for i in range(0, 3):
            for j in range(0, 3):
                graphics_cube[s].side[i][j].draw()

        x = graphics_cube[s].side[0][0].x
        y = graphics_cube[s].side[0][0].y
        width = graphics_cube[s].side[0][0].width

        # side's gridlines
        for line in range(0, 4):
            pygame.draw.rect(display, Colour.BLACK.value,
                             (x-2, ((y-2)+(line*width)), (3*width + 2), 2))
            pygame.draw.rect(display, Colour.BLACK.value,
                             (((x-2)+(line*width)), y-2, 2, (3*width + 2)))


def cube_to_graphics():
    for s in range(0, 6):
        for i in range(0, 3):
            for j in range(0, 3):
                graphics_cube[s].side[i][j].color = char_to_colour(
                    char_cube[s][i][j])
                clean_graphics_cube[s].side[i][j].color = char_to_colour(
                    clean_char_cube[s][i][j])


def graphics_to_cube():
    for s in range(0, 6):
        for i in range(0, 3):
            for j in range(0, 3):
                char_cube[s][i][j] = colour_to_char(
                    graphics_cube[s].side[i][j].color)


def char_to_colour(char):
    match(char):
        case 'b':
            return Colour.BLUE.value
        case 'r':
            return Colour.RED.value
        case 'g':
            return Colour.GREEN.value
        case 'o':
            return Colour.ORANGE.value
        case 'y':
            return Colour.YELLOW.value
        case 'w':
            return Colour.WHITE.value
        case _:
            return Colour.BLACK.value


def colour_to_char(colour):
    match(colour):
        case Colour.BLUE.value:
            return 'b'
        case Colour.RED.value:
            return 'r'
        case Colour.GREEN.value:
            return 'g'
        case Colour.ORANGE.value:
            return 'o'
        case Colour.YELLOW.value:
            return 'y'
        case Colour.WHITE.value:
            return 'w'
        case _:
            return ' '


def cube_to_string():
    cube_string = ""
    for row in range(3):
        for col in range(3):
            cube_string += char_cube[5][row][col]
    for side in range(4):
        for row in range(3):
            for col in range(3):
                cube_string += char_cube[side][row][col]
    for row in range(3):
        for col in range(3):
            cube_string += char_cube[4][row][col]
    return cube_string
