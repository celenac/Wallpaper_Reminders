import sys, ctypes, os
import pickle, json
import datetime, random, textwrap
# from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image, ImageDraw, ImageFont


# Simply click on the exe file to run a test image ewit hthe current settings

class Application:
	def __init__(self):
		self.read_settings()

		text = self.pick_random_note()
		image = self.create_background()
		image_file_name = self.new_image_file_name()
		self.add_text_to_image(text, image, image_file_name)

		folder = "wallpapers"
		image_path = os.path.join(os.getcwd(), folder, image_file_name)

		self.change_background(image_path)


	def pick_random_note(self):
		f = open("notes.db", "rb")
		notes = pickle.load(f)
		text = random.choice(notes)
		f.close()
		return text

	def default_settings(self):
		# instructions in read_me file
		settings = {}
		settings['text position'] = (50,50) # left, center, right
		settings['paragraph width'] = 10
		settings['background color'] = {}
		settings['background color']['red'] = (0, 255)
		settings['background color']['green'] = (0, 255)
		settings['background color']['blue'] = (0, 255)
		settings['text color'] = 'white' # white, black
		settings['font'] = 'ELEPHNT.ttf' # make sure the .ttf file is copied into the "fonts" folder
		settings['font size'] = 50
		with open('settings.txt', 'w') as settings_file:
			json.dump(settings, settings_file, indent = 4)

	def read_settings(self):
		with open('settings.txt', 'r') as settings_file:
			settings = json.load(settings_file)
			self.text_position = (settings['text position'][0], settings['text position'][1])
			self.paragraph_width = settings['paragraph width']
			self.bg_red = (settings['background color']['red'][0], settings['background color']['red'][1])
			self.bg_green = (settings['background color']['green'][0], settings['background color']['green'][1])
			self.bg_blue = (settings['background color']['blue'][0], settings['background color']['blue'][1])
			self.text_color = settings['text color']
			self.font = settings['font']
			self.font_size = settings['font size']

	def random_color(self, r_range, g_range, b_range):
		r_low, r_high = r_range
		g_low, g_high = g_range
		b_low, b_high = b_range
		return random.randint(r_low, r_high), random.randint(g_low, g_high), random.randint(b_low, b_high)

	def create_background(self):
		""" BACKGROUND """
		r,g,b = self.random_color(self.bg_red, self.bg_green, self.bg_blue) # background color
		user32 = ctypes.windll.user32
		screen_width = user32.GetSystemMetrics(0)
		screen_height = user32.GetSystemMetrics(1)
		image = Image.new('RGB', (screen_width, screen_height), (r, g, b))
		return image

	def add_text_to_image(self, text, image, file_name):
		""" TEXT """
		# font

		font = ImageFont.truetype('fonts/' + self.font, size = self.font_size)

		# text color
		if self.text_color == 'white':
			text_color = 'rgb(255,255,255)'
		else: 
			text_color = 'rgb(0,0,0)' # black
			
	
		formatted_msg = textwrap.wrap(text, width = self.paragraph_width)

		# insert text onto image
		draw = ImageDraw.Draw(image)
		draw.text(self.text_position, "\n".join(formatted_msg), fill = text_color, font = font)

		# save image
		image.save(os.getcwd() + "/wallpapers/" + file_name, "PNG")
		return

	# Citation: Michael Bell and Dan O'Boyle on https://stackoverflow.com/questions/16943733/change-windows-background-from-python
	def change_background(self, imagePath):
		SPI_SETDESKWALLPAPER = 20
		ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, imagePath, 0)
		# ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, imagePath , 0)
		return

	def new_image_file_name(self):
		now = datetime.datetime.now()
		return "-".join([str(now.month), str(now.day), str(now.year), "wallpaper.png"])


















"""
Project folder setup:
\application
	\wallpapers
		bg1.png
		bg2.png
		...
	\fonts
	application.py	
"""









def main():
	# Get random text from notes
	application = Application()



if __name__ == '__main__':
	main()
