class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Cube(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def area(self):
        return self.length * self.width * self.height

cube = Cube(3, 3, 3)    
print(cube.area())
