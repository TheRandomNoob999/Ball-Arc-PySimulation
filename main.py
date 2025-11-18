import pygame
import math
import pymunk
from pymunk import Vec2d
from Classes import arc
from Classes import ball

COLLTYPE_DEFAULT = 0
COLLTYPE_MOUSE = 1
COLLTYPE_BALL = 2

def flipy(y):
    return -y + 800

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    clock = pygame.time.Clock()
    running = True

    space = pymunk.Space()
    space.gravity = 0.0, -900.0

    balls = []
    testArc = arc.Arc(position=(400,400), radius=200, width=10, friction=0.9, elasticity=0.95, segments=10, rotation_speed=1,start_angle=0, end_angle=300, color=(0,255,0))
    testball = ball.Ball(mass=10, moment=100, position=(400,400), friction=0.5, elasticity=1.1, radius=10, width=2, object_array=balls, color=(255,0,0))

    run_physics = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                run_physics = not run_physics

        testArc.create_arc(COLLTYPE_DEFAULT, space)
        testArc.rotate_arc()

        if len(balls) < 1:
            testball.create_ball(space)

        if run_physics:
            dt = 1.0 / 60.0
            for x in range(1):
                space.step(dt)

        
        screen.fill(pygame.Color(0,0,0))

        for x in balls:
            if(not x.get_position().y < -300):
                # Draw the ball
                x.draw_ball(screen)
            else:
                # Off of screen so remove
                space._remove_body(x.body)
                balls.remove(x)

        testArc.draw_arc(screen)

        pygame.display.flip()
        clock.tick(60)
        pygame.display.set_caption("fps: " + str(clock.get_fps()))


if __name__ == "__main__":
    main()
else:
    print("huh")