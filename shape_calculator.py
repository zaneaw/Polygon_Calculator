import math


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        area = self.height * self.width
        return area

    def get_perimeter(self):
        perimeter = 2 * self.width + 2 * self.height
        return perimeter

    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** 0.5
        return diagonal

    def get_picture(self):
        row = ""
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        for i in range(self.width):
            row += "*"
        row = row + "\n"
        row = row * self.height
        return row

    def get_amount_inside(self, shape):
        amount_inside = (self.width * self.height) / (
            shape.width * shape.height
        )
        amount_inside = math.floor(amount_inside)
        return amount_inside

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side
        self.side = side

    def set_side(self, side):
        self.width = side
        self.height = side
        self.side = side

    def set_width(self, side):
        self.side = side

    def set_height(self, side):
        self.side = side

    def __str__(self):
        return f"Square(side={self.side})"
