from src.perspective.perspective import Perspective
from src.position import Vector3
import curses

class LinearPerspective(Perspective):

    def __init__(self, vanishingPoint):
        self.vanishingPoint = vanishingPoint
        self.ratio = 100

    def getVanishingPoint(self):
        if self.vanishingPoint == "center":
            return Vector3(curses.COLS / 2, curses.LINES / 2)

    def apply(self, point, camera):
        visible = True

        vanishingPoint = self.getVanishingPoint()
        offsetPercentage = 1 / (exp(point.z / self.ratio))

        x = (point.x - vanishingPoint.x) * offsetPercentage + vanishingPoint.x + camera.position.x
        y = (point.y - vanishingPoint.y) * offsetPercentage + vanishingPoint.y + camera.position.y

        if point.z < camera.position.z:
            visible = False

        return [Vector3(x, y, point.z), visible]
