#!/bin/env python3
from board import Board
from term import *

def game():
	board = Board( block_char='\u2592')

	instructions = '''
The goal is to flood-fill the whole board with the same color.
Your starting point is the upper left corner.
By successively filling in colors that are adjacent to your captured
area you expand your territory until every field is uniformly colored.

Good luck!
'''

	menu = '\033[s\033[{}A'.format(
		board.size + 1)

	for c in range(len(colors)):
		menu += '\033[{indent}C{idx}: {val}\n'.format(
			indent = 1 + 2 * board.size,
			idx = c,
			val = colored(colors[c], c))

	menu += '\n'
	menu += '\033[{indent}Cn: New Game\n'.format(
			indent = 1 + 2 * board.size)
	menu += '\033[{indent}Cq: Quit\n'.format(
			indent = 1 + 2 * board.size)
	menu += '\033[{indent}Ch: Help\n'.format(
			indent = 1 + 2 * board.size)
	menu += '\033[u'

	turnlimit = 25
	turn = 0

	while turn < turnlimit:
		print(board)
		print(menu)
		cmd = input('your move ({}): '.format(
			1 + turn))
		try:
			board.flood(int(cmd))
			turn += 1
		except AttributeError as e:
			print(e)
		except ValueError:
			if cmd == 'n':
				return True
			elif cmd == 'q':
				return False
			elif cmd == 'h':
				print(instructions)
		if board.uniform():
			print('Congratulations, you won!')
			break

	if turn == turnlimit:
		print('Too bad, you lost.')
	return not input('Play again? [Y/n] ').lower() == 'n'

def main():
	while game():
		pass

if __name__ == '__main__':
	main()
