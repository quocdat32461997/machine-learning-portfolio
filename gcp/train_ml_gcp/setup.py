"""
Author: Firstname Lastname
File: setup.py
"""

# import dependencies
from setuptools import find_packages
from setuptools import setup

# read required packages
with open('requirements.txt') as file:
	REQUIRED_PACKAGES = file.read().split('\n')

setup(
	name = 'trainer',
	version = '0.1',
	install_requires = REQUIRED_PACKAGES,
	packages = find_packages(),
	include_package_data = True,
	description = 'My first training package'
)
