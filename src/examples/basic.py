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
    def tick(self, deltaTime, timePassed):
        self.rotation.yaw += 0.02 * deltaTime
        self.rotation.pitch += 0.05 * deltaTime

window = Window(1000, Camera(FlatPerspective(), Vector3(0, 0)))

window.addObject(Text("Hello, World!", Vector3(5, 5)))
window.addObject(FpsDisplay(Vector3(100, 10)))
window.addObject(RotatingCube(Vector3(50, 20), Rotation(0, 0), 15))

curses.wrapper(window.main())