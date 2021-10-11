from src.object import Object
from src._2d.text import Text
from src.position import Vector3


class LogsDisplay(Object):

    def __init__(self, position, height):
        self.position = position
        self.height = height

    def draw(self, window):
        length = len(window.logs)

        if length > self.height:
            height = self.height
            offset = length - self.height
        else:
            height = length
            offset = 0

        for i in range(height):
            Text(window.logs[offset + i], self.position.add(Vector3(0, height - i))).draw(window)
