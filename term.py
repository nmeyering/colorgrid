colors = [
"gray"
,"red"
,"green"
,"yellow"
,"blue"
,"magenta"
,"cyan"
,"white"]

def colored(string, color):
	# 0	gray
	# 1	red
	# 2	green
	# 3	yellow
	# 4	blue
	# 5	magenta
	# 6	cyan
	# 7	white
	return '\033[{bold}{col}m{str}\033[0m'.format(
			bold = '' if color in [2,6] else '1;',
			col = color + 30,
			str = string)

def clear():
	print('\033?6l\033[2J')
