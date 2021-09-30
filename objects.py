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
        self.endPoint.setX(self.endPoint.getX() + sin(0.1 * timePassed) * deltaTime)
        self.endPoint.setY(self.endPoint.getY() + sin(0.3 * timePassed) * deltaTime)
        
    def draw(self, screen):
        distance = self.startPoint.distance(self.endPoint)
        
        stepX = (self.startPoint.getX() + self.endPoint.getX()) / distance
        stepY = (self.startPoint.getY() + self.endPoint.getY()) / distance
        
        if stepX == 0:
            direction = "|"
        elif stepY == 0:
            direction = "-"
        elif ((stepX > 0 and stepY) > 0 or (stepX < 0 and stepY < 0)):
            direction = "\\"
        else:
            direction = "/"
            
        for i in range(round(distance)):
            screen[int(i*stepY)][int(i*stepX)] = direction