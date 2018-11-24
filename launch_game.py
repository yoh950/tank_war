import pygame
from pygame.locals import *

grey = (197,191,190)
height = 900
width = 1200

pygame.init()

window = pygame.display.set_mode((width, height), RESIZABLE)
tank = pygame.image.load("assets/images/player.png").convert_alpha()
#tankRival = pygame.image.load("assets/images/").convert_alpha()
#shell = pygame.image.load("assets/images/shell.png").convert_alpha()



class challenger:
	def __init__(self, gun_power, speed, life, picture, position, orientation):
		self.gun_power = gun_power
		self.speed = speed
		self.life = life
		self.picture = picture
		self.position = position
		self.orientation = orientation
		self.image = pygame.image.load(picture).convert_alpha()
		self.image = pygame.transform.rotate(self.image, self.orientation)
		window.blit(self.image, position)

	def shoot(self, direction):
		self.picture = pygame.image.load("assets/images/shell.png").convert_alpha()

	def take_damage(self, damage):
    		self.life -= damage

	def move(self, direction):
		self.position[0] += direction[0]
		self.position[1] += direction[1]
		

class warrior(challenger):
	pass

window.fill(grey)
player = challenger(5, 1, 100, "assets/images/player.png",(width/2, height/2), 180)
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

	pygame.display.flip()


		 
		

