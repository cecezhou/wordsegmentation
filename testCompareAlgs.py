import time
import re
import helpers
import models

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


shorttext= "thequickbrownfoxjumpsoverthelazydog"
print "Short Text: " + shorttext
compareAlgorithms(shorttext)


text = open("songlyrics.txt").read()
longertext = re.sub('[^a-zA-Z\'.]', '', text)
print "Longer Text: " + longertext
compareAlgorithms(longertext)


nonsensicaltext = "willIfinishthisproblemsetintimeforvanillawhataresomewordsthatmightnotworkoutchocolatedon't"
print "Nonsensical Text: " + nonsensicaltext
compareAlgorithms(nonsensicaltext)

