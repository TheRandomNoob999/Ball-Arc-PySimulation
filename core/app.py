import pygame
from Core import setup
from GUI import frames
from Core import input
from Core import constants as const

runningApp = True
runningSimulation = False

def run() -> None:
    gameLoop(setup.window, setup.clock, setup.space, setup.objectManager)

def gameLoop(screen, clock, space, objectManager) -> None:

    frames.loadStandardGUI(objectManager)

    while runningApp:
        input.events(objectManager)

        screen.fill(const.BLACK)
        if runningSimulation:
            objectManager.addBalls(space, screen)
            objectManager.addArcs(space, screen)
            objectManager.drawArcs()
            objectManager.drawBalls()
        
        objectManager.drawGUI(screen)
        objectManager.step()
        pygame.display.flip()
        clock.tick(60)


    print("Game loop ended")