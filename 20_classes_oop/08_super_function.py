class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):

    def __init__(self, *, length, width):
        super().__init__(length, width)

    def area(self):
        return  self.length * self.width

class Cube(Rectangle):

    def __init__(self, *, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length * self.width * self.height

square = Square(length=3, width=3)
cube = Cube(length=3, width=3, height=3)

print(square.area())
print(cube.volume())