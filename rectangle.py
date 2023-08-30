

class Rectangle:

    def __init__(self, a, b):
        self.a = a
        self.b = b
    def getArea(self):
        return self.a * self.b

class Square:
    def __init__(self, a):
        self.a = a
    def getAreaSquare(self):
        return self.a ** 2

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def getCircleArea(self):
        return 3.14 * (self.radius ** 2)

