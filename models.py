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
		self.dict.add("haoqing")

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
				prevSpace = -1
			if assignment[i] == 1:
				if not self.dict.check(self.text[prevSpace:(i+1)]):
					return False
				prevSpace = i + 1
		if prevSpace == -1:
			return True
		else:
			return self.dict.check(self.text[prevSpace:])

	def adjustVariable(self, variable, varValue):
		self.spaces[variable] = varValue

	def getText(self):
		ind = True
		for i in xrange(self.length - 1):
			if self.spaces[i] == None:
				ind = False
				break
		if ind:
			output = ""
			for i in xrange(self.length - 1):
				output += self.text[i]
				if self.spaces[i]:
					output += " "
			output += self.text[self.length - 1]
			return output
		else:
			return "No valid segmentation found."

	def dpSearch(self):
		self.possiblePreviousSpaces[0] = [0]
		for i in xrange(1, self.length + 1):
			self.possiblePreviousSpaces[i] = []
			for j in xrange(1, self.maxWordLength):
				k = self.maxWordLength - j
				if (i - k) >= 0:
					if self.dict.check(self.text[i - k: i]) and self.possiblePreviousSpaces[i-k]:
						self.possiblePreviousSpaces[i].append(i - k)
		if self.possiblePreviousSpaces[self.length]:
			self.setVariablesFromDP()
			# self.getText()
			return True
		return False

	def setVariablesFromDP(self):
		lenSpaces = len(self.possiblePreviousSpaces)
		index = lenSpaces - 1
		for i in xrange(len(self.spaces)):
			self.spaces[i] = 0
		while index != 0:
			if index != lenSpaces - 1 :
				self.adjustVariable(index - 1, 1)
			index = self.possiblePreviousSpaces[index][0]

	def classicalSolve(self):
		queue = [([None] * (self.length - 1), 0)]
		while(len(queue) > 0):
			(assignment, num) = queue.pop(0)
			ind = False
			for i in xrange(2):
				assignment[num] = i
				if self.checkAssignment(assignment):
					if num == self.length - 1 and i == 1:
						ind = True
						self.spaces = assignment
						return assignment
					elif num < self.length - 2:
						copy = list(assignment)
						queue.append((copy, num + 1))
			if ind:
				break
		return None
