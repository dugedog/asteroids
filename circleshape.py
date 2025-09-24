import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def col_det(self, position_2):
        distance = pygame.math.Vector2.distance_to(self.position, position_2.position)
        size = self.radius + position_2.radius
#        print (f"The size is {size}, distance is {distance}")
        if distance <= size:
            return(True)
        else:
            return(False)


        
