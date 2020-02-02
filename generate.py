from textwrap import wrap
import png

class BgGenerator:
	"""Class to generate the background image along with the associated data."""

	def __init__(self, name, hexArg):
		self.name = name.title()
		self.filename = self.name.replace(' ', '')
		self.hex = hexArg.lower()

	def writedata(self):
		"""Writes background data file."""
		file = open('_backgrounds/'+self.filename+'.dat', 'w')
		file.write('---')
		file.write('\nname: ' + self.name)
		file.write('\ncolorcode: ' + self.hex)
		file.write('\n---')
		file.close()

	def writepng(self):
		"""Writes PNG file."""
		hex_colors = wrap(self.hex, 2)
		rgb_colors = []
		for color in hex_colors:
			rgb_colors.append(int(color, 16))

		color = [(rgb_colors[0], rgb_colors[1], rgb_colors[2])]
		pngfile = open('imgs/'+self.filename+'.png', 'wb')
		pngwriter = png.Writer(1, 1)
		pngwriter.write(pngfile, color)
		pngfile.close()

def main():
	"""Main function."""
	while True:
		print("===========================")
		input_name = input('Enter name: ')
		input_hex = input('Enter hex: ').lstrip('#')

		gen = BgGenerator(input_name, input_hex)
		gen.writedata()
		gen.writepng()


if __name__ == "__main__":
	main()
