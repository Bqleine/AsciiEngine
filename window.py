from time import monotonic
import os
import curses

class Window:

    def __init__(self, targetFps, camera):
        self.windowSize = [0, 0]
        self.running = False
        self.time = 0 # Unified time for objects
        self.lastFrame = 0
        self.targetFps = targetFps
        self.fps = 0
        self.framesLastSecond = 0
        self.lastSecond = 0
        self.framesPassed = 1
        self.startTime = 0

        self.stdscr = curses.initscr()
        self.stdscr.keypad(True)
        curses.noecho()
        curses.cbreak()

        self.window = curses.newwin(curses.LINES - 1, curses.COLS - 1, 0, 0) # TODO : add as args, autoresize

        self.objects = []
        self.camera = camera

    def getTerminalSize(self):
        return [curses.COLS, curses.LINES]

    def start(self):
        curses.wrapper(self.main)
        self.quit()


    def main(self, a):
        self.startTime = monotonic()

        self.running = True
        while self.running:

            # Limit FPS
            self.time = monotonic()
            if self.lastFrame > self.time - (1 / self.targetFps):
                continue

            self.tick()
            self.updateScreen()

    def quit(self):
        curses.nocbreak()
        self.stdscr.keypad(False)
        curses.echo()
        curses.endwin()

    def tick(self):

        # Calulate FPS
        if self.lastSecond + 1 <= self.time:
            self.fps = self.framesLastSecond
            self.framesLastSecond = 0
            self.lastSecond = self.time

        self.windowSize = self.getTerminalSize()

        for obj in self.objects:
            obj.tick(30/self.targetFps, self.framesPassed)

        self.framesPassed += 1
        self.framesLastSecond += 1
        self.lastFrame = self.time

    def updateScreen(self):

        self.window.erase()

        for obj in self.objects:
            obj.draw(self)

        self.window.refresh()

    def addObject(self, object):
        self.objects.append(object)

    def drawCharacter(self, character, position, attr=curses.COLOR_WHITE):
        y = round(position.y)
        x = round(position.x)

        if x < 0 or x >= self.windowSize[0] or y < 0 or y >= self.windowSize[1]: return

        self.window.addch(y, x, character, attr) # TODO : Replace round with math.floor / ceil ?