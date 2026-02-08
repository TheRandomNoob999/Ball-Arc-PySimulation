from Core import constants as const
from Core import objects as obj
import pygame
import pymunk

pygame.init()

window = pygame.display.set_mode(const.SCREENSIZE)
clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = const.GRAVITY
objectManager = obj.ObjectManager(space)

print("Setup complete")