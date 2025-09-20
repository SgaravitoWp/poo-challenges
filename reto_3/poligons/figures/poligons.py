from poligons.figures.methods import Method
from poligons.primitives import Point, Line, Edge

class Rectangle:
    def __init__(self, center: Point, width: float, height: float):
       
        self.edge = Edge(center, width, height)

    def compute_area(self):
        return self.edge.width * self.edge.height

    def compute_perimeter(self):
        return 2*(self.edge.width + self.edge.height)

    def compute_interference_point(self, point: Point, method: Method):
        return method().compute_interference_point(point, self.edge)
    
    def compute_interference_line(self, line: Line, method: Method):
        return method().compute_interference_line(line, self.edge)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.edge.width}, {self.edge.height}, {self.edge.center})"
    
    def __str__(self):
        return f"{self.__class__.__name__}({self.edge.width}, {self.edge.height}, {self.edge.center})"

class Square(Rectangle):

    def __init__(self, center: Point, width: float, height: float):
        if width != height:
            raise ValueError("Width and height must be equal for a square.")
        super().__init__(center, width, height)

