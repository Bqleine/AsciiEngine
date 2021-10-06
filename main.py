from camera import *
from objects import *
from perspective import *
from window import *
from utils.fpsDisplay import FpsDisplay

camera = Camera(LinearPerspective("center"), Vector3(0, 0, 0))

window = Window(1000, camera)

window.addObject(Text("Hello, World!", Vector3(5, 10)))
window.addObject(FpsDisplay(Vector3(5, 5)))
window.addObject(Line(Vector3(10, 10), Vector3(50, 25)))
#window.addObject(Square(Vector3(25, 25), 25))

window.start()