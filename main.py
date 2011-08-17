#!/bin/env python3
import random

colors = [
"gray",
"red",
"green",
"yellow",
"blue",
"magenta",
"cyan",
"white"]

class Board:
	def __init__(self, size=10, block_char='\u2588'):
		self.size = size
		self.block_char = block_char
		self.field = []
		for y in range(self.size):
			self.field.append([])
			for x in range(self.size):
				self.field[y].append(
					random.randrange(6))

	def flood(self, col):
		old = self.field[0][0],
		if old == col:
			return
		return self._flood(
			old,
			color = col,
			x = 0,
			y = 0)

	def _flood(self, old_color, color, x, y):
		self.field[y][x] = color
		for neighbor in range(4):
			dx = 2 * (neighbor % 2) - 1 if neighbor < 2 else 0
			dy = 2 * (neighbor % 2) - 1 if neighbor >= 2 else 0

			ret = False
			if x + dx in range(self.size) and y + dy in range(self.size):
				if self.field[y + dy][x + dx] == old_color:
					ret = True
					self._flood(old_color, color, x + dx, y + dy)

		return ret

	def __str__(self):
		ret = ''
		for y in range(self.size):
			for x in range(self.size):
				ret += colored(
												#full block
												'{c}{c}'.format(
													c = self.block_char),
												self.field[y][x])
			ret += '\n'
		return ret

def main():
	board = Board(14, '\u2592')

	instructions = '\033[{}A'.format(
		board.size + 1)

	for c in range(len(colors)):
		instructions += '\033[{indent}C{idx}: {val}\n'.format(
			indent = 1 + 2 * board.size,
			idx = c,
			val = colored(colors[c], c))

	turnlimit = 25
	for turn in range(turnlimit):
		print(board)
		print('\033[s', end='')
		print(instructions)
		print('\033[u', end='')
		color = int(input('your move ({}): '.format(
			1 + turn)))
		board.flood(color)

def colored(string, color):
	#0			1				2				3				4				5				6				7
	#gray		red			green		yellow	blue		magenta	cyan		white
	return '\033[{bold}{col}m{str}\033[0m'.format(
			bold = '' if color in [2,6] else '1;',
			col = color + 30,
			str = string)

if __name__ == '__main__':
	main()
