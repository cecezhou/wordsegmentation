import enchant

""" Note: variable positions are after char positions, var_0 is after 0th char """

class NoSpaceText:
	def __init__(self, inputText, maxWordLength):
		self.text = inputText
		self.length = len(inputText)
		self.maxWordLength = maxWordLength
		self.spaces = [None] * (self.length - 1)
		self.factors = [None] * (self.length - self.maxWordLength + 1) # True if factor satisfied.
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
			if self.spaces[i + factorIndex]:
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
		for word in wordList:
			if self.dict.check(word) == False:
				self.factors[factorIndex] = False
				return False
		self.factors[factorIndex] = True
		return True

	# Checks partial assignments until first None.
	def checkAssignment(self, assignment):
		prevSpace = 0
		for i in xrange(self.length - 1):
			if assignment[i] == None:
				return True
			if assignment[i]:
				if not self.dict.check(self.text[prevSpace:(i+2)]):
					return False
				prevSpace = i + 1
		return True

	def adjustVariable(self, variable, varValue):
		self.spaces[variable] = varValue

	def printText(self):
		ind = True
		for i in xrange(len(self.factors)):
			if not self.factors[factorIndex]:
				ind = False
				break
		if ind:
			output = ""
			for i in xrange(self.length - 1):
				output += self.text[i]
				if self.spaces:
					output += " "
			output += self.text(self.length - 1)
			return output
		else:
			return "No valid segmentation found."

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
		# for i in xrange(self.possiblePreviousSpaces):

	def classicalSolve(self):
		spaces = [None] * (self.length - 1)
		queue = [([None] * (self.length - 1), 0)]
		while(True):
			(assignment, num) = queue.pop(0)
			ind = True
			for i in xrange(1):
				assignment[num] = i
				if checkAssignment(assignment):
					if num == self.length - 1:
						ind = False
						return assignment
					else:
						queue.append((assignment, num + 1))
			if ind:
				return None
