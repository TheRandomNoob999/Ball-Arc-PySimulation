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

    #Loads required GUI needed
    frames.loadStandardGUI(objectManager)

    while runningApp:
        #Checks all of the inputs for any events
        input.events(objectManager)

        #Background color
        screen.fill(const.BLACK)
        
        # Runs the simulation
        if runningSimulation:
            objectManager.addBalls(space, screen)
            objectManager.addArcs(space, screen)
            objectManager.drawArcs()
            objectManager.drawBalls()
        
        # Draws GUI on top of the simulation
        objectManager.drawGUI(screen)

        # Pymunk physics runs
        objectManager.step() 

        # Pygame necessities
        pygame.display.flip()
        clock.tick(60)


    print("Game loop ended")