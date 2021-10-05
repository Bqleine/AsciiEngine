from position import *
from math import sin, floor

class Object:
    
    def tick(self, deltaTime, timePassed): pass
    def draw(self, screen, camera): pass

class Text(Object):
    
    def __init__(self, text, x, y):
        self.position = Vector3(x, y)
        self.setText(text)
    
    def draw(self, screen, camera):
        for i in range(len(self.text)): 
            screen[round(self.position.y)][round(self.position.x+i)] = self.text[i]
            
    def setText(self, text):
        self.text = str(text)
        
class Line(Object):
    
    def __init__(self, startPoint, endPoint):
        self.startPoint = startPoint
        self.endPoint = endPoint

    def tick(self, deltaTime, timePassed):
        self.endPoint = self.endPoint.add(Vector3(0, 0, 1*deltaTime))
        self.startPoint = self.startPoint.add(Vector3(0, 0, 1*deltaTime))
        pass
    
    def draw(self, screen, camera):
        startPoint = self.startPoint.applyPerspective(camera)
        endPoint = self.endPoint.applyPerspective(camera)

        if not (startPoint[1] or endPoint[1]):
            return

        startPoint = startPoint[0]
        endPoint = endPoint[0]

        dx = startPoint.distanceX(endPoint)
        dy = startPoint.distanceY(endPoint)
        
        if (abs(dx) > abs(dy)):
            pixels = round(dx)
        else:
            pixels = round(dy)
            
        if pixels == 0: return
        
        if dy > 0 or (dy == 0 and dx > 0):
            origin = startPoint
        else:
            origin = endPoint

        stepX = dx / pixels
        stepY = dy / pixels
        
        if stepY == 0:
            character = "-"
        elif stepX == 0:
            character = "|"
        elif stepX > 0:
            character = "\\"
        else:
            character = "/"
        
        for i in range(abs(pixels)):
            position = Vector3(i * stepX + origin.x, i * stepY + origin.y)
            screen[floor(position.y)][floor(position.x)] = character

class Parallelogram(Object):
    
    def __init__(self, A, B, C, D):
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        
    def draw(self, screen, camera):
        
        # Sides go first so it overrides prettier
        lines = [
            Line(self.B, self.C),
            Line(self.D, self.A),
            Line(self.A, self.B),
            Line(self.C, self.D),
        ]
        
        for line in lines:
            line.draw(screen, camera)
            
class Square(Object):
    
    def __init__(self, position, length):
        self.position = position
        self.length = length
    
    def draw(self, screen, camera):
        
        A = self.position
        B = self.position.add(Vector3(self.length, 0))
        C = self.position.add(Vector3(self.length, self.length))
        D = self.position.add(Vector3(0, self.length))

        Parallelogram(A, B, C, D).draw(screen, camera)
            
class Rectangle(Object):
    
    def __init__(self, startPoint, endPoint):
        self.startPoint = startPoint
        self.endPoint = endPoint
    
    def draw(self, screen, camera):
        
        A = self.startPoint
        B = Vector3(self.endPoint.x, self.startPoint.y)
        C = self.endPoint
        D = Vector3(self.startPoint.x, self.endPoint.y)
        
        Parallelogram(A, B, C, D).draw(screen, camera)