from math import sqrt, sin, cos


class Vector3:

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "Vector3(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"

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
        return camera.perspective.apply(self, camera)

    def applyRotation(self, rotation, origin):
        point = self.add(Vector3(-origin.x, -origin.y, -origin.z))

        point = point.applyYRotation(rotation).applyXRotation(rotation)

        return point.add(Vector3(origin.x, origin.y, origin.z))

    def applyXRotation(self, rotation):
        rSin = sin(rotation.yaw)
        rCos = cos(rotation.yaw)

        y = self.y * rCos - self.z * rSin
        z = self.z * rCos + self.y * rSin

        return Vector3(self.x, y, z)

    def applyYRotation(self, rotation):
        rSin = sin(rotation.pitch)
        rCos = cos(rotation.pitch)

        x = self.x * rCos - self.z * rSin
        z = self.z * rCos + self.x * rSin

        return Vector3(x, self.y, z)
