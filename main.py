from camera import *
from objects import *
from perspective import *
from window import *
from _3d.cube import Cube
from rotation import Rotation
from utils.fpsDisplay import FpsDisplay
from utils.logsDisplay import LogsDisplay
import curses

camera = Camera(LinearPerspective("center"), Vector3(0, 0, 0))

window = Window(120, camera)

window.addObject(FpsDisplay(Vector3(curses.COLS - 15, 1)))
window.addObject(LogsDisplay(Vector3(curses.LINES - 1), 10))
window.addObject(Cube(Vector3(20, 20, 20), Rotation(), 20))


window.start()