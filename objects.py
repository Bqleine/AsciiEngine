from position import *
from math import sin, floor, ceil

class Object:
    
    def tick(self, deltaTime, timePassed): pass
    def draw(self, window): pass

class Text(Object):
    
    def __init__(self, text, position):
        self.position = position
        self.text = text
    
    def draw(self, window):
        for i in range(len(self.text)):
            window.drawCharacter(self.text[i], self.position.applyPerspective(window.camera)[0].add(Vector3(i, 0)))

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
        dx = startPoint.distanceX(endPoint)
        dy = startPoint.distanceY(endPoint)

        if dx < 0:
            stepX = -1
            dx = -dx
            character = "/"
        else:
            stepX = 1
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
        dx = startPoint.distanceX(endPoint)
        dy = startPoint.distanceY(endPoint)

        if dy < 0:
            stepY = -1
            dy = -dy
            character = "/"
        else:
            stepY = 1
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

class Parallelogram(Object):
    
    def __init__(self, A, B, C, D):
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        
    def draw(self, window):
        
        # Sides go first so it overrides prettier
        lines = [
            Line(self.B, self.C),
            Line(self.D, self.A),
            Line(self.A, self.B),
            Line(self.C, self.D),
        ]
        
        for line in lines:
            line.draw(window)
            
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