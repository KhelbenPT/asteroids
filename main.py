import pygame
from constants import *
from player import *
from asteroidfield import *
from asteroid import *

def main():
	pygame.init()
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	time = pygame.time.Clock()
	dt = 0
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	Shot.containers = (shots, updatable, drawable)
	AsteroidField.containers = (updatable)
	asteroidfield = AsteroidField()
	player = Player(x = SCREEN_WIDTH / 2, y= SCREEN_HEIGHT /2)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
        			return
		for thing in updatable:
			thing.update(dt)
		screen.fill((0,0,0))
		for thing in drawable:
			thing.draw(screen)
		pygame.display.flip()
		for obj in asteroids:
			if player.colision(obj):
				print("Game over!")
				exit()

		for obj in asteroids:
			for shot in shots:
				if shot.colision(obj):
					shot.kill()
					obj.split()
		dt = time.tick(60) /1000


if __name__ == "__main__":
	main()
