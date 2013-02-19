import random
import term

class Board:
	def __init__(self, size=14, max_colors=6, block_char='\u2588'):
		self.size = size
		self.block_char = block_char
		self.field = []
		self.max_colors = max_colors
		for y in range(self.size):
			self.field.append([])
			for x in range(self.size):
				self.field[y].append(
					random.randrange(max_colors))

	def uniform(self):
		c = self.field[0][0]
		for line in self.field:
			for tile in line:
				if not tile == c:
					return False
		return True

	def flood(self, col):
		if col not in range(self.max_colors):
			raise AttributeError('Invalid color!')

		old = self.field[0][0]
		if old == col:
			return
		return self._flood(
			old,
			color = col,
			x = 0,
			y = 0)

	def _flood(self, old_color, color, x, y):
		#TODO: use a more efficient flood fill algorithm
		if x not in range(self.size) or y not in range(self.size):
			return
		if not self.field[y][x] == old_color:
			return
		self.field[y][x] = color
		for neighbor in range(4):
			#left, right, up, down:
			#should yield (-1,0), (1,0), (0,-1), (0,1)
			dx = 2 * (neighbor % 2) - 1 if neighbor < 2 else 0
			dy = 2 * (neighbor % 2) - 1 if neighbor >= 2 else 0
			self._flood(old_color, color, x + dx, y + dy)

	def __str__(self):
		ret = ''
		for y in range(self.size):
			for x in range(self.size):
				ret += term.colored(
					#full block
					'{c}{c}'.format(
						c = self.block_char),
					self.field[y][x])
			ret += '\n'
		return ret
