# this allows us to use code from
# the open-source pygame library
# throughout this file

import pygame
from constants import *
from player import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    game_clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Shot.containers = (updatable, drawable)    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player_no_1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    new_field = AsteroidField()

    while True:
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
                return
               
        updatable.update(dt) 

        screen.fill(000)
        for thing in drawable:
            thing.draw(screen)

            for asteroid in asteroids:
                collision_check = asteroid.col_det(player_no_1)
                if collision_check == True:
                    print("Game Over!")
                    raise SystemExit()

        pygame.display.flip()

        dt =  game_clock.tick(60)/1000
        

if __name__ == "__main__":
    main()
