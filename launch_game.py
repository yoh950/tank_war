import pygame
from pygame.locals import *

grey = (197,191,190)

pygame.init()

window = pygame.display.set_mode((800,800),RESIZABLE)
tank = pygame.image.load("assets/images/player.png").convert_alpha()





#pygame.display.flip()

game_over = False
while not game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_over= True

	window.fill(grey)
	window.blit(tank, (200,300))

	pygame.display.update()


		 
		

