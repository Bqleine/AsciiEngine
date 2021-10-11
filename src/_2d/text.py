from src.position import Vector3
from src.object import Object

class Text(Object):

    def __init__(self, text, position):
        self.position = position
        self.text = text

    def draw(self, window):
        for i in range(len(self.text)):
            window.drawCharacter(self.text[i], self.position.applyPerspective(window.camera)[0].add(Vector3(i, 0)))
