import pygame
import json
import pymunk
from pymunk import Vec2d
from Classes import arc
from Classes import ball
from Classes import pygameGUI as pGUI

COLLTYPE_DEFAULT = 0
COLLTYPE_MOUSE = 1
COLLTYPE_BALL = 2

def loadBallSet():
    with open("Presets\default.json", mode="r", encoding="utf-8") as read_file:
        loadedFile = json.load(read_file)
    
    x = loadedFile["ball"][0]
    pos = (x["positionx"], x["positiony"])
    color = (x["red"], x["green"], x["blue"])

    loadedSet = {
        "mass": x["mass"],
        "moment": x["moment"],
        "friction": x["friction"],
        "elasticity": x["elasticity"],
        "radius": x["radius"],
        "width": x["width"],
        "position": pos,
        "color": color,
        "amount": x["amount"]
    }

    return loadedSet

def loadArcSet():
    with open("Presets\default.json", mode="r", encoding="utf-8") as read_file:
        loadedFile = json.load(read_file)
    
    x = loadedFile["arc"][0]
    pos = (x["positionx"], x["positiony"])
    color = (x["red"], x["green"], x["blue"])

    loadedSet = {
        "friction": x["friction"],
        "elasticity": x["elasticity"],
        "radius": x["radius"],
        "width": x["width"],
        "position": pos,
        "color": color,
        "amount": x["amount"],
        "segments": x["segments"],
        "rotation_speed": x["rotation_speed"],
        "start_angle": x["start_angle"],
        "end_angle": x["end_angle"]
    }

    return loadedSet

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    clock = pygame.time.Clock()
    running = True
    leftMouseButtonDown = False

    space = pymunk.Space()
    space.gravity = 0.0, -900.0

    arcSet = loadArcSet()
    ballSet = loadBallSet()

    run_physics = True

    balls = []
    arcs = []
    guiElements = []

    test_button = pGUI.button(10, 10, 150, 25, backgroundColor=(192,192,192), label="Presets", autoSize=True, paddingX=10, paddingY=10)
    test_label = pGUI.labelFrame(800-156, 700+51, 100, 100, label="ver 0.3.0", paddingX=10, paddingY=10, autoSize=True)
    guiElements.append(test_button)
    guiElements.append(test_label)

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
                    for element in guiElements:
                        if callable(getattr(element, "mouseClicked", None)):
                            if leftMouseButtonDown:
                                if element.mouseClicked(pygame.mouse.get_pos()):
                                    break
                                leftMouseButtonDown = False


        # Sets up arcs
        if len(arcs) < arcSet["amount"]:
            new_arc = arc.Arc(
                position = arcSet["position"],
                friction = arcSet["friction"],
                elasticity = arcSet["elasticity"],
                radius = arcSet["radius"],
                width = arcSet["width"],
                color = arcSet["color"],
                segments = arcSet["segments"],
                rotation_speed = arcSet["rotation_speed"],
                start_angle = arcSet["start_angle"],
                end_angle = arcSet["end_angle"]
            )

            # Makes the arcs not overlap
            if len(arcs) >= 1:
                new_arc.set_radius(new_arc.get_radius() + 100)
                new_arc.randomize_rotation()
                arcSet["radius"] += 100
                
            arcs.append(new_arc)

        # Sets up balls
        if len(balls) < ballSet["amount"]:
            new_ball = ball.Ball(
                mass = ballSet["mass"],
                moment = ballSet["moment"],
                position = ballSet["position"],
                friction = ballSet["friction"],
                elasticity = ballSet["elasticity"],
                radius = ballSet["radius"],
                width = ballSet["width"],
                color = ballSet["color"]
            )
            new_ball.create_ball(space)
            balls.append(new_ball)

        if run_physics:
            dt = 1.0 / 60.0
            for x in range(1):
                space.step(dt)

        
        screen.fill(pygame.Color(0,0,0))

        # Draw/Spawn Balls
        for x in balls:
            if(not x.get_position().y < -300):
                # Draw the ball
                x.draw_ball(screen)

                # Caps velocity
                if(x.get_velocity().length > 1000):
                    x.set_velocity(0.99)
            else:
                # Off of screen so remove
                space._remove_body(x.body)
                balls.remove(x)

        # Draw Arcs
        for x in arcs:
            x.rotate_arc()
            x.create_arc_collision(COLLTYPE_DEFAULT, space)
            x.draw_arc(screen)
        
        # Draw GUI
        for x in guiElements:
            x.draw(screen)


        pygame.display.flip()
        clock.tick(60)
        pygame.display.set_caption("fps: " + str(clock.get_fps()))


if __name__ == "__main__":
    main()
else:
    print("huh")