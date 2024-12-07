import pygame
from constants import *
from player import *
from asteroidfield import *
import sys

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()
split = pygame.sprite.Group()

Shot.containers = (shots,updatable,drawable)
Player.containers = (updatable,drawable)
Asteroid.containers = (asteroids,split, updatable, drawable)
AsteroidField.containers = (updatable,)

asteroid_field = AsteroidField()

def main():
    pygame.init()
    clock = pygame.time.Clock()
    player1 = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        dt = clock.tick(60)/1000
        for update1 in updatable:
            update1.update(dt)
        
        for asteroid in asteroids:
            for shot in shots:
                if shot.check_collision(asteroid):
                    shot.kill()
                    asteroid.split()

        for asteroid in asteroids:
            if asteroid.check_collision(player1):
                sys.exit("Game over!")
        for draw1 in drawable:
            draw1.draw(screen)
        pygame.display.flip()
        
        
    








if __name__ == "__main__":
    main()