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
	#0			1				2				3				4				5				6				7
	#gray		red			green		yellow	blue		magenta	cyan		white
	return '\033[{bold}{col}m{str}\033[0m'.format(
			bold = '' if color in [2,6] else '1;',
			col = color + 30,
			str = string)
