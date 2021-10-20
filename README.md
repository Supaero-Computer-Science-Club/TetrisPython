# Tetris modular 2000
## Introduction
Upper text<br>
Bottom text

> Since its beginning, mankind has always played games, and Tetris, is one of those games, even if it's recent, it's still relevant and played by many people, even bypassing cultures differences

### TODO List
- [ ] Chose terrain size
- [ ] A proper graphic interface
- [ ] A score system
- [ ] Next piece coming window 
- [ ] Chose controls (maybe)
- [ ] Sound support (maybe)
- [x] Line Suppression
- [x] Read the config files
- [x] Have it to work

## Plan
---
<ol type = "1">
	<li>
		<a href = "#Requierments">Requierments</a>
		<ol type = "i">
			<li>
				<a href="#Python-version">Python version</a>
			</li>
			<li>
				<a href="#Librairies">Librairies</a>
			</li>
		</ol>
	</li>
	<li>
		<a href="#The-Game">The Game</a>
		<ol type = "i">
			<li>
				<a href="#Command">Command</a>
			</li>
			<li>
				<a href="#How-to-play">How to play</a>
			</li>
		</ol>
	</li>
	<li>
		<a href="#User-customization">User customization</a>
		<ol type = "i">
			<li>
				<a href="#Import-custom-pieces">Import custom pieces</a>
			</li>
			<li>
				<a href="#Chose-colors">Chose all the colors used</a>
			</li>
			<li>
				<a href="#Chose-terrain-sizes">Chose the size of the terrain</a>
			</li>
			<li>
				<a href="#Change-controls">Change the controls (Maybe)</a>
			</li>
			<li>
				<a href="#Change-piece-selector">Chose how the pieces are selected (Maybe)</a>
			</li>
		</ol>
	</li>
</ol>

## Requierments
---
### Python version

Coded using Python 3.9 <br>
(TODO check) 3.8 might be enough

### Librairies
Some librairies such as :
- [numpy](https://numpy.org/)
- [pygame](https://www.pygame.org)

## The Game
---
It's a basic Tetris, for now at least, but I wanted it to be as flexible as possible, so there are are few functionnalities that differ from the original Tetris, detailed in [User customization](#User-customization)<br>
Score not implemented yet<br>
Better graphic interface to come<br>
T-spin works

### How to play 
To play, just enter `python main.py` in something that receives commands and understands python such as Linux terminal or Windows Powershell 

### How it works
As said in the librairies section, it uses the numpy librairy, and it is used a lot to compute collisions between pieces.<br>
More precisely, the game uses the numpy masks and array check to find if there is any collision happening in the next wanted move, to recognize, the collision array has a structure composed of `0` where there is nothing, `1` for a piece and `-2` outside, so if there are `-1` or `2` in the array it won't move.


## User customization
---
- [Import custom pieces](#Import-custom-pieces)
- [Chose all the colors used](#Chose-colors)
- [Chose the size of the terrain](#Chose-terrain-size)
- [Change the controls (Maybe)](#Change-controls)
- [Chose how the pieces are selected (Maybe)](#Change-piece-selector)

### Import custom pieces
Yes, indeed you can create your own pieces to play with them. It's not that hard but you have to respect a few rules to avoid the code to eplode !
- Respect the syntax, look closely to the existing pieces for templates
- The piece mask must be a square, so maybe add spaces at the end
- Keep in mind that the center square will be the center of rotation of the piece
- For new color for pieces, check the color implementation doc below, and put the index of the color, not the color itself<br>

To implement your pieces, all you have to do is to edit the file `patterns.txt` in the `config` folder<br>
If it's still unclear, lets have an example :<br>
For the T piece, the mask is `[ # :###:   ]`, we can see that `#` represents a block, a space nothing, and `:` means to go on the next layer. We have a third layer to have a squared piece and this layer is on the bottom, otherwise the rotation would be pretty strange.

### Chose colors
In this game you can also change colors ! Wow such amazing features aren't they !<br>
To do so you have to go and edit the `config.cfg` in the `config` folder with any notepad application<br>
There are some fields non-related to colors so scroll a bit until you find a huge list of colors, note that by default the 0-16 indexes are reserved for game use, so for pieces colors, use the indexes from 17 to 255.<br>
As exposed, there are 256 indexes for color, so you have a lot of choices, each is associated with a color in hexadecimal, if you want to convert your rgb color into hexa, you can go [here](https://www.rgbtohex.net/)


### Chose terrain size
TODO

### Change controls
TODO

### Change piece selector
TODO