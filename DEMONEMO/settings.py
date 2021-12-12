import pygame

pygame.init()

screen = pygame.display.set_mode((900,600))
display = pygame.Surface((300, 200))
clock = pygame.time.Clock()


#Menu buttons
text_font = pygame.font.Font('pixeltype-regular.ttf', 35)

menu_bg = pygame.image.load('menu_bg.png').convert()
play_b = pygame.image.load('play_button.png').convert()
play_b.set_colorkey((0,0,0))
play_b_rect = play_b.get_rect(center = (150,160))

game_win_bg = pygame.image.load('game_win_bg.png').convert()
game_over_bg = pygame.image.load('game_over_bg.png').convert()



#Game UI
class Mouse():

	def __init__(self):
		self.image = pygame.image.load('hand_cursor.png').convert()
		self.image.set_colorkey((255,255,255))
		self.rect = self.image.get_rect(center = (0,0))

	def update(self):
		self.rect.center = (pygame.mouse.get_pos()[0]/3, pygame.mouse.get_pos()[1]/3)



front_side_bg = pygame.image.load('front_side.png').convert()
front_side_bg.set_colorkey((0,0,0))
left_side_bg = pygame.image.load('left_side.png').convert()
left_side_bg.set_colorkey((0,0,0))
right_side_bg = pygame.image.load('right_side.png').convert()
right_side_bg.set_colorkey((0,0,0))

outside_bg = pygame.image.load('outside_bg.png').convert()


left_b = pygame.image.load('left_button.png').convert()
left_b_rect = left_b.get_rect(center = (20, 100))
right_b = pygame.image.load('right_button.png').convert()
right_b_rect = right_b.get_rect(center = (280, 100))
block_b = pygame.image.load('block_button.png').convert()
block_b.set_colorkey((0,0,0))
block_b_rect = block_b.get_rect(center = (150,150))
block_b_bg = pygame.image.load('block_button_bg.png').convert()
block_b_bg.set_alpha(128)

#demonemo
curious_matels_img = pygame.image.load('demonemo.png').convert()
curious_matels_img.set_colorkey((0,0,0))
demonemo_evil_img = pygame.image.load('demonemo_evil.png').convert()
demonemo_evil_img.set_colorkey((0,0,0))
demonemo_img = pygame.image.load('DEMONEMO.png').convert()
demonemo_img.set_colorkey((0,0,0))



#player
lantern_icon = pygame.image.load('lantern.png').convert()
lantern_icon.set_colorkey((0,0,0))
hand_lantern = pygame.image.load('hand_lantern.png').convert()
hand_lantern.set_colorkey((0,0,0))
hand_lantern_off = pygame.image.load('hand_lantern_off.png').convert()
hand_lantern_off.set_colorkey((0,0,0))
lantern_light = pygame.image.load('lantern_light.png').convert()
lantern_light.set_colorkey((0,0,0))
lantern_light.set_alpha(128)

salt_icon = pygame.image.load('salt_sack.png').convert()
salt_icon.set_colorkey((255,255,255))

