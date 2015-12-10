import time
import re
import helpers
import models

# compare the 4 algorithms' runtime and output -
# Classical Search, Dynamic Programming, 
# Individual Frequencies, and Transition frequencies
def compareAlgorithms(comptext):

	mytext = models.NoSpaceText(comptext, 15)

	mytext.freq_dict = freq_dict
	mytext.normFactor = normFactor
	mytext.transition_freq_dict = transition_freq_dict
	mytext.transNormFactor = transNormFactor

	print "Classical Search"

	start_time = time.time()
	mytext.classicalSearch()
	print mytext.getBestSeg()
	print("--- %s seconds ---\n" % (time.time() - start_time))

	print "Dynamic Programming Approach"

	start_time = time.time()
	mytext.dpSearch()
	print mytext.getBestSeg()
	print("--- %s seconds ---\n" % (time.time() - start_time))


	print "Dynamic Programming with Naive Frequency Approach"

	start_time = time.time()
	mytext.dpGreedy()
	print mytext.getBestSeg()
	print("--- %s seconds ---\n" % (time.time() - start_time))

	print "Dynamic Programming with Transition Frequency Approach"

	start_time = time.time()
	mytext.dpGreedy(transFreq = True)
	print mytext.getBestSeg()
	print("--- %s seconds ---\n" % (time.time() - start_time))


helpers.parseBaseText()
print "Segmenting Text..."

# process basetexts 
(freq_dict, normFactor) = helpers.getFreq("alphanumeric.txt")
(transition_freq_dict, transNormFactor) = helpers.getTransitionFreq("alphanumeric.txt")	

# compare using short text
shorttext= "thequickbrownfoxjumpsoverthelazydog"
print "Short Text: " + shorttext
compareAlgorithms(shorttext)

# compare using longer text, song lyrics from Justin Bieber's "Sorry"
text = open("songlyrics.txt").read()
longertext = re.sub('[^a-zA-Z\'.]', '', text)
print "Longer Text: " + longertext
compareAlgorithms(longertext)

# compare using nonsensical text
nonsensicaltext = "willIfinishthisproblemsetintimeforvanillawhataresomewordsthatmightnotworkoutchocolatedon't"
print "Nonsensical Text: " + nonsensicaltext
compareAlgorithms(nonsensicaltext)

