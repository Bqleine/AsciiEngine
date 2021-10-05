from math import sqrt, exp

class Vector3:
    
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        
    def __str__(self):
        return "Vector3(" + str(self.x) + ", " + str(self.y) +  + ", " + str(self.z) + ")"

    # sqrt((x2-x1)^2 + (y2 - y1)^2)
    def distance(self, vector):
        return sqrt((self.x - vector.x) ** 2 + (self.y - vector.y) ** 2)

    def distanceX(self, vector):
        return vector.x - self.x

    def distanceY(self, vector):
        return vector.y - self.y

    def distanceZ(self, vector):
        return vector.z - self.z

    def add(self, vector):
        return Vector3(self.x + vector.x, self.y + vector.y, self.z + vector.z)
        
    def applyPerspective(self, camera):

        visible = True

        vanishingPoint = camera.perspective.getVanishingPoint()
        offsetPercentage = 1/(exp(self.z / camera.perspective.ratio))

        x = (self.x - vanishingPoint.x) * offsetPercentage - vanishingPoint.x + camera.position.x
        y = (self.y - vanishingPoint.y) * offsetPercentage - vanishingPoint.y + camera.position.y

        if self.z < camera.position.z:
            visible = False

        return [Vector3(x, y, self.z), visible]