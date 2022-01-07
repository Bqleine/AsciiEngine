import curses
from math import floor
from time import monotonic
from src.gamemode import Gamemode


class Window:

    def __init__(self, targetFps, camera):
        self.windowSize = [0, 0]
        self.running = False
        self.time = 0  # Unified time for objects
        self.lastFrame = 0
        self.targetFps = targetFps
        self.fps = 0
        self.framesLastSecond = 0
        self.lastSecond = 0
        self.framesPassed = 1
        self.startTime = 0
        self.paused = False
        self.gamemode = Gamemode()

        self.window = curses.initscr()
        self.window.keypad(True)
        self.window.nodelay(True)
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)

        #self.window = curses.newwin(curses.LINES - 1, curses.COLS - 1, 0, 0)

        self.logs = []

        self.objects = []
        self.camera = camera

    def getTerminalSize(self):
        return [curses.COLS, curses.LINES]

    def start(self):
        self.main()
        self.quit()

    def main(self):
        self.startTime = monotonic()

        self.running = True
        while self.running:

            # Limit FPS
            self.time = monotonic()
            if self.lastFrame >= self.time - (1 / self.targetFps):
                continue

            self.processInputs()

            if self.paused: continue

            self.tick()
            self.updateScreen()

    def quit(self):
        curses.nocbreak()
        self.stdscr.keypad(False)
        curses.echo()
        curses.endwin()

    def processInputs(self):
        ch = self.window.getch()
        if ch != -1:
            self.gamemode.onInput(ch, self)

    def tick(self):

        # Calulate FPS
        if self.lastSecond + 1 <= self.time:
            self.fps = self.framesLastSecond
            self.framesLastSecond = 0
            self.lastSecond = self.time

        self.windowSize = self.getTerminalSize()

        deltaTime = 30 / self.targetFps
        for obj in self.objects:
            obj.tick(deltaTime, self)
        self.gamemode.tick(deltaTime, self)

        self.framesPassed += 1
        self.framesLastSecond += 1
        self.lastFrame = self.time

    def updateScreen(self):

        self.window.erase()
        curses.update_lines_cols()

        for obj in self.objects:
            obj.draw(self)

        self.window.refresh()

    def addObject(self, object):
        self.objects.append(object)

    def removeObject(self, object):
        self.objects.remove(object)

    def pause(self):
        self.paused = True

    def unpause(self):
        self.paused = False

    def drawCharacter(self, character, position, attr=curses.COLOR_WHITE):
        y = floor(position.y)
        x = floor(position.x)

        if x < 0 or x >= self.windowSize[0] - 1 or y < 0 or y >= self.windowSize[1] - 1: return

        try:
            self.window.addch(y, x, character, attr)
        except:
            self.quit()
            print("Failed to add character '" + character + "' at coordonitates x=" + str(x) + " y=" + str(y))
            raise


    def log(self, message):
        self.logs.append(message)
