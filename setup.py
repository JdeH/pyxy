import os
import sys

sys.path.append ('pyxy')
import base

from setuptools import setup

def read (*paths):
	with open (os.path.join (*paths), 'r') as aFile:
		return aFile.read()

setup (
	name = 'xyref',
	version = base.getProgramVersionString (),
	description = 'Draws a timing chart of the contents of variables in multithreaded Python programs in realtime',
	long_description = (
		read ('README.rst') + '\n\n' +
		read ('pyxy/license_reference.txt')
	),
	keywords = ['debug, debugger, log, logger, time, timechart, timing, sequence, thread, multithreading, event, variable, realtime'],
	url = 'http://www.qquick.org',
	license = 'app',
	author = 'Jacques de Hooge',
	author_email = 'jacques.de.hooge@qquick.org',
	packages = ['xyref'],	
	include_package_data = True,
	install_requires = [],
	classifiers = [
		'Development Status :: 1 - Planning',
		'Intended Audience :: Developers',
		'Natural Language :: English',
		'License :: OSI Approved :: Apache Software License',
		'Topic :: Software Development :: Libraries :: Python Modules',
		'Operating System :: Microsoft :: Windows',
		'Operating System :: POSIX :: Linux',
		'Programming Language :: Python :: 3.5'        
	],
)
