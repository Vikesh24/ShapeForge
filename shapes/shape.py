# ./shapes/shape.py

import turtle
from abc import ABC, abstractmethod

class Shape(ABC):
    """ Abstract base class for shapes."""
    def __init__(self, color='black', size=100, ):
        self.color = color
        self.size = size
        self.t = turtle.Turtle()
        self.t.speed(3)

    @abstractmethod
    def draw(self):
        """Abstract base class to draw a shape"""
        pass