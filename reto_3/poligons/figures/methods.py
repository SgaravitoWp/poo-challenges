from __future__ import annotations
from abc import ABC, abstractmethod
from poligons.primitives import Point, Line, Edge


class Method(ABC):
    def compute_area(self, edge: Edge):
        return edge.width * edge.height
    
    def compute_perimeter(self, width: float, height: float):
        return 2 * (width + height)
        
    @abstractmethod
    def compute_interference_point(self):
        pass 

    @abstractmethod
    def compute_interference_line(self):
        pass

class Method1(Method):
    def compute_interference_line(self, line):
        pass
    def compute_interference_point(self, point: Point, edge:Edge):
        botton_left = edge.bottom_left
        top_right = Point(edge.top_right.x, edge.top_right.y)
        if ((botton_left.x <= point.x <= top_right.x)
             and (botton_left.y <= point.y <= top_right.y)):
            return True
        return False

class Method2(Method):
    def compute_interference_line(self, line):
        pass
    def compute_interference_point(self, point:Point, edge:Edge):
        center = edge.center
        botton_left = Point(center.x - edge.width/2, center.y - edge.height/2)
        top_right = Point(center.x + edge.width/2, center.y + edge.height/2)
        if ((botton_left.x <= point.x <= top_right.x)
             and (botton_left.y <= point.y <= top_right.y)):
            return True
        return False

class Method3(Method):
    def compute_interference_line(self, line):
        pass
    def compute_interference_point(self, point:Point, edge:Edge):
        botton_left = edge.bottom_left
        top_right = edge.top_right 
        if ((botton_left.x <= point.x <= top_right.x)
             and (botton_left.y <= point.y <= top_right.y)):
            return True
        return False


