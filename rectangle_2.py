
from rectangle import Rectangle, Square, Circle

rect1 = Rectangle(3, 4)
rect2 = Rectangle(12, 5)
print(rect1.getArea(),
      rect2.getArea())

square_1 = Square(5)
square_2 = Square(10)
print(square_1.getAreaSquare(),
      square_2.getAreaSquare())

circle_1 = Circle(2)
circle_2 = Circle(1.2)
print(f"Площадь круга circle_1 равна: {circle_1.getCircleArea()}\n",
      f"Площадь круга circle_2 равна: {circle_2.getCircleArea()}\n")

figures = [rect1, rect2, square_1, square_2, circle_1, circle_2]

for figure in figures:
    if isinstance(figure, Square):
        print(figure.getAreaSquare())

    elif isinstance(figure, Circle):
        print(figure.getCircleArea())

    else:
        print(figure.getArea())



