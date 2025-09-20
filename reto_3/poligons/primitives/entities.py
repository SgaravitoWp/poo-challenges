class Point:
    definition: str = "Entidad geometrica abstracta que representa una ubicación en un espacio."
    def __init__(self, x: float=0, y: float=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
class Line:
    pass

class Edge:
    def __init__(self, center: Point, width: float, height: float):
        self.center = center
        self.width = width
        self.height = height
        self.define_edges()
        
    def define_edges(self):
        self.bottom_left = Point(self.center.x - self.width / 2, self.center.y - self.height / 2)
        self.top_right = Point(self.center.x + self.width / 2, self.center.y + self.height / 2)
        self.bottom_right = Point(self.top_right.x, self.bottom_left.y)
        self.top_left = Point(self.bottom_left.x, self.top_right.y)