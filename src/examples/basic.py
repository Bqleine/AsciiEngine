from src.camera import Camera
from src.window import Window
from src.perspective.flatPerspective import FlatPerspective
from src.position import Vector3
from src._2d.text import Text
from src._2d.rectangle import Rectangle
from src._3d.cube import Cube
from src.rotation import Rotation
from src.utils.fpsDisplay import FpsDisplay
import curses

class RotatingCube(Cube):
    def tick(self, deltaTime, window):
        self.rotation.yaw += 0.02 * deltaTime
        self.rotation.pitch += 0.05 * deltaTime
        self.rotation.roll += 0.05 * deltaTime

window = Window(60, Camera(FlatPerspective(), Vector3(0, 0)))

window.addObject(FpsDisplay(Vector3(10, 5)))
window.addObject(RotatingCube(Vector3(50, 20), Rotation(), 15))

curses.wrapper(window.main())