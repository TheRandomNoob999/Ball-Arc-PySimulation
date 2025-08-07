import pygame
import math
import pymunk
from pymunk import Vec2d

COLLTYPE_DEFAULT = 0
COLLTYPE_MOUSE = 1
COLLTYPE_BALL = 2

class arc():
    def __init__(self, space, surface, center, radius, start_angle, end_angle, width, segments, color):
        self.space = space
        self.surface = surface
        self.center = center
        self.radius = radius
        self.start_angle = math.radians(start_angle)
        self.end_angle = math.radians(end_angle)
        self.width = width
        self.segments = segments
        self.color = color
        self.segment_shapes = []

    def rotate_arc(self, speed):
        self.start_angle += speed * (1/60)
        self.end_angle += speed * (1/60)

    def create_arc(self):
        points = []
        angle_range = self.end_angle - self.start_angle
        
        # Create points along arc
        for i in range(self.segments + 1):
            angle = self.start_angle + angle_range * i / self.segments
            x = self.center[0] + math.cos(angle) * self.radius
            y = self.center[1] + math.sin(angle) * self.radius
            points.append((x, y))

        #Remove old segments
        for segment in self.segment_shapes:
            self.space.remove(segment)
        self.segment_shapes = []

        # Create Collision
        for i in range(len(points)-1):
            segment = pymunk.Segment(self.space.static_body, points[i], points[i+1], self.width * 1.5)
            segment.elasticity = 0.95
            segment.friction = 0.9
            segment.collision_type = COLLTYPE_DEFAULT
            self.space.add(segment)
            self.segment_shapes.append(segment)
    
    def draw_arc(self):
        rect = pygame.Rect(
            self.center[0] - self.radius,
            self.center[1] - self.radius,
            self.radius * 2,
            self.radius * 2
        )
        pygame.draw.arc(self.surface, self.color, rect, self.start_angle, self.end_angle, self.width)

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
    testArc = arc(space, screen, (400,400), 200, 0, 300, 10, 10, (0,255,0))    
    testball = Ball(screen, 10, 100, (400,400), 0.5, COLLTYPE_BALL, 1.1, 10, 2, balls, (255,0,0))

    run_physics = True
    SPEED = 1

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                run_physics = not run_physics

        testArc.rotate_arc(SPEED)
        testArc.create_arc()

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

        testArc.draw_arc()

        pygame.display.flip()
        clock.tick(60)
        pygame.display.set_caption("fps: " + str(clock.get_fps()))


if __name__ == "__main__":
    main()
else:
    print("huh")