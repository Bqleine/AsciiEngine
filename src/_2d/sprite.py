from src.object import Object
from src.position import Vector3


class Sprite(Object):

    def __init__(self, position, content, alpha=" ", newline="\n"):
        self.position = position
        self.content = content.split(newline)
        print(self.content)
        self.alpha = alpha

    def draw(self, window):
        for line in range(len(self.content)):
            for col in range(len(self.content[line])):
                if self.content[line][col] in ["\n", self.alpha]: continue
                window.drawCharacter(self.content[line][col], self.position.add(Vector3(col, line)))