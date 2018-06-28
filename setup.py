import sys
from cx_Freeze import setup, Executable

includefiles = ['README.md', 'fonts/', 'wallpapers/', 'my reminders.db', 'settings.txt']
# packages = ['os', 'sys', 'ctypes', 'PIL', 'pickle', 'json', 'datetime', 'random', 'textwrap']
excludes = ['PyQt5']
includes = ['']

base = None
if sys.platform == 'win32':
	base = 'Win32GUI'

setup(
	name = 'Wallpaper Reminders',
	version = '1.0',
	description = 'A tool that creates simple desktop wallpapers displaying your reminders',
	author = 'Celena Chang',
	author_email = 'changcelena@gmail.com',
	options = {
		'build_exe' : {'include_files': includefiles, 'excludes': excludes}

	},
	executables = [
		Executable('My Reminders.py', base = base, icon = 'wallpapers_icon2.ico'),
		Executable('Wallpaper Reminders.py', base = base, icon = 'wallpapers_icon2.ico')
		]
	)
