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
				result.append(('direction',word))
			elif checkWord(word,verbs):
				result.append(('verb',word))
			elif checkWord(word,nouns):
				result.append(('noun', word))
			elif checkWord(word,stopList):
				result.append(('stopList', word))
			


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





		
