from Classes import basicPart
import pymunk
from pymunk import Vec2d
import pygame
import random

class Ball(basicPart.BasicPart):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.mass = kwargs.get('mass', 100)
        self.moment = kwargs.get('moment', (400,400))
        self.body = self.create_body()
    
    def create_body(self):
        body = pymunk.Body(self.mass, self.moment)
        body.position = self.position
        return body
    
    def create_ball(self, space):
            self.body = self.create_body()
            shape = pymunk.Circle(self.body, self.radius)
            shape.friction = self.friction + random.uniform(-0.2,0.5)
            shape.collision_type = 2
            shape.elasticity = self.elasticity
            space.add(self.body, shape)

    def draw_ball(self, surface):
            r = self.radius
            v = self.get_position()
            rot = self.get_rotation_vector()
            p = int(v.x), int(self.flipy(v.y, 800))
            p2 = p + Vec2d(rot.x, -rot.y) * r * 0.9
            p2 = int(p2.x), int(p2.y)
            pygame.draw.circle(surface, self.color, p, int(r), self.width)
            #pygame.draw.line(screen, pygame.Color(0,0,255), p, p2) // Origin Rotation Line
    
    def get_position(self):
        return self.body.position
    
    def get_rotation_vector(self):
        return self.body.rotation_vector
