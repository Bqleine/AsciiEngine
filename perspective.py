from position import Vector3
from os import get_terminal_size

class Perspective:
    pass

class LinearPerspective(Perspective):

    def __init__(self, vanishingPoint):
        self.vanishingPoint = vanishingPoint
        self.ratio = 100

    def getVanishingPoint(self):
        if self.vanishingPoint == "center":
            terminalSize = get_terminal_size()
            return Vector3(terminalSize.columns / 2, terminalSize.lines / 2)