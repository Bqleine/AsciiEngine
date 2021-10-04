from math import sqrt

class Vector2:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return "Vector2(" + str(self.getX()) + ", " + str(self.getY()) + ")"
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def setX(self, x):
        self.x = x
        
    def setY(self, y):
        self.y = y
        
    def add(self, vector):
        return Vector2(self.getX() + vector.getX(), self.getY() + vector.getY())
    
    # sqrt((x2-x1)^2 + (y2 - y1)^2)
    def distance(self, vector):
        return sqrt((self.getX() - vector.getX())**2 + (self.getY() - vector.getY())**2)
    
    def distanceX(self, vector):
        return vector.getX() - self.getX()
    
    def distanceY(self, vector):
        return vector.getY() - self.getY()
    
        
class Vector3:
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def __str__(self):
        return "Vector3(" + str(self.getX()) + ", " + str(self.getY()) +  + ", " + str(self.getZ()) + ")"
        
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