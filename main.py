from camera import *
from objects import *
from perspective import *
from window import *

camera = Camera(LinearPerspective("center"), Vector3(0, 0, 0))

window = Window(10, camera)

window.addObject(Text("Hello, World!", 5, 10))
window.addObject(Square(Vector3(25, 25), 25))

window.main()