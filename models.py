import enchant

""" Note: variable positions are after char positions, var_0 is after 0th char """


# class searchAgent():
# 	def getAction():

class NoSpaceText:
	def __init__(self, inputText, maxWordLength):
		self.text = inputText
		self.length = len(inputText)
		self.maxWordLength = maxWordLength
		self.spaces = [None] * (self.length - 1)
		self.factors = [0] * (self.length - self.maxWordLength +1)
		self.dict = enchant.Dict("en_US")
		self.possiblePreviousSpaces = [None] * (self.length + 1)

		# for char in "bcdefghjklmnopqrstuvwxyz":
		# 	self.dict.remove(char)
		# self.dict.add("I")
		# self.dict.add("i")

	def getFactor(self, factorIndex):
		return self.text[factorIndex:(factorIndex + self.maxWordLength)]

	def findWordsInFactor(self, factorIndex):
		wordList = []
		currWord = ""
		foundWord = 0
		factorText = self.getFactor(factorIndex)

		if factorIndex == 0:
			foundWord = 1

		for i in xrange(self.maxWordLength):
			if foundWord ==	 1:
				# append character
				currWord += factorText[i]
			if self.spaces[i + factorIndex] == 1:
				# we have already seen a space
				if foundWord == 1:
					wordList.append(currWord)
					# reset current word
					currWord = ""
				else:
					foundWord = 1
			if i + factorIndex == self.length - 1:
				wordList.append(currWord)
		return wordList

	def checkFactor(self, factorIndex):
		wordList = self.findWordsInFactor(factorIndex)
		print wordList
		for word in wordList:
			if self.dict.check(word) == False:
				return False
		return True

	def adjustVariable(self, variable, varValue):
		self.spaces[variable] = varValue

	def printText(self):
		pass

	def dpSearch(self):
		self.possiblePreviousSpaces[0] = [0]
		for i in xrange(1, self.length + 1):
			self.possiblePreviousSpaces[i] = []
			for j in xrange(1, self.maxWordLength):
				if (i - j) >= 0:
					if self.dict.check(self.text[i - j: i]) and self.possiblePreviousSpaces[i-j]:
						self.possiblePreviousSpaces[i].append(i - j)
		if self.possiblePreviousSpaces[self.length]:
			return True
		return False


	def setVariablesFromDP(self):
		pass


	