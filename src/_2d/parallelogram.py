from src.object import Object
from src._2d.line import Line


class Parallelogram(Object):

    def __init__(self, A, B, C, D):
        self.A = A
        self.B = B
        self.C = C
        self.D = D

    def draw(self, window):
        # Sides go first
        lines = [
            Line(self.B, self.C),
            Line(self.D, self.A),
            Line(self.A, self.B),
            Line(self.C, self.D),
        ]

        for line in lines:
            line.draw(window)
