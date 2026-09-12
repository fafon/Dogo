import pygame
import time
from Dog import Dog


def main():
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

	animation_counter = 0
	the_end = False

	clock = pygame.time.Clock()
	screen = pygame.display.set_mode((width, height))

	last_space_action = 0
	space_interval = 2000
	space_pressed = False

	
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

		if animation_counter == animationFrames:
			animation_counter = 0 
	pygame.quit()


if __name__ == '__main__':
	dog = Dog(10, 10)
	main()