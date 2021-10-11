from src.object import Object
from src.position import Vector3


class Line(Object):

    def __init__(self, startPoint, endPoint, showPoints=False):
        self.startPoint = startPoint
        self.endPoint = endPoint
        self.showPoints = showPoints

    def draw(self, window):
        startPoint = self.startPoint.applyPerspective(window.camera)
        endPoint = self.endPoint.applyPerspective(window.camera)

        if not (startPoint[1] or endPoint[1]):
            return

        startPoint = startPoint[0]
        endPoint = endPoint[0]

        # Bresenham's line algorithm
        if abs(endPoint.y - startPoint.y) < abs(endPoint.x - startPoint.x):
            if startPoint.x > endPoint.x:
                self.plotLineLow(endPoint, startPoint, window)
            else:
                self.plotLineLow(startPoint, endPoint, window)
        else:
            if startPoint.y > endPoint.y:
                self.plotLineHigh(endPoint, startPoint, window)
            else:
                self.plotLineHigh(startPoint, endPoint, window)

        if self.showPoints:
            window.drawCharacter("A", startPoint)
            window.drawCharacter("B", endPoint)

    def plotLineHigh(self, startPoint, endPoint, window):
        dx = round(startPoint.distanceX(endPoint))
        dy = round(startPoint.distanceY(endPoint))

        if dx < 0:
            stepX = -1
            dx = -dx
            character = "/"
        else:
            stepX = 1
            if dx == 0:
                character = "|"
            else:
                character = "\\"

        distance = (2 * dx) - dy

        x = startPoint.x

        for y in range(round(startPoint.y), round(endPoint.y)):
            window.drawCharacter(character, Vector3(x, y))
            if distance > 0:
                x += stepX
                distance += 2 * (dx - dy)
            else:
                distance += 2 * dx

    def plotLineLow(self, startPoint, endPoint, window):
        dx = round(startPoint.distanceX(endPoint))
        dy = round(startPoint.distanceY(endPoint))

        if dy < 0:
            stepY = -1
            dy = -dy
            character = "/"
        else:
            stepY = 1
            if dy == 0:
                character = "-"
            else:
                character = "\\"

        distance = (2 * dy) - dx

        y = startPoint.y

        for x in range(round(startPoint.x), round(endPoint.x)):
            window.drawCharacter(character, Vector3(x, y))
            if distance > 0:
                y += stepY
                distance += 2 * (dy - dx)
            else:
                distance += 2 * dy
