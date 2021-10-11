from src.object import Object
from src._2d.text import Text
from src._2d.line import Line
from src.position import Vector3


class Cube(Object):

    def __init__(self, position, rotation, length, showPoints=False):
        self.length = length
        self.position = position
        self.rotation = rotation
        self.showPoints = showPoints

    def draw(self, window):
        length = self.length / 2

        A = self.position.add(Vector3(-length, -length, -length)).applyRotation(self.rotation, self.position)
        B = self.position.add(Vector3(length, -length, -length)).applyRotation(self.rotation, self.position)
        C = self.position.add(Vector3(length, length, -length)).applyRotation(self.rotation, self.position)
        D = self.position.add(Vector3(-length, length, -length)).applyRotation(self.rotation, self.position)
        E = self.position.add(Vector3(-length, -length, length)).applyRotation(self.rotation, self.position)
        F = self.position.add(Vector3(length, -length, length)).applyRotation(self.rotation, self.position)
        G = self.position.add(Vector3(length, length, length)).applyRotation(self.rotation, self.position)
        H = self.position.add(Vector3(-length, length, length)).applyRotation(self.rotation, self.position)

        lines = [
            Line(A, B),
            Line(D, C),
            Line(E, F),
            Line(H, G),

            Line(A, E),
            Line(D, H),
            Line(B, F),
            Line(C, G),

            Line(A, D),
            Line(B, C),
            Line(E, H),
            Line(F, G),
        ]

        if self.showPoints:
            lines.extend([
                Text("A", A),
                Text("B", B),
                Text("C", C),
                Text("D", D),
                Text("E", E),
                Text("F", F),
                Text("G", G),
                Text("H", H),
            ])

        for line in lines:
            line.draw(window)
