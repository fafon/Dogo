import pygame
import time


class Dog:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.side = 1

		self.arrowKeys_action_left = [ 
		pygame.image.load(f"dog_animations/dog_walks_left/frame_{i+1}.png") 
			for i in range(0, 6)
		]

		self.arrowKeys_action_right = [ 
			pygame.image.load(f"dog_animations/dog_walks_right/frame_{i+1}.png") 
				for i in range(0, 6)
			]

		self.arrowKeys_action_up = [ 
					pygame.image.load(f"dog_animations/dog_walks_up/frame_{i+1}.png") 
						for i in range(0, 4)
					]

		self.arrowKeys_action_down = [
			pygame.image.load(f"dog_animations/dog_walks_down/frame_{i+1}.png") 
				for i in range(0, 4)
		]

		self.arrowKeys_action = self.arrowKeys_action_left

		self.idle_state_left = [
			pygame.image.load(f"dog_animations/dog_sits_left/frame_{i+1}.png") 
				for i in range(0, 7)
		]

		self.idle_state_right = [
			pygame.image.load(f"dog_animations/dog_sits_right/frame_{i+1}.png") 
				for i in range(0, 7)
		]

		self.idle_state = self.idle_state_left

		self.spaceKey_action_left = [
			pygame.image.load(f"dog_animations/dog_jumps_left/frame_{i+1}.png") 
				for i in range(0, 5)
		]

		self.spaceKey_action_right = [
			pygame.image.load(f"dog_animations/dog_jumps_right/frame_{i+1}.png") 
				for i in range(0, 5)
		]

		self.spaceKey_action = self.spaceKey_action_left

	def ChangeSide(self):
		self.side *= -1
		self.arrowKeys_action = self.arrowKeys_action_left if self.side == 1 else self.arrowKeys_action_right
		self.idle_state = self.idle_state_left if self.side == 1 else self.idle_state_right
		self.spaceKey_action = self.spaceKey_action_left if self.side == 1 else self.spaceKey_action_right	



width = 468
height = 474
r_border = width 
l_border = 0 
bottom_border = height - 80
upper_border = 10
animationFrames = 6

art_bg = pygame.image.load("terrain.png")
beach = pygame.image.load("beach.png")
bg = art_bg

the_end = False
x = 0
y = 0
animation_counter = 0
first_jump = True

bolt_list = list()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))

last_space_action = 0
space_interval = 2000
space_pressed = False

dog = Dog(10, 10)
first_scr = True

while not the_end:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			the_end = True
			break

	screen.blit(bg, (0, 0))

	keys = pygame.key.get_pressed()
	current_time = pygame.time.get_ticks()

	if keys[pygame.K_LEFT] or keys[pygame.K_a]:	
		if dog.side == -1:
			dog.ChangeSide()
		dog.x -= velocity_x
		if dog.x <= l_border and first_scr:
			dog.x = l_border
		elif not first_scr and dog.x <= l_border:
			first_scr = True
			bg = art_bg
			dog.x = r_border - 10
		screen.blit(dog.arrowKeys_action[animation_counter], (dog.x, dog.y))
		animation_counter += 1
		if animation_counter == animationFrames:
			animation_counter = 0 

	elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
		if dog.side == 1:
			dog.ChangeSide()
		dog.x += velocity_x
		if dog.x >= r_border and first_scr:
			first_scr = False
			bg = beach
			dog.x = l_border + 10
		elif not first_scr and dog.x >= r_border:
			dog.x = r_border
		screen.blit(dog.arrowKeys_action[animation_counter], (dog.x, dog.y))
		animation_counter += 1
		if animation_counter == animationFrames:
			animation_counter = 0 

	elif keys[pygame.K_UP] or keys[pygame.K_w]:
		dog.y -= velocity_y
		if dog.y <= upper_border:
			dog.y = upper_border
		screen.blit(dog.arrowKeys_action_up[animation_counter-2], (dog.x, dog.y))
		animation_counter += 1
		if animation_counter == animationFrames:
			animation_counter = 0 

	elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
		dog.y += velocity_y
		if dog.y >= bottom_border:
			dog.y = bottom_border
		screen.blit(dog.arrowKeys_action_down[animation_counter-2], (dog.x, dog.y))
		animation_counter += 1
		if animation_counter == animationFrames:
			animation_counter = 0 
	else:
		screen.blit(dog.idle_state[animation_counter+1], (dog.x, dog.y))
		animation_counter += 1
		if animation_counter +1 == animationFrames+1:
			animation_counter = 0 

	if keys[pygame.K_ESCAPE]:
		break

	if keys[pygame.K_SPACE]:
		if not space_pressed:
			a_c = 1
			for i in range(1, 6):
				dog.x -= (velocity_x + 1) * dog.side
				if dog.x <= l_border:
					dog.x = l_border
				screen.blit(bg, (0, 0))
				screen.blit(dog.spaceKey_action[a_c], (dog.x, dog.y))
				a_c += 1
				if a_c == animationFrames-1:
					a_c = 0
				time.sleep(0.05)
				pygame.display.flip()
			last_space_action = current_time
		elif current_time - last_space_action >= space_interval:
			last_space_action = current_time
		space_pressed = True
	else:
		space_pressed = False	
			
	pygame.display.flip()

	dt = clock.tick(24) / 1000
	velocity_x = 10
	velocity_y = 10


	#animation_counter += 1
	if animation_counter == animationFrames:
		animation_counter = 0 

	bolt_list = []

pygame.quit()