from Components import basicPart
import math
import random
import pymunk
import pygame

class Arc(basicPart.BasicPart):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.segments = kwargs.get('segments', 10)
        self.rotation_speed = kwargs.get('rotation_speed', 1)
        self.start_angle = math.radians(kwargs.get('start_angle', 0))
        self.end_angle = math.radians(kwargs.get('end_angle', 360))
        self.segment_shapes = []
    
    def rotate_arc(self):
        self.start_angle += self.rotation_speed * (1/60)
        self.end_angle += self.rotation_speed * (1/60)

    def create_arc_collision(self, collision_type, space):
        points = []
        angle_range = self.end_angle - self.start_angle
        
        # Create points along arc
        for i in range(self.segments + 1):
            angle = self.start_angle + angle_range * i / self.segments
            x = self.position[0] + math.cos(angle) * self.radius
            y = self.position[1] + math.sin(angle) * self.radius
            points.append((x, y))

        #Remove old segments
        for segment in self.segment_shapes:
            space.remove(segment)
        self.segment_shapes = []

        # Create Collision
        for i in range(len(points)-1):
            segment = pymunk.Segment(space.static_body, points[i], points[i+1], self.width * 1.5)
            segment.elasticity = self.elasticity
            segment.friction = self.friction
            segment.collision_type = collision_type
            space.add(segment)
            self.segment_shapes.append(segment)
    
    def draw_arc(self, surface):
        rect = pygame.Rect(
            self.position[0] - self.radius,
            self.position[1] - self.radius,
            self.radius * 2,
            self.radius * 2
        )
        pygame.draw.arc(surface, self.color, rect, self.start_angle, self.end_angle, self.width)
    
    def get_radius(self):
        return self.radius

    def set_radius(self, newRadius):
        self.radius = newRadius
        
    def randomize_rotation(self):
        randomOffset = random.uniform(-360, 360)
        self.start_angle += randomOffset
        self.end_angle += randomOffset