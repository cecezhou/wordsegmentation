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

		for char in "bcdefghjklmnopqrstuvwxyz":
			self.dict.remove(char)

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
			paths = self.getPossibilitiesList()
			# print paths
			listofStrings = []
			for path in paths:
				self.setVariablesFromPossibility(path)
				listofStrings.append(self.getText())
			return listofStrings
		return None


	def getPossibilitiesList(self):
		paths = []
		stack = [[self.length]]
		currentPath = None
		while stack != []:
			currentPath = stack.pop()
			# get paths from last index of path
			for possibility in self.possiblePreviousSpaces[currentPath[-1]]:
				if possibility != 0:
					newPath = currentPath + [possibility]
					stack.append(newPath)
				else:
					paths.append(currentPath)
		return paths


	def setVariablesFromPossibility(self, possibility):
		lenSpaces = len(self.possiblePreviousSpaces)
		for i in xrange(len(self.spaces)):
			self.adjustVariable(i, 0)
		for i in xrange(1, len(possibility)):
			self.adjustVariable(possibility[i] - 1, 1)


	def classicalSolve(self):
		queue = [([None] * (self.length - 1), 0)]
		ls = []
		ind = False
		while(len(queue) > 0):
			(assignment, num) = queue.pop(0)
			for i in xrange(2):
				assignment[num] = i
				if self.checkAssignment(assignment):
					if num == (self.length - 2):
						ind = True
						assignmentCopy = list(assignment)
						ls.append(assignmentCopy)
					elif num < self.length - 2:
						copy = list(assignment)
						# print (copy, num + 1)
						queue.append((copy, num + 1))
		if ind:
			results = []
			for assignment in ls:
				self.spaces = assignment
				results.append(self.getText())
			return results
		else:
			return None
	
	def normalize(self, d):
		factor=1.0/sum(d.itervalues())
		for k in d:
	  		d[k] = d[k]*factor
	  	self.normalizationFactor = factor
	  	return d

	def getFreq(self, text):
		# get frequencies
		freq_dict = {}
		mydict = enchant.Dict("en_US")
		f = open(text)
		for word in f.read().split():
			word = word.lower()
			if mydict.check(word):
				if word in freq_dict:
					freq_dict[word] += 1
				else:
					freq_dict[word] = 1
		self.freq_dict = self.normalize(freq_dict)
		# print self.freq_dict

