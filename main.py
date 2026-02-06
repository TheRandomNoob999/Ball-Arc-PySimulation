import pygame
import pymunk
from Core import constants as const
from Components import objects as obj
from GUI import elements as gui

def main():
    pygame.init()
    screen = pygame.display.set_mode(const.SCREENSIZE)
    clock = pygame.time.Clock()
    running = True

    space = pymunk.Space()
    space.gravity = 0.0, -900.0

    run_physics = True

    obj.addGUI(gui.settingsElement())
    obj.addGUI(gui.presetOptionsElement([gui.presetElement()]))
    obj.addGUI(gui.versionElement())

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False # Exit the main loop
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                run_physics = not run_physics # Toggle physics on/off
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed(3)[0]:
                    leftMouseButtonDown = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if pygame.mouse.get_pressed(3)[0] == False:
                    for element in obj.GUI_ELEMENTS:
                        if callable(getattr(element, "mouseClicked", None)):
                            element.mouseClicked(pygame.mouse.get_pos())
        obj.addArcs(space, screen)

        obj.addBalls(space, screen)

        if run_physics:
            dt = 1.0 / 60.0
            for x in range(1):
                space.step(dt)
        
        screen.fill(pygame.Color(0,0,0))
        obj.drawBalls()
        obj.drawArcs()
        obj.drawGUI(screen)

        pygame.display.flip()
        clock.tick(60)
        pygame.display.set_caption("fps: " + str(clock.get_fps()))


if __name__ == "__main__":
    main()
else:
    print("huh")