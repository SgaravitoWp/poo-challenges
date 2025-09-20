
from poligons import Rectangle, Square
from poligons.primitives import Line, Point
from poligons import Method1, Method2, Method3

if __name__ == "__main__":
    rectangle = Rectangle(center=Point(0, 0), width=4, height=6)
    square = Square(center=Point(1, 1), width=4, height=4)

    print(rectangle.compute_area())
    print(rectangle.compute_perimeter())

    print(square.compute_area())
    print(square.compute_perimeter())

    print(rectangle.compute_interference_point(point = Point(7,7), method= Method1))
    print(rectangle.compute_interference_point(point = Point(7,7), method= Method2))
    print(rectangle.compute_interference_point(point = Point(7,7), method= Method3))

    print(square.compute_interference_point(point = Point(2,2), method= Method1))
    print(square.compute_interference_point(point = Point(2,2), method= Method2))
    print(square.compute_interference_point(point = Point(2,2), method= Method3))