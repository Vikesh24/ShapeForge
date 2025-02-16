# ./shapes/triangle.py

from .shape import Shape

class Triangle(Shape):
    """Concrete class for Circle"""
    def __init__(self, color='black', size=100):
        super().__init__(color, size)

    def draw(self):
        self.t.color(self.color)
        self.t.penup()
        self.t.goto(-self.size/2, self.size/2)
        self.t.pendown()
        for _ in range(3):
            self.t.forward(self.size)
            self.t.right(60)