import pygame
from pygame.locals import *
import math

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
		self.rect = self.image.get_rect()
		self.or_to_angle = {
			"up":0,
			"left":90,
			"down":180,
			"right":270
			}
		self.image = pygame.transform.rotate(self.image, self.or_to_angle[self.orientation])
		window.blit(self.image, position)

	def shoot(self):
		new_shell = shell(self.gun_power, self.or_to_angle[self.orientation], 2,
			(self.position_x, self.position_y), "assets/images/shell.png", self.image)
		return new_shell

	def take_damage(self, damage):
		self.life -= damage

	def move(self, direction):
		new_or = self.orientation
		if direction[0] > 0 :
			new_or = "right"
		elif direction[0] < 0:
			new_or = "left"
		elif direction[1] > 0 :
			new_or = "down"
		elif direction[1] < 0:
			new_or = "up"
		rotate = self.convert_dir_to_angle(self.or_to_angle[self.orientation], self.or_to_angle[new_or])
		if rotate == 360:
			new_pos_x = self.position_x + direction[0] * self.speed
			new_pos_y = self.position_y + direction[1] * self.speed
			if new_pos_y > 0 and new_pos_y < height - self.image.get_height() :
				self.position_y = new_pos_y
			if new_pos_x > 0 and new_pos_x < width - self.image.get_width() :
				self.position_x = new_pos_x
		else:
			self.orientation = new_or
			self.image = pygame.transform.rotate(self.image, rotate)

	def convert_dir_to_angle(self, orientation, angle):
    		return 360 - orientation + angle


class warrior(challenger):
	pass

class shell:
	def __init__(self, damage, direction, speed, position, picture, shooter):
		self.damage = damage
		self.direction = direction
		self.speed = speed
		self.position_x = position[0]
		self.position_y = position[1]
		self.image = pygame.image.load(picture).convert_alpha()
		self.image = pygame.transform.rotate(self.image, direction)
		self.rect = self.image.get_rect()

		#print(shooter.get_height)
		if direction == 0:
			self.position_x = self.position_x + shooter.get_width()/2 
			self.position_y = self.position_y - self.image.get_height()
		elif direction == 90:
			self.position_x = self.position_x - self.image.get_width()
			self.position_y = self.position_y + shooter.get_height()/2
		elif direction == 180:
			self.position_x = self.position_x + shooter.get_width()/2
			self.position_y = self.position_y + shooter.get_height()
		elif direction == 270:
			self.position_x = self.position_x + shooter.get_width()
			self.position_y = self.position_y + shooter.get_height()/2
	
	def move(self):
		new_pos_x = self.position_x - math.sin(math.radians(self.direction)) * self.speed
		new_pos_y = self.position_y - math.cos(math.radians(self.direction)) * self.speed
		if new_pos_y > 0 and new_pos_y < height - self.image.get_height() :
			self.position_y = new_pos_y
		else: 
			return True
		if new_pos_x > 0 and new_pos_x < width - self.image.get_width() :
			self.position_x = new_pos_x
		else:
			return True
		return False
		


		
window.fill(grey)

player = challenger(5, 10, 100, "assets/images/player.png",(width/2, height/2), "left")
enemy = warrior(5, 10, 100, "assets/images/player.png",(width/3, height/3), "up")
game_over = False
pygame.key.set_repeat(150,25)
game_objects = []
mun = None
game_objects.append(player)
game_objects.append(enemy)

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
			if event.key == pygame.K_SPACE:
				mun = player.shoot()
				game_objects.append(mun)

	player.move((x_move, y_move))
	window.fill(grey)

	for game_object in game_objects:
		rects = [my_object.rect for my_object in game_objects if my_object is not game_object]
		print(rects)
		if type(game_object) is shell:
			if game_object.move() == True:
				game_objects.remove(game_object)
		if game_object.rect.collidelist(rects) >= 0:
			print("youpii")
		if game_object not in game_objects:
			del(game_object)
		else:
			window.blit(game_object.image, (game_object.position_x, game_object.position_y))
		
	
	pygame.display.flip()





