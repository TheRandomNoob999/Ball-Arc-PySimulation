import pygame
from Core import setup
from GUI import frames
from Core import input
from Core import constants as const

run_BallPhysics = True
run_ArcPhysics = True
runningApp = True

def run() -> None:
    gameLoop(setup.window, setup.clock, setup.space, setup.objectManager)

def gameLoop(screen, clock, space, objectManager) -> None:

    frames.loadStandardGUI(objectManager)

    while runningApp:
        input.events(objectManager)

        if run_BallPhysics:
            dt = 1.0 / 60.0
            for x in range(1):
                space.step(dt)

        screen.fill(const.BLACK)

        objectManager.drawGUI(screen)
        objectManager.addBalls(space, screen)
        objectManager.addArcs(space, screen)
        
        objectManager.drawArcs()
        objectManager.drawBalls()

        pygame.display.flip()
        clock.tick(60)


    print("Game loop ended")
