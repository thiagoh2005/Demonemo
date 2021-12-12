import pygame, sys, random
from settings import *

pygame.init()

pygame.mouse.set_visible(False)

cursor = Mouse()
current_pos = [0,1,0]

side_front = []
side_left = []
side_right = []

time_to_end = 7200

#player
salt = 5
stamina = 90
lantern = 600

lantern_on = False
block_on = False

#states
game_on = False
game_over = False
game_win = False


#demonemo
class Demonemo():

	def __init__(self, image_path, d_type, time, attack_time, attack_frequency):
		self.d_type = d_type
		self.image = pygame.image.load(image_path).convert()
		self.image.set_colorkey((0,0,0))
		self.rect = self.image.get_rect(center = (80, 20))
		self.states = {'peeking': False, 'attacking': False}
		self.current_pos = [0,0,0]
		self.attack_frequency = attack_frequency
		self.attack_pause = attack_time
		self.base_time = time
		self.time = self.base_time
		self.block = False
		self.hit_light = False


	def attack(self, d_group):
		if self.d_type == 'curious':
			choice = random.choice([0,1,2])
		elif self.d_type == 'demonemo':
			choice = 1
		elif self.d_type == 'evil':
			choice = random.choice([0,2])
		lst = [0,0,0]
		lst[choice] = 1
		for d in d_group:
			if d.current_pos == lst and d.d_type != self.d_type:
				self.time = 60
				self.current_pos = [0,0,0]
				return self.current_pos
		self.states['peeking'] = True

		return lst

		return choice
	def update(self, d_group):

		if self.time == 0:
			self.block = False
			self.current_pos = self.attack(d_group)
			
			self.time = self.attack_frequency

		else:

			
			self.time -= 1	
		
		if self.block == True and (self.d_type == 'curious' or self.d_type == 'evil'):

			self.attack_pause = self.attack_frequency

			self.states['peeking'] = False	
			self.current_pos = [0,0,0]
		if self.hit_light and (self.d_type == 'curious' or self.d_type == 'demonemo'):
			self.attack_pause = self.attack_frequency
			self.states['peeking'] = False	
			self.current_pos = [0,0,0]		
		if self.states['peeking']:
			if self.attack_pause == 0:
				self.states['attacking'] = True
				self.states['peeking'] = False
				

			elif self.block == False:
				self.attack_pause -= 1
		elif self.states['attacking']:
			print('u ded')
			
		


demonemo_evil = Demonemo('demonemo_evil.png', 'evil', 4800, 360, 1200)
curious_matels = Demonemo('MatheusThink.png', 'curious', 120, 900, 480)
demonemo = Demonemo('DEMONEMO.png', 'demonemo', 2400, 600, 960)

#bug, only curious matels is spawning
demonemo_group = [demonemo_evil, curious_matels, demonemo]


while True:
	cursor.update()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			if play_b_rect.collidepoint((event.pos[0]/3, event.pos[1]/3)):
				game_on = True

	display.blit(menu_bg, (0,0))
	display.blit(play_b, play_b_rect)
	display.blit(cursor.image, cursor.rect)		


	while game_on:
		display.fill('black')
		time_to_end -= 1

		demonemo_evil.update(demonemo_group)
		curious_matels.update(demonemo_group)
		demonemo.update(demonemo_group)
		print(game_over)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if left_b_rect.collidepoint((event.pos[0]/3, event.pos[1]/3)) and current_pos[1]:
					current_pos = [1,0,0]
				if right_b_rect.collidepoint((event.pos[0]/3, event.pos[1]/3)) and current_pos[1]:
					current_pos = [0,0,1]
				if right_b_rect.collidepoint((event.pos[0]/3, event.pos[1]/3)) and current_pos[0]:
					current_pos = [0,1,0]
				if left_b_rect.collidepoint((event.pos[0]/3, event.pos[1]/3)) and current_pos[2]:
					current_pos = [0,1,0]
				if block_b_rect.collidepoint((event.pos[0]/3, event.pos[1]/3)):

					for d in demonemo_group:
						if d.current_pos == current_pos:
							d.block = True
		
						else:
							d.block = False

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_x:
					lantern_on = True
				if event.key == pygame.K_c:
					for d in demonemo_group:
						if d.current_pos == current_pos:
							d.block = True
			
						else:
							d.block = False
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_x:
					lantern_on = False

		display.blit(outside_bg, (0,0))
		for d in demonemo_group:
			if d.states['peeking']:
		
				if d.current_pos[0] and current_pos[0]:
					display.blit(d.image, (80, 20))
				if d.current_pos[1] and current_pos[1]:
					display.blit(d.image, (60, 40))
				if d.current_pos[2] and current_pos[2]:
					display.blit(d.image, (120, 20))
			if d.states['attacking']:
				game_over = True



		if current_pos[1]:
			display.blit(front_side_bg, (0,0))
		if current_pos[0]:
			display.blit(left_side_bg, (0,0))
			
			display.blit(left_side_bg, (0,0))
		if current_pos[2]:
			display.blit(right_side_bg, (0,0))

		if lantern_on and lantern:
			display.blit(lantern_light, (0,0))
			display.blit(hand_lantern, (230, 130))
			lantern -= 1
			for d in demonemo_group:
				if d.current_pos == current_pos:
					d.hit_light = True
				else:
					d.hit_light = False
		elif lantern_on:
			display.blit(hand_lantern_off, (230, 130))


		display.blit(left_b, left_b_rect)
		display.blit(right_b, right_b_rect)
		display.blit(block_b_bg, block_b_rect)
		display.blit(block_b, block_b_rect)
		display.blit(cursor.image, cursor.rect)
		display.blit(lantern_icon, (280, 180))
		display.blit(text_font.render(f'{round(lantern/60)}', False, (240, 160, 0)), (240, 180))
		
		cursor.update()
		
		if time_to_end <= 0:
			game_win = True
			game_on = False

		while game_win:
			display.fill('black')
			display.blit(game_win_bg, (0,0))
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					game_on = False
					pygame.quit()
					exit()
			screen.blit(pygame.transform.scale(display, (900,600)), (0,0))
			pygame.display.update()
			clock.tick(60)
		while game_over:
			display.fill('black')
			display.blit(game_over_bg, (0,0))
			if event.type == pygame.QUIT:
					game_on = False
					pygame.quit()
					exit()

			screen.blit(pygame.transform.scale(display, (900,600)), (0,0))
			pygame.display.update()
			clock.tick(60)


		screen.blit(pygame.transform.scale(display, (900,600)), (0,0))
		
		pygame.display.update()
		clock.tick(60)


	screen.blit(pygame.transform.scale(display, (900,600)), (0,0))
	pygame.display.update()
	clock.tick(60)
