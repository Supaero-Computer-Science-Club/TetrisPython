##########################
##### OWO TETRIS OWO #####
##########################


#Lib & files
from src import game_struct as struct
from src import data_read as data
import numpy as np
import pygame
from time import time

config_file = "config/config.cfg"
pattern_file = "config/patterns.txt"

def read_File(fileName) :
	f = open(fileName,'r', encoding="utf8")
	text = f.read()
	f.close()
	return text.lower()
"""
Random bs
def disp_update() :
	rect_border = pygame.Rect(0,0,scale*terrain_width,scale*terrain_height)
	pygame.draw.rect(screen, color_list[border_color],rect_border)
	for y in range(0, terrain_height) :
		print("\n")
		for x in range(0,terrain_width) :
			print(grid[y,x],end = "")

			rect_piece  = pygame.Rect(scale*x,scale*y,0.9*scale,0.9*scale)

			pygame.draw.rect(screen,color_list[grid[y,x]],rect_piece)
	pygame.display.update()
"""

if __name__ == "__main__" :
	##############################
	### USER MODIFICATION ZONE ###
	##############################

	#Terrain parameters
	terrain_width  = 10
	terrain_height = 20
	terrain_color  = 0 
	border_color   = 1 

	#Hardcoded colors ugh
	color_list = [(0,0,0),(40,40,40),(255,0,0)]

	#Window property
	scale = 40
	(WIDTH, HEIGHT) = (terrain_width*scale, terrain_height*scale)
	background_color = (0,0,0)

	#Files treatment
	text = read_File(pattern_file)
	pattern = data.pattern_Read(text)

	text2 = read_File(config_file)
	config = data.cfg_Read(text2)
	color_list = config[0]
	###########
	### END ###
	###########

	#Screen init
	screen = pygame.display.set_mode((WIDTH, HEIGHT)) #Size of the window
	screen.fill(background_color) #Baackground of the window
	pygame.display.flip() #Closes at the end of the code
	pygame.display.set_caption('Tetris') #Name of the window

	#Simu init
	sim = struct.Simu()
	max_size = sim.set_Piece_List(pattern)
	ter = struct.Terrain(terrain_width,terrain_height,max_size-1)
	sim.set_Terrain(ter)
	sim.new_Piece()
	
	grid = sim.display()
	#Time
	t = time()



	rect_border = pygame.Rect(0,0,WIDTH,HEIGHT)
	pygame.draw.rect(screen, color_list[border_color],rect_border)

	pygame.display.update()
	hold_time = 200
	pygame.key.set_repeat(hold_time,hold_time)
	i = 0
	run = True
	while run :
		#Check if quit
		for event in pygame.event.get():
			if event.type == pygame.QUIT :
				run = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					sim.do_Move("t_up")
					grid = sim.display()
				if event.key == pygame.K_LEFT:
					sim.do_Move("t_left")
					grid = sim.display()
				if event.key == pygame.K_RIGHT:
					sim.do_Move("t_right")
					grid = sim.display()
				if event.key == pygame.K_DOWN:
					sim.do_Move("t_down")
					grid = sim.display()
				if event.key == pygame.K_DELETE :
					sim.do_Move("r_left")
					grid = sim.display()
				if event.key == pygame.K_PAGEDOWN :
					sim.do_Move("r_right")
					grid = sim.display()
		#print(grid)
		if (time()-t > 1) :
			sim.go_down()
			t = time()
			grid = sim.display()
		for y in range(0, terrain_height) :
			for x in range(0,terrain_width) :
				rect_piece  = pygame.Rect(scale*x,scale*y,0.9*scale,0.9*scale)
				pygame.draw.rect(screen,color_list[grid[y,x]],rect_piece)
		pygame.display.update()
