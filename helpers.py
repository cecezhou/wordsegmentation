import re
import enchant

# replace hyphen \n's and all double quotes
def parseBaseText():
	print "Type in the file you would like to use for base frequencies."
	print "Press enter to default to A Farewell to Arms by Ernest Hemingway"
	# we provide 'farewell_to_arms.txt' if you would like to use a different file feel free
	basetext = raw_input()
	if basetext == "":
		basetext = "farewell_to_arms.txt"
	string = open(basetext).read()
	new_str = re.sub('[^a-zA-Z\n\']', ' ', string)
	# remove excess apostrophes
	new_str.replace(' \' ','')
	open('alphanumeric.txt', 'w').write(new_str)

def normalize(d):
	factor=1.0/sum(d.itervalues())
	for k in d:
  		d[k] = d[k]*factor
  	return (d, factor)

def getFreq(textfile):
	# get frequencies
	freq_dict = {}
	mydict = enchant.Dict("en_US")
	f = open(textfile)
	for word in f.read().split():
		word = word.lower()
		if mydict.check(word):
			if word in freq_dict:
				freq_dict[word] += 1
			else:
				freq_dict[word] = 1
	(freq_dict, factor) = normalize(freq_dict)
	return (freq_dict, factor)

def getTransitionFreq(textfile):
	transition_freq_dict = {}
	mydict = enchant.Dict("en_US")

	f = open(textfile)
	prev = ""
	for word in f.read().split():
		word = word.lower()
		if mydict.check(word):
			if (prev, word) in transition_freq_dict:
				transition_freq_dict[(prev, word)] += 1
			else: 
				transition_freq_dict[(prev, word)] = 1
			# set prev to be current word for next word
			prev = word
	# careful with normalization factors
	(transition_freq_dict, factor) = normalize(transition_freq_dict)
	return (transition_freq_dict, factor)

def modifyDictionary():
	mydict.add("haoqing")

	for char in "bcdefghjklmnopqrstuvwxyz":
		self.dict.remove(char)

	self.dict.remove("int")

	twoletter = open('twoletter.txt').read()
	twoletterlist = twoletter.split()
	for word in twoletterlist:
		self.dict.remove(word)


def compare(s1, s2):
	# split by spaces 
	s1words = s1.split()
	s2words = s2.split()
	for (w1, w2) in zip(s1words, s2words):
		# strip excess spaces and change to lowercase
		if w1.lower() != w2.lower():
			return False 
	return True

# string1 = "they    truly  beat  me"
# string2 = "They truly beat me"

# print compare(string1, string2)
