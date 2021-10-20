file = "patterns.txt"
file2 = "config.cfg"
import numpy as np

#################
### Utilitary ###
#################

def rm_Between(string,beg,end) :
	depth = 0
	out = []
	n = len(beg)
	m = len(end)
	for i in range(len(string)) :
		if i < len(string)-n and string[i:i+n] == beg :
			depth += 1
		if depth == 0 :
			out.append(string[i])
		if depth > 0 :
			if i >= m and string[i-m+1:i+1] == end :
				depth -= 1
	return "".join(out)


def rm_After(string,beg) :
	out = []
	n = len(beg)
	for i in range(len(string)) :
		if i <= len(string)-n and string[i:i+n] == beg :
			break
		out.append(string[i])
	return "".join(out)



def get_Between(string, beg, end) :
	out = []
	n = len(beg)
	m = len(end)
	get = False
	for i in range(len(string)) :
		if i >= n and string[i-n:i] == beg :
			get = True
		if get and i <= len(string)-m and string[i:i+m] == end and m>0 :
			get = False
		if get :
			out.append(string[i])
	return "".join(out)

#################
### File read ###
#################

## Pattern

def pattern_Read(text) :
	text = rm_Between(text,"/*", "*/")
	text_list = text.split(";\n\n")
	pattern = []
	for piece in text_list :
		if not "=" in piece :
			continue
		piece = get_Between(piece,"{","}").split(", ")
		export = [int(get_Between(piece[i],"=","")) for i in range(0,3)]
		shape = get_Between(piece[3],"[","]").replace(" ","0").replace("#","1").split(":")
		shape = np.array([list(s) for s in shape], dtype = int)
		export.append(shape)
		pattern.append(export)
	return pattern
#return [[id1,size1,color_id1,piece1],[id2,size2,..]]


## Config [WIP]

data_cfg = ["terrain_width","terrain_height","window_size"\
						"translate_left_key","translate_right_key"\
						"translate_down_key","rotate_left_key"\
						"rotate_right_key","pause_key"]

def cfg_Read(text) :
	#Remove multiples \n
	text_list = text.split("\n")
	text_list = [rm_After(line,'#') for line in text_list]
	text_list = list(filter(("").__ne__, text_list))
	#print(text_list)
	color_list = [0]*256
	#Colors
	for line in text_list :
		if 'color' in line :
			number = int(get_Between(line,"color_","="))
			color = int(get_Between(line,"=",''),16)
			b = color%256; color >>= 8
			g = color%256; color >>= 8
			r = color%256
			color_list[number] = [r,g,b]
	return [color_list]
