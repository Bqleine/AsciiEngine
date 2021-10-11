from src.object import Object
from src.position import Vector3
from src._2d.parallelogram import Parallelogram


class Rectangle(Object):

    def __init__(self, startPoint, endPoint):
        self.startPoint = startPoint
        self.endPoint = endPoint

    def draw(self, window):
        A = self.startPoint
        B = Vector3(self.endPoint.x, self.startPoint.y)
        C = self.endPoint
        D = Vector3(self.startPoint.x, self.endPoint.y)

        Parallelogram(A, B, C, D).draw(window)
