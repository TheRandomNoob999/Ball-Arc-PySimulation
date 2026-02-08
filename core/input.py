import pygame
from Core import objects as obj
from Core import app

def checkForButtonClick(button) -> None:
    if callable(getattr(button, "mouseClicked", None)):
        button.mouseClicked(pygame.mouse.get_pos())

def events(objectManager) -> None:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            app.runningApp = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            objectManager.run_BallPhysics = not objectManager.run_BallPhysics
        elif event.type == pygame.MOUSEBUTTONUP:
            if pygame.mouse.get_pressed(3)[0] == False:
                for element in objectManager.GUI_ELEMENTS:
                    if len(element.getChildren()) >= 1:
                        for child in element.getChildren():
                            checkForButtonClick(child)
                    checkForButtonClick(element)
