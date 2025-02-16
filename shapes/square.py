# ./shapes/square.py

from .shape import Shape

class Square(Shape):
    """Concrete class for Circle"""
    def __init__(self, color='black', size=100):
        super().__init__(color, size)

    def draw(self):
        self.t.color(self.color)
        self.t.penup()
        self.t.goto(-self.size/2, self.size/2)
        self.t.pendown()
        for _ in range(4):
            self.t.forward(self.size)
            self.t.right(90)