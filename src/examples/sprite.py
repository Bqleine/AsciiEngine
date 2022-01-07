from src.camera import Camera
from src.window import Window
from src.perspective.flatPerspective import FlatPerspective
from src.position import Vector3
from src._2d.sprite import Sprite
from src.utils.fpsDisplay import FpsDisplay
import curses
import os

window = Window(120, Camera(FlatPerspective(), Vector3(0, 0)))

sprite = " O \n" \
         "-|-\n" \
         "/ \\"

window.addObject(Sprite(Vector3(5, 5), sprite))
window.addObject(FpsDisplay(Vector3(100, 10)))

curses.wrapper(window.main())