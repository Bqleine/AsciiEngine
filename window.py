from time import monotonic
from os import get_terminal_size

class Window:

    def __init__(self, fps, camera):
        self.windowSize = None
        self.running = False
        self.lastFrame = 0
        self.fps = fps
        self.framesPassed = 1

        self.objects = []
        self.camera = camera

    def getWindowSize(self):
        return self.windowSize

    def main(self):
        self.running = True

        while self.running:

            # Limit FPS
            time = monotonic()
            if self.lastFrame > time - (1 / self.fps):
                continue

            self.tick()
            self.updateScreen()

    def tick(self):
        self.lastFrame = monotonic()
        self.terminalSize = get_terminal_size()

        for obj in self.objects:
            obj.tick(30/self.fps, self.framesPassed)

        self.framesPassed += 1

    def updateScreen(self):
        self.screen = [[" " for x in range(self.terminalSize.columns)] for y in range(self.terminalSize.lines - 2)]

        for obj in self.objects:
            obj.draw(self.screen, self.camera)

        output = ""
        for x in self.screen:
            output += "\n"
            for y in x:
                output += y
        print(output, end="")

    def addObject(self, object):
        self.objects.append(object)