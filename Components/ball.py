from Components import basicPart
from Core import constants as const
import pymunk
from pymunk import Vec2d
import pygame
import random

class Ball(basicPart.BasicPart):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        self.mass = kwargs.get('mass', 100)
        self.moment = kwargs.get('moment', (400,400))
        self.colltype = const.COLLTYPE_BALL
        
    def create_body(self) -> pymunk.body:
        body = pymunk.Body(self.mass, self.moment)
        body.position = self.position
        return body
    
    def create_shape(self) -> pymunk.Circle:
        shape = pymunk.Circle(self.body, self.radius)
        shape.friction = self.friction + random.uniform(-0.2,0.5)
        shape.collision_type = self.colltype
        shape.elasticity = self.elasticity
        return shape

    def create_ball(self) -> None:
        self.body = self.create_body()
        self.shape = self.create_shape()
        self.space.add(self.body, self.shape)

    def draw_ball(self) -> None:
        r = self.radius
        v = self.get_position()
        rot = self.get_rotation_vector()
        p = int(v.x), int(self.flipy(v.y, const.SCREENSIZE[1]))
        p2 = p + Vec2d(rot.x, -rot.y) * r * 0.9
        p2 = int(p2.x), int(p2.y)
        pygame.draw.circle(self.screen, self.color, p, int(r), self.width)
        #pygame.draw.line(screen, pygame.Color(0,0,255), p, p2) // Origin Rotation Line
    
    def get_velocity(self) -> pymunk.Vec2d:
        return self.body.velocity
    
    def set_velocity(self, x) -> None:
        self.body.velocity *= x

    def get_position(self) -> pymunk.Vec2d:
        return self.body.position
    
    def get_rotation_vector(self) -> pymunk.Vec2d:
        return self.body.rotation_vector
