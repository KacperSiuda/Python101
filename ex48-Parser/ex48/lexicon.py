class lexicon(object):
	"""docstring for lexicon"""
	def __init__(self, arg):
		self.directions = ['north', 'south', 'east', 'west',
		                   'down', 'up', 'left', 'right', 'back']
		self.verbs = ['go', 'stop', 'kill', 'eat']
		self.nouns = ['door', 'bear', 'princess', 'cabinet']
		self.stopList = ['he', 'in', 'of', 'from', 'at', 'it']

	def scan(self,text):
		words = text.split()
		result = []
		for word in words:
			if checkWord(word,directions):
				pass
			elif checkWord(word,verbs):
				pass
			elif checkWord(word,nouns):
				pass
			elif checkWord(word,stopList):
				pass


	def checkWord(word,dictionary):
		if word in dictionary:
			return True
		else:
			return False

	def convertNumbers(number):
		try:
			return int(numner)
		except ValueError:
			return None





		