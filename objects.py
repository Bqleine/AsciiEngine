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
        
        if dy > 0:
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
