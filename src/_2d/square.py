from src.object import Object
from src._2d.parallelogram import Parallelogram
from src.position import Vector3


class Square(Object):

    def __init__(self, position, length):
        self.position = position
        self.length = length

    def draw(self, window):
        A = self.position
        B = self.position.add(Vector3(0, self.length))
        C = self.position.add(Vector3(self.length, self.length))
        D = self.position.add(Vector3(self.length, 0))

        Parallelogram(A, B, C, D).draw(window)
