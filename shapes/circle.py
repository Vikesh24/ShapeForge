# ./shapes/circle.py

from .shape import Shape

class Circle(Shape):
    """Concrete class for Circle"""
    def __init__(self, color='black', size=100):
        super().__init__(color, size)

    def draw(self):
        self.t.color(self.color)
        self.t.penup()
        self.t.goto(0, -self.size)
        self.t.pendown()
        self.t.circle(self.size)
