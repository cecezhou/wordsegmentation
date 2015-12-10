import enchant
import helpers
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
		self.possibleStrings = []
		self.freq_dict = {}
		self.transition_freq_dict = {}
		self.normFactor = 1
		self.transNormFactor = 1
	# default is to use whatever is in alphanumeric.txt, but you can give it what you want 
	def initalizeFrequencies(basetext = "alphanumeric.txt"):
		(self.freq_dict, self.normFactor) = helpers.getFreq(basetext)
		(self.transition_freq_dict, self.transNormFactor) = helpers.getTransitionFreq(basetext)
		return (self.freq_dict, self.normFactor, self.transition_freq_dict, self.transNormFactor)

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

	def classicalSearch(self):
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
			self.possibleStrings = results
			return results
		else:
			return None


	def dpSearch(self):
		self.possiblePreviousSpaces[0] = [0]
		for i in xrange(1, self.length + 1):
			self.possiblePreviousSpaces[i] = []
			for j in xrange(1, self.maxWordLength):
				k = self.maxWordLength - j
				if (i - k) >= 0:
					word = self.text[i - k: i].lower()
					if self.dict.check(word) and self.possiblePreviousSpaces[i-k]:
						self.possiblePreviousSpaces[i].append(i - k)
		if self.possiblePreviousSpaces[self.length]:
			paths = self.getPossibilitiesList()
			# print paths
			listofStrings = []
			for path in paths:
				self.setVariablesFromPossibility(path)
				listofStrings.append(self.getText())
			self.possibleStrings = listofStrings
			return listofStrings
		return None

	def dpGreedy(self, transFreq = False):

		self.possiblePreviousSpaces[0] = [0]
		for i in xrange(1, self.length + 1):
			self.possiblePreviousSpaces[i] = []
			bestprob = 0
			prevspace = None
			for j in xrange(1, self.maxWordLength):
				# get best one where previous one also exists
				k = self.maxWordLength - j
				if (i - k) >= 0:
					word = self.text[i - k: i].lower()
				else:
					continue
				if self.dict.check(word) and self.possiblePreviousSpaces[i-k]:
					frequency = 1
					if transFreq == False:
						if word in self.freq_dict:
							frequency = self.freq_dict[word]
						else:
							frequency = self.normFactor/2
					else: 
						# get previous word
						end = i - k
						start = self.possiblePreviousSpaces[i-k][0]
						prevword = self.text[start:end]
						if (prevword, word) in self.transition_freq_dict:
							frequency = self.transition_freq_dict[prevword, word]
						else:
							frequency = self.transNormFactor/2
						prevword = word
					if frequency > bestprob:
						prevspace = (i - k)
						bestprob = frequency
			if bestprob > 0:
				self.possiblePreviousSpaces[i].append(prevspace)

		# find possible strings from possiblePreviousSpaces
		if self.possiblePreviousSpaces[self.length]:
			paths = self.getPossibilitiesList()
			listofStrings = []
			for path in paths:
				self.setVariablesFromPossibility(path)
				listofStrings.append(self.getText())
			self.possibleStrings = listofStrings
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


	def getBestSeg(self):
		maxProb = 0
		bestString = ""
		for string in self.possibleStrings:
			prob = 1
			wordList = string.split()
			for word in wordList:
				if word in self.freq_dict:
					prob *= self.freq_dict[word]
				else:
					prob *= self.transNormFactor
			if prob > maxProb:
				bestString = string
				maxProb = prob
		return bestString

