from src.position import Vector3
from src.perspective.perspective import Perspective


class FlatPerspective(Perspective):

    def apply(self, point, camera):
        return [Vector3(point.x, point.y, point.z), True]
