#!/usr/bin/env python3
"""
Game name:		Space Invaders (change to cooler name)
Author:			Dan Petersson
Github:			DanPetersson
Github link:	to add

Description:
---------------------------------------------------------
- Survive as long as possible as shoot as many aliens as possible to get good score

---------------------------------------------------------
Python:			3.8 						
PyGame:			1.9.6

Revision updates:
---------------------------------------------------------
Backlog_revision_history.txt

"""

import pygame
import random
import math

# ----------------------------
# 		Define Classes
# ----------------------------

class SpaceObject:

	def __init__(self, image, explosion_image, posX=0, posY=0, speedX = 0, speedY = 0, sizeX = 64, sizeY = 64, state = 'show', sound = ' '):
		#self.namme	= name
		self.image  = image
		self.explosion_image = explosion_image 
		self.sizeX  = sizeX
		self.sizeY  = sizeY
		self.posX   = posX
		self.posY   = posY
		self.speedX = speedX
		self.speedY	= speedY
		self.state	= state		# 'hide', 'show'
		self.sound 	= sound
		self.explosion_counter = -1
		self.explosion_image

	def show(self):
		if self.state == 'show' and self.explosion_counter <= 0:
			screen.blit(self.image, (int(self.posX), int(self.posY)))
		elif self.explosion_counter > 0:
			screen.blit(self.explosion_image, (int(self.posX), int(self.posY)))
			
class SpaceShip(SpaceObject):
    
    # def __init__(self):
    #     super().__init__()

	def update_player_postion(self, screen_sizeX, screen_sizeY):

		# Update X position (update with min/max)
		self.posX += self.speedX
		if self.posX < 0:
			self.posX = 0
		elif self.posX > screen_sizeX-self.sizeX:
			self.posX = screen_sizeX-self.sizeX

		# Update Y position (update with min/max)
		self.posY += self.speedY
		if self.posY < 0:
			self.posY = 0
		elif self.posY > screen_sizeY-self.sizeY:
			self.posY = screen_sizeY-self.sizeY


class SpaceEnemy(SpaceObject):

	def update_enemy_position(self, screen_sizeX, screen_sizeY):

		# Update X position
		self.posX += self.speedX

		# Update Y position
		self.posY += self.speedY

class Bullet(SpaceObject):

	def update_bullet_position(self, screen_sizeX, screen_sizeY):

		# Update X position
		self.posX += self.speedX

		# Update Y position, and change state if outside screen
		self.posY += self.speedY
		if self.posY < -self.sizeY:
			self.state = 'hide'


	def fire_bullet(self, player):

		self.posX = player.posX + player.sizeX/2 - self.sizeX/2
		self.posY = player.posY
		self.sound.play()
		self.state = 'show'


# ----------------------------
# 		Define Procedures
# ----------------------------

def text_objects(text, font):
    textSurface = font.render(text, True, (255,255,0))
    return textSurface, textSurface.get_rect()

def message_display(text, screen_sizeX, screen_sizeY):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((screen_sizeX/2),(screen_sizeY/2))
    screen.blit(TextSurf, TextRect)
    pygame.display.update()


def menu():
	# into screen 
	intro_screen = True
	while intro_screen:

		screen.fill(background_color)
		screen.blit(background_image, (0,0))

		# Welcome message
		new_game_font = pygame.font.Font('freesansbold.ttf', 64)
		play_again_font = pygame.font.Font('freesansbold.ttf', 32)

		new_game_text = new_game_font.render('SPACE WARS', True, (255, 255, 000))
		play_again_text = play_again_font.render('New Game (Y/N)', True, (255, 255, 000))

		screen.blit(new_game_text, (int(screen_sizeX/2-250), int(screen_sizeY/2-75)))
		screen.blit(play_again_text, (int(screen_sizeX/2-150), int(screen_sizeY/2)))

		for event in pygame.event.get():	
			if event.type == pygame.QUIT:
				intro_screen = False
				quit_game = True

		# if 'Y' or 'N' key is pressed
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_y or event.key == pygame.K_z or event.key == pygame.K_RETURN:
					intro_screen = False
					quit_game = False
				if event.key == pygame.K_n:
					intro_screen = False
					quit_game = True

		# Display intro screen
		pygame.display.update()

	return quit_game

def paused(screen_sizeX, screen_sizeY):

	largeText = pygame.font.SysFont("freesansbold",115)
	TextSurf, TextRect = text_objects("Paused", largeText)
	TextRect.center = ((screen_sizeX/2),(screen_sizeX/2))
	screen.blit(TextSurf, TextRect)

	pause = True
	while pause:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				# 'p' for unpause 
				if event.key == pygame.K_p or event.key == pygame.K_ESCAPE:
					pause = False
		screen.blit(TextSurf, TextRect)
		#button("Continue",150,450,100,50,(0,255,0),bright_green,unpause)
		#button("Quit",550,450,100,50,(255,0,0),bright_red,quitgame)
		pygame.display.update()

		

def enemy_respawn(enemy, level):
	enemy.explosion_counter = -1	
	enemy.posX 	= random.randint(0, screen_sizeX - enemy.sizeX) 
	enemy.posY 	= random.randint(-screen_sizeY, -100)
	if enemy.posX < screen_sizeX / 3:
		enemy.speedX = random.randint(0, 10) / 10 * enemy.speedY
	elif enemy.posX > screen_sizeX * 2 / 3:
		enemy.speedX = random.randint(-10, 0) / 10 * enemy.speedY
	else:
		enemy.speedX = random.randint(-5, 5) / 10 * enemy.speedY
	
#	enemy.speedY = level
	
def is_collision(object1, object2):

	obj1_midX = object1.posX + object1.sizeX
	obj1_midY = object1.posY + object1.sizeY
	obj2_midX = object2.posX + object2.sizeX
	obj2_midY = object2.posY + object2.sizeY

	# think if I want to improve this...
	distance = math.sqrt(math.pow(obj1_midX-obj2_midX,2) + math.pow(obj1_midY-obj2_midY,2))
	collision_limit = (object1.sizeX + object1.sizeY + object2.sizeX + object2.sizeY) / 5

	return distance < collision_limit

def show_explosion(object, image):
	screen.blit(image, (int(object.posX), int(object.posY)))


def show_score(score, level, font_size = 16, x=10, y=10):
	score_font = pygame.font.Font('freesansbold.ttf', font_size)
	level_text = score_font.render("Level : " + str(level), True, (255, 255, 0))
	score_text = score_font.render("Score : " + str(score), True, (255, 255, 0))
	screen.blit(level_text, (x, y))
	screen.blit(score_text, (x, y + 5 + font_size))


def show_game_over(screen_sizeX, screen_sizeY):
	
	# Move enemies below screen (is there a better way?)
	for i in range(num_of_enemies):
		enemies[i].posY = screen_sizeY + 100

	# Write text
	game_over_font = pygame.font.Font('freesansbold.ttf', 64)
	game_over_text = game_over_font.render('GAME OVER', True, (255, 0, 0))
	screen.blit(game_over_text, (int(screen_sizeX/2-200), int(screen_sizeY/2-75)))
	return_font = pygame.font.Font('freesansbold.ttf', 32)
	return_text = return_font.render('Press Return', True, (255, 0, 0))
	screen.blit(return_text, (int(screen_sizeX/2-100), int(screen_sizeY/2)))


#############################
#		Main Program		#
#############################
#if __name__ == '__main__':

# initialize pygame 
pygame.init()

# Initialize Global variables
screen_sizeX = 800
screen_sizeY = 600
screen_size = (screen_sizeX, screen_sizeY)
background_color = (255, 255, 0)
# Initialize screen
screen = pygame.display.set_mode((screen_sizeX, screen_sizeY))

# Initialize fonts
#score_font = pygame.font.Font('freesansbold.ttf', 32)

# Initialize images
#example_image     = pygame.image.load('.\\images\\') 
icon_image			= pygame.image.load('.\\images\\icon_01.png') 
background_image	= pygame.image.load('.\\images\\background_01.jpg')
player_image		= pygame.image.load('.\\images\\MilFal_02.png')
bullet_image		= pygame.image.load('.\\images\\bullet.png')
enemy_images	    = [pygame.image.load('.\\images\\ufo_01.png'),
				       pygame.image.load('.\\images\\death_star.png'),
				       pygame.image.load('.\\images\\ufo_03.png'),
				       pygame.image.load('.\\images\\ufo_04.png'),
				       pygame.image.load('.\\images\\alien_01.png'),
					   pygame.image.load('.\\images\\yoda.png')]
explosion_images	= [pygame.image.load('.\\images\\explosion_01.png'),
				       pygame.image.load('.\\images\\explosion_02.png')]

background_image_hight = 600

				      
# Caption and Icon
pygame.display.set_caption("Space Wars")
pygame.display.set_icon(icon_image)

# Initialize sounds
bullet_sound		= pygame.mixer.Sound('.\\sounds\\laser.wav')
explosion_sound		= pygame.mixer.Sound('.\\sounds\\explosion.wav')

# Start backgound music
pygame.mixer.music.load('.\\sounds\\background.wav')
pygame.mixer.music.play(-1)


# Initialize settings
player_maxSpeedX = 3.2			# recommended: 3
player_maxSpeedY = 3.2			# recommended: 3
enemy_maxSpeedX = 2
enemy_maxSpeedY = 2


# --------------------
# Full Game Play Loop
# --------------------

quit_game = False
while not quit_game:

	# Start manu
	quit_game = menu()

	# Game settings
	num_of_enemies	= 5				# recommended: 5
	level_change	= 1000			# recommended: 1000
	level_score_increase = 10
	level_enemy_increase = 5
	level			= 1
	score			= 0

	# initialize other variables / counters
	level_iter	 = 0
	loop_iter	 = 0
	keyX_pressed = 0
	keyY_pressed = 0
	game_over 	 = False
	go_to_menu 	 = False
	backgound_Y_lower = 0
	backgound_Y_higher = backgound_Y_lower - background_image_hight

	# initialize player and bullet
	player = SpaceShip(player_image, explosion_images[0], screen_sizeX/2-32, screen_sizeY-100)
	bullet = Bullet(bullet_image, explosion_images[0], speedY = -10, sound = bullet_sound, state = 'hide', sizeX = 32, sizeY = 32)

	# initialize enemies
	enemies = []
	for i in range(num_of_enemies):
		enemy_image_index = (level - 1) % len(enemy_images)	
	#	enemy_image_index = random.randint(1,len(enemy_images)) - 1
		enemies.append(SpaceEnemy(enemy_images[enemy_image_index], explosion_images[1], speedY = level))
		enemy_respawn(enemies[i], level)


	# --------------------
	# Main Game Play Loop
	# --------------------

	while not go_to_menu and not quit_game:

		# Fill screen and background image	
		screen.fill(background_color)

		# Background imaages moving
		backgound_Y_lower += 1
		backgound_Y_higher += 1
		if backgound_Y_lower > screen_sizeY:
			temp = backgound_Y_higher
			backgound_Y_lower = backgound_Y_higher
			backgound_Y_higher = backgound_Y_lower - background_image_hight
		screen.blit(background_image, (0,backgound_Y_higher))
		screen.blit(background_image, (0,backgound_Y_lower))

		# check if increase level
		level_iter += 1
		if level_iter > level_change and not game_over:
			level_iter = 0
			level += 1
			# increase number of enemies with higher speed
			for i in range(num_of_enemies, num_of_enemies+level_enemy_increase):
				enemy_image_index = level % len(enemy_images)
				#	enemy_image_index = random.randint(1,len(enemy_images) - 1)
				enemies.append(SpaceEnemy(enemy_images[enemy_image_index], explosion_images[1], speedY = level))
				enemy_respawn(enemies[i], level)
			num_of_enemies	+= level_enemy_increase
			# increase number of enemies
			score += level_score_increase

		# Check events and take action
		for event in pygame.event.get():	
			if event.type == pygame.QUIT:
				quit_game = True	

			# if key is pressed
			if event.type == pygame.KEYDOWN:
				
				# 'p' or ESC' for pause 
				if event.key == pygame.K_p or event.key == pygame.K_ESCAPE:
				 	paused(screen_sizeX, screen_sizeY)

				# 'arrow keys' for movement
				elif event.key == pygame.K_LEFT:
					player.speedX = -player_maxSpeedX
					keyX_pressed += 1
				elif event.key == pygame.K_RIGHT:
					player.speedX = player_maxSpeedX
					keyX_pressed += 1
				elif event.key == pygame.K_UP:
					player.speedY = -player_maxSpeedY
					keyY_pressed += 1
				elif event.key == pygame.K_DOWN:
					player.speedY = player_maxSpeedY
					keyY_pressed += 1

				# if space key, fire bullet or contiue from Game Over				
				elif (event.key == pygame.K_SPACE or event.key == pygame.K_a) and bullet.state == 'hide':
					bullet.fire_bullet(player)
					
				# if return and Game Over, go to menu				
				elif event.key == pygame.K_RETURN and game_over:
					go_to_menu = True

			# if key is released, stop movement in a nice way
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					keyX_pressed -= 1
					if keyX_pressed == 0:
						player.speedX = 0
				if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					keyY_pressed -= 1
					if keyY_pressed == 0:
						player.speedY = 0

		# Move player and check not out of screen
		player.update_player_postion(screen_sizeX, screen_sizeY)
		bullet.update_bullet_position(screen_sizeX, screen_sizeY)

		if game_over:
			# add explosion picture here
			show_game_over(screen_sizeX, screen_sizeY)
			show_score(score, level)
		else:
			
			# Move enemies and check collisions
			for i in range(num_of_enemies):
				
				# if enemy exploding
				if enemies[i].explosion_counter >= 1:
					enemies[i].explosion_counter -= 1
				elif enemies[i].explosion_counter == 0:
					enemy_respawn(enemies[i], level)				
				else:
					enemies[i].update_enemy_position(screen_sizeX, screen_sizeY)
					if enemies[i].posY > screen_sizeY:
						enemy_respawn(enemies[i], level)
					enemies[i].show()
					
					# if enemy collision with player
					if is_collision(enemies[i], player):
						explosion_sound.play()
						player.explosion_counter = 5
						game_over = True
						break
					
					# if bullet hits enemy 
					elif bullet.state == 'show' and is_collision(enemies[i], bullet) :
						explosion_sound.play()
						enemies[i].explosion_counter = 10
						score += 1
						bullet.state = 'hide'

				enemies[i].show()

			# show player
			bullet.show()
			player.show()
			show_score(score, level)
		
		pygame.display.update()


print('Successfully quit!')