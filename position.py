from math import sqrt

class Vector2:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def setX(self, x):
        self.x = x
        
    def setY(self, y):
        self.y = y
    
    # sqrt((x2-x1)^2 + (y2 - y1)^2)
    def distance(self, vector):
        return sqrt((self.getX() - vector.getX())**2 + (self.getY() - vector.getY())**2)
    
    def distanceX(self, vector):
        return (self.getX() + vector.getX()) / 2
    
    def distanceY(self, vector):
        return (self.getY() + vector.getY()) / 2
    
        
class Vector3:
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getZ(self):
        return self.z
    
    def setX(self, x):
        self.x = x
        
    def setY(self, y):
        self.y = y
        
    def setZ(self, z):
        self.z = z