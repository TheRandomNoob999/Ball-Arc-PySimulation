import pygame
import json
import pymunk
from pymunk import Vec2d
from Classes import arc
from Classes import ball

COLLTYPE_DEFAULT = 0
COLLTYPE_MOUSE = 1
COLLTYPE_BALL = 2

balls = []
arcs = []

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

    space = pymunk.Space()
    space.gravity = 0.0, -900.0

    arcSet = loadArcSet()
    ballSet = loadBallSet()

    run_physics = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                run_physics = not run_physics

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
            else:
                # Off of screen so remove
                space._remove_body(x.body)
                balls.remove(x)

        # Draw Arcs
        for x in arcs:
            x.rotate_arc()
            x.create_arc_collision(COLLTYPE_DEFAULT, space)
            x.draw_arc(screen)

        pygame.display.flip()
        clock.tick(60)
        pygame.display.set_caption("fps: " + str(clock.get_fps()))


if __name__ == "__main__":
    main()
else:
    print("huh")