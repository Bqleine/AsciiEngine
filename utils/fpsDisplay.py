from objects import Text

class FpsDisplay(Text):

    def __init__(self, position):
        super().__init__("", position)

    def draw(self, window): # TODO : Refactor screen -> window
        self.text = "Fps: " + str(window.fps) + "/" + str(window.targetFps)
        super().draw(window)