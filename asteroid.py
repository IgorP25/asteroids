import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255,255), self.position, 
                           self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        rand_angle = random.uniform(20, 50)
        v1 = self.velocity.rotate(rand_angle)
        v2 = self.velocity.rotate(-rand_angle)

        asteroid1 = Asteroid(self.position.x, self.position.y, 
                            self.radius - ASTEROID_MIN_RADIUS)
        asteroid2 = Asteroid(self.position.x, self.position.y, 
                            self.radius - ASTEROID_MIN_RADIUS)
        asteroid1.velocity = v1 * 1.2
        asteroid2.velocity = v2 * 1.2