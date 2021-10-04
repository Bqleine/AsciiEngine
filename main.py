from time import monotonic
from objects import *
from copy import deepcopy
from os import get_terminal_size

# Main

fps = 10

objects = []
objects.append(Text("Hello, World!", 5, 5))

lastFrame = monotonic()

timePassed = 0

run = True
while run:
    
    # Limit fps
    time = monotonic()
    if lastFrame > time - (1 / fps):
        continue
    
    lastFrame = monotonic()
    #print("Frame:", time)
    
    # Update screen size and clear screen
    terminalSize = get_terminal_size()
    screen = [[" " for x in range(terminalSize.columns)] for y in range(terminalSize.lines)]
    
    # Tick objects
    for obj in objects:
        obj.tick(30/fps, timePassed)
    timePassed += 1
    
    # Draw objects
    for obj in objects:
        obj.draw(screen)
    
    # Draw screen
    output = ""
    for x in screen:
        output += "\n"
        for y in x:
            output += y
    print(output, end="")