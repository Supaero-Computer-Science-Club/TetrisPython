import random as rd
import numpy as np



def print_tab(tab) :
	(x,y) = tab.shape
	for x_ in range(0,x) :
		for y_ in range(0,y) :
			print('{0:3d}'.format(tab[x_,y_]),end = "")
		print("\n")

"""
Class Terrain
Doc TODO
"""
class Terrain :
	def __init__(self,sx = 10, sy = 20, off = 2) :
		self.xsize = sx
		self.ysize = sy
		self.offset = off
		# offset to consider collision
		self.grid       =  np.ones((sy + 2*off,sx + 2*off), dtype = np.int8 )*(-2)
		self.grid_color = np.zeros((sy + 2*off,sx + 2*off), dtype = np.uint8)
		self.grid[off:sy+off, off:sx+off] = 0

"""
Class Piece
Attributes :
 - Mask : numpy square array
 - Color : Color of the piece
 - Size : Size of the mask
 - pos : np array
 - x : x of the center
 - y : y of the center

"""
class Piece :
	def __init__(self, mask, color, pos) :
		self.mask = mask #numpy array size n*n
		self.color = color
		self.size = len(mask)
		#x & y of spawn point ( with the +2 offset)
		#x and y on the bottom left of the piece
		self.pos = pos
		self.x   = pos[0]
		self.y   = pos[1]

	def move(self, move_id) :
		mask = np.copy(self.mask)
		pos  = np.copy(self.pos )
		u = np.array([1,0],dtype = int)
		v = np.array([0,1],dtype = int)

		# Rotation Left
		if   move_id == "r_left" : 
			mask = np.rot90(mask, 1)
		# Rotation Right
		elif move_id == "r_right" :
			mask = np.rot90(mask,-1)
		# Translation Left
		elif move_id == "t_left" :
			pos -= u
		# Translation Right
		elif move_id == "t_right" :
			pos += u
		# Translation Down
		elif move_id == "t_down" :
			pos += v
		# Translation Up (illegal)
		elif move_id == "t_up" :
			pos -= v
		return [mask, pos]




#Hardcoded piece ugh
m = np.array([[0,1,0],[1,1,1],[0,0,0]], dtype = np.uint8)
p = np.array([3,2], dtype = int)

"""
Class Simu

Handles the terrain & piece modifications
"""
class Simu :
	def __init__(self) :
		self.piece_list = []
		self.active_piece = 0
		self.terrain = 0
		self.n_pieces = 0

	def set_Piece_List(self,pattern) :
		sizes = []
		for piece in pattern :
			mask = np.array(piece[-1], dtype = np.uint8)
			pos = np.array([0,0], dtype = np.int8)
			p = Piece(mask, piece[2], pos)
			self.piece_list.append(p)
			sizes.append(p.size)
		self.n_pieces = len(sizes) # =len(piece_list)
		return max(sizes)

	def set_Terrain(self,terrain) :
		self.terrain = terrain

	def new_Piece(self) :
		k = rd.randint(0,self.n_pieces-1)
		
		self.active_piece = self.piece_list[k]
		sx = self.terrain.xsize
		off = self.terrain.offset
		self.active_piece.pos = np.array([off+sx//2,off], dtype = np.int8)
		self.active_piece.x = off+sx//2
		self.active_piece.y = off

	##################
	## Move gestion ##
	##################

	def check_Move(self, move_id) :
		piece = self.active_piece
		[mask, pos] = piece.move(move_id)

		x0 = pos[0]
		y0 = pos[1]
		size = piece.size
		mask_ter = self.terrain.grid[y0:y0+size, x0:x0+size] + mask
		#Move possible ?
		if mask_ter[mask_ter[:,:] == 2].size == 0 and mask_ter[mask_ter[:,:] == -1].size == 0 :
			return [mask,pos,move_id]
		else :
			return [0,0,-1]


	def do_Move(self, move_id) :
		[mask, pos, move_id] = Simu.check_Move(self,move_id)
		if move_id == -1 :
			return "Stuck"
		else :
			self.active_piece.mask = mask
			self.active_piece.pos  = pos
			self.active_piece.x = pos[0]
			self.active_piece.y = pos[1]
			return "Stuckn't"

  ###################
	## Special moves ##
	###################
	def go_down(self) :
		state = Simu.do_Move(self,"t_down")
		if state == "Stuck" :
			piece = self.active_piece
			x0 = piece.x
			y0 = piece.y
			size = piece.size
			self.terrain.grid[      y0:y0+size, x0:x0+size] += piece.mask
			self.terrain.grid_color[y0:y0+size, x0:x0+size] += piece.mask*piece.color
			Simu.erase_Line(self)
			Simu.new_Piece(self)

	def erase_Line(self) :
		grid = self.terrain.grid
		c_grid = self.terrain.grid_color
		sx = self.terrain.xsize
		off = self.terrain.offset
		for i in range(len(grid)) :
			if sum(grid[i]) == sx -4*off :
				grid   = np.delete(grid  ,i,   axis=0)
				grid   = np.insert(grid  ,off,0,axis=0)
				c_grid = np.delete(c_grid,i,   axis=0)
				c_grid = np.insert(c_grid,0,0,axis=0)
				grid[off][0:off] = -2
				grid[off][off+sx:] = -2
		self.terrain.grid       = grid
		self.terrain.grid_color = c_grid 

	

	#############
	## Display ##
	#############
	def display(self) :
		#Piece param
		piece = self.active_piece
		x0 = piece.x
		y0 = piece.y
		size = piece.size
		#Terrain param
		ter = self.terrain
		off = ter.offset
		Ly = ter.ysize
		Lx = ter.xsize
		c_grid = np.copy(ter.grid_color)
		c_grid[y0:y0+size, x0:x0+size] += piece.mask*piece.color
		return c_grid[off:Ly+off, off:Lx+off]




