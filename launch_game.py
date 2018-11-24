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
		self.position_x = position[0]
		self.position_y = position[1]
		self.orientation = orientation
		self.image = pygame.image.load(picture).convert_alpha()
		self.image = pygame.transform.rotate(self.image, self.orientation)
		window.blit(self.image, position)

	def shoot(self, direction):
		self.picture = pygame.image.load("assets/images/shell.png").convert_alpha()

	def take_damage(self, damage):
		self.life -= damage

	def move(self, direction):
			new_or = self.orientation
			if direction[0] > 0 : new_or = 270
			elif direction[0] < 0: new_or = 90
			if direction[1] > 0 : new_or = 180
			elif direction[1] < 0: new_or = 0
			if new_or == self.orientation:
    			self.position_x += direction[0] * self.speed
				self.position_y += direction[1] * self.speed
			else:
    			self.orientation = new_or

class warrior(challenger):
	pass

window.fill(grey)
player = challenger(5, 10, 100, "assets/images/player.png",(width/2, height/2), 180)
game_over = False
pygame.key.set_repeat(150,250)
while not game_over:
	y_move = 0 
	x_move = 0
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_over= True

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				y_move = -1
			if event.key == pygame.K_DOWN:
				y_move = 1
			if event.key == pygame.K_RIGHT:
				x_move = 1
			if event.key == pygame.K_LEFT:
				x_move = -1
	player.move((x_move, y_move))
	window.fill(grey)
	window.blit(player.image, (player.position_x, player.position_y))
	pygame.display.flip()


		 
		

