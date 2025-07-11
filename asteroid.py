import pygame # type: ignore
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position), self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            split_angle = random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            first_angle = self.velocity.rotate(split_angle)
            second_angle = self.velocity.rotate(-split_angle)
            first_rock = Asteroid(self.position.x, self.position.y, new_radius)
            second_rock = Asteroid(self.position.x, self.position.y, new_radius)
            first_rock.velocity = first_angle * 1.2
            second_rock.velocity = second_angle * 1.2