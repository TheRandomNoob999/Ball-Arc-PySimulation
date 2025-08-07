import pygame
import math
import pymunk
from pymunk import Vec2d
from Classes import arc

COLLTYPE_DEFAULT = 0
COLLTYPE_MOUSE = 1
COLLTYPE_BALL = 2

class Ball():
    def __init__(self, surface, mass, moment, position, friction, collision_type, elasticity, radius, width, object_array, color):
        self.surface = surface
        self.mass = mass
        self.moment = moment
        self.position = position
        self.friction = friction
        self.collision_type = collision_type
        self.elasticity = elasticity
        self.radius = radius
        self.width = width
        self.object_array = object_array
        self.color = color
        self.body = self.create_body()
    
    def create_body(self):
        body = pymunk.Body(self.mass, self.moment)
        body.position = self.position
        return body
    
    def create_ball(self, space):
            self.body = self.create_body()
            shape = pymunk.Circle(self.body, self.radius)
            shape.friction = self.friction
            shape.collision_type = self.collision_type
            shape.elasticity = self.elasticity
            space.add(self.body, shape)
            self.object_array.append(self)

    def draw_ball(self):
            r = self.radius
            v = self.get_position()
            rot = self.get_rotation_vector()
            p = int(v.x), int(flipy(v.y))
            p2 = p + Vec2d(rot.x, -rot.y) * r * 0.9
            p2 = int(p2.x), int(p2.y)
            pygame.draw.circle(self.surface, self.color, p, int(r), self.width)
            #pygame.draw.line(screen, pygame.Color(0,0,255), p, p2) // Origin Rotation Line
    
    def get_position(self):
        return self.body.position
    
    def get_rotation_vector(self):
        return self.body.rotation_vector

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
    testball = Ball(screen, 10, 100, (400,400), 0.5, COLLTYPE_BALL, 1.1, 10, 2, balls, (255,0,0))

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

        for ball in balls:
            if(not ball.get_position().y < -300):
                # Draw the ball
                ball.draw_ball()
            else:
                # Off of screen so remove
                space._remove_body(ball.body)
                balls.remove(ball)

        testArc.draw_arc(screen)

        pygame.display.flip()
        clock.tick(60)
        pygame.display.set_caption("fps: " + str(clock.get_fps()))


if __name__ == "__main__":
    main()
else:
    print("huh")