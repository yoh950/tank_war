import pygame
from pygame.locals import *

grey = (197,191,190)

pygame.init()

window = pygame.display.set_mode((1200,900),RESIZABLE)
tank = pygame.image.load("assets/images/player.png").convert_alpha()
#tankRival = pygame.image.load("assets/images/").convert_alpha()
#shell = pygame.image.load("assets/images/shell.png").convert_alpha()



class challenger:
	def __init__(self, power, speed, life, die, picture):
		self.power = power
		self.speed = speed
		self.life = life
		self.die = die
		self.picture = picture

	def rival():


	def warrior():









#pygame.display.flip()

game_over = False
while not game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_over= True

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				y_move = 1

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_DOWN:
				y_move = -1


	window.fill(grey)
	window.blit(tank, (200,300))

	pygame.display.update()


		 
		

