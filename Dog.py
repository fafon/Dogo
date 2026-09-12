import pygame

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
