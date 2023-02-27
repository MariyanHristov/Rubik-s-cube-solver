import pygame
import v_display as display
from e_colour import Colour


class Rectangle:
    def __init__(self, surface, color, x, y, length, width):
        self.surface = surface
        self.color = color
        self.x = x
        self.y = y
        self.length = length
        self.width = width

    def draw(self):
        pygame.draw.rect(self.surface, self.color,
                         (self.x, self.y, self.length, self.width))

    # checks if the current rectangle is inside the rectangle in parameter
    def intersects(self, rect1):
        x1 = rect1.x
        y1 = rect1.y
        length = rect1.length
        width = rect1.width

        return x1 < self.x < x1 + length and y1 < self.y < y1 + width

    def display_text(self, surface, color, x, y, size, str):

        font = pygame.font.SysFont('Times New Roman', size)

        # create a text suface object, on which the text will be drawn.
        text = font.render(str, True, color)
        textRect = text.get_rect()

        # set the center of the rectangular object.
        textRect.center = (x, y)
        surface.blit(text, textRect)


class Square(Rectangle):
    def __init__(self, surface, color, x, y, width):
        self.surface = surface
        self.color = color
        self.x = x
        self.y = y
        self.length = width
        self.width = width


class Side(Square):
    # generating 9 squares for 1 side. x and y is position of top left corner
    def __init__(self, color, x, y, width):
        self.side = [[Square(display.display, color, x + width * j, y + width * i, width)
                      for j in range(0, 3)] for i in range(0, 3)]


class Button(Rectangle):
    def __init__(self, x, y, text, bg_color=Colour.BROWN.value, surface=display.display, length=30, width=30, text_color=Colour.WHITE.value, text_size=20):
        self.surface = surface
        self.color = bg_color
        self.x = x
        self.y = y
        self.length = length
        self.width = width
        self.text = text
        self.text_color = text_color
        self.text_size = text_size

    def draw(self):
        pygame.draw.rect(self.surface, self.color,
                         (self.x, self.y, self.length, self.width))
        self.display_text(self.surface, self.text_color, self.x +
                          self.length/2, self.y + self.width/2, self.text_size, self.text)
