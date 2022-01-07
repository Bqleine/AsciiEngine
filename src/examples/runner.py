from src.window import Window
from src.camera import Camera
from src.perspective.flatPerspective import FlatPerspective
from src._2d.line import Line
from src.position import Vector3
from src.gamemode import Gamemode
from src._2d.sprite import Sprite
from src.utils.fpsDisplay import FpsDisplay
from src._2d.text import Text
import curses

class Cactus(Sprite):

    def __init__(self, gamemode):
        self.speed = 15
        self.gamemode = gamemode

        position = Vector3(curses.COLS, curses.LINES - 12)
        sprite = " n \n" \
                "\\| \n" \
                 " |/\n"
        super().__init__(position, sprite)

    def tick(self, deltaTime, window):
        self.position = self.position.add(Vector3(-0.1 * self.speed * deltaTime))
        if self.position.x <= -3:
            window.removeObject(self)
            self.gamemode.cactus.remove(self)

class Player(Sprite):

    def __init__(self):
        
        self.jumping = False
        self.velocity = 0
        
        position = Vector3(10, curses.LINES - 12)
        sprite = " o \n" \
                 "-|-\n" \
                 "/ \\\n"
        super().__init__(position, sprite)
        
    def jump(self):
        if self.jumping: return
        self.jumping = True
        self.velocity = 5

    def tick(self, deltaTime, window):
        if self.jumping:
            self.position.y = min(curses.LINES - 12, self.position.y - (self.velocity*deltaTime))
            self.velocity -= deltaTime

            if self.position.y == curses.LINES - 12:
                self.jumping = False


class RunnerGamemode(Gamemode):

    def __init__(self, window):
        self.cactus = []
        self.gameOver = False
        self.player = Player()
        window.addObject(self.player)

    def tick(self, deltaTime, window):

        if window.framesPassed % 500 == 0:
            cactus = Cactus(self)
            window.addObject(cactus)
            self.cactus.append(cactus)

        for i in range(len(self.cactus)):
            cactus = self.cactus[i]
            if cactus.position.x <= 13 and cactus.position.x >= 10 and self.player.position.y >= curses.LINES - 13:
                Text("Game Over!", Vector3(10, curses.LINES - 10)).draw(window)
                window.window.refresh()
                self.gameOver = True
                window.pause()

    def onInput(self, ch, window):
        # 32 = Space key
        if ch == 32 or ch == curses.KEY_UP:
            if self.gameOver:
                self.gameOver = False
                window.unpause()

                i = len(self.cactus) - 1
                while i >= 0:
                    i -= 1
                    window.removeObject(self.cactus[i])
                    del(self.cactus[i])

            else:
                self.player.jump()

camera = Camera(FlatPerspective(), Vector3(0, 0))

window = Window(60, camera)

window.addObject(FpsDisplay(Vector3(3, 3)))

window.addObject(Line(Vector3(0, curses.LINES - 10), Vector3(curses.COLS - 1, curses.LINES - 10))) # Ground
window.gamemode = RunnerGamemode(window)

window.main()
