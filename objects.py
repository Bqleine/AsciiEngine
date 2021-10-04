from position import *
from math import sin

class Object:
    
    def tick(self, deltaTime, timePassed): pass
    def draw(self, screen): pass

class Text(Vector2, Object):
    
    def __init__(self, text, x, y):
        super().__init__(x, y)
        self.setText(text)
    
    def draw(self, screen):
        for i in range(len(self.text)): 
            screen[round(self.y)][round(self.x+i)] = self.text[i]
            
    def setText(self, text):
        self.text = str(text)
        
class Line(Object):
    
    def __init__(self, startPoint, endPoint):
        self.startPoint = startPoint
        self.endPoint = endPoint
        
    def tick(self, deltaTime, timePassed):
        #self.endPoint.setY(self.endPoint.getY() + (sin(timePassed) * 3))
        pass
    
    def draw(self, screen):
        dx = self.startPoint.distanceX(self.endPoint)
        dy = self.startPoint.distanceY(self.endPoint)
        
        if (abs(dx) > abs(dy)):
            pixels = int(dx)
        else:
            pixels = int(dy)
            
        if pixels == 0: return
        
        if dy > 0 or (dy == 0 and dx > 0):
            origin = self.startPoint
        else:
            origin = self.endPoint
                    
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
            position = Vector2(i * stepX + origin.getX(), i * stepY + origin.getY())

            screen[int(position.getY())][int(position.getX())] = character

class Parallelogram(Object):
    
    def __init__(self, A, B, C, D):
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        
    def draw(self, screen):
        lines = [
            Line(self.A, self.B),
            Line(self.B, self.C),
            Line(self.C, self.D),
            Line(self.D, self.A),
        ]
        
        for line in lines:
            line.draw(screen)
            
class Square(Object):
    
    def __init__(self, position, length):
        self.position = position
        self.length = length
    
    def draw(self, screen):
        
        A = self.position
        B = self.position.add(Vector2(self.length, 0))
        C = self.position.add(Vector2(self.length, self.length))
        D = self.position.add(Vector2(0, self.length))
                
        Parallelogram(A, B, C, D).draw(screen)
            
class Rectangle(Object):
    
    def __init__(self, startPoint, endPoint):
        self.startPoint = startPoint
        self.endPoint = endPoint
    
    def draw(self, screen):
        
        A = self.startPoint
        B = Vector2(self.endPoint.getX(), self.startPoint.getY())
        C = self.endPoint
        D = Vector2(self.startPoint.getX(), self.endPoint.getY())
        
        Parallelogram(A, B, C, D).draw(screen)