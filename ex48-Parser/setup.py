try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
			'description': "Mój projekt testowy",
			'author': 'Kacper Siuda',
			'url': 'www.google.com',
			'version': '0.1',
			'install_requires': ['nose']
}

setup(**config)