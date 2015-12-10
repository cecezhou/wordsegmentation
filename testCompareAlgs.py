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
# process basetexts 
(freq_dict, normFactor) = helpers.getFreq("alphanumeric.txt")
(transition_freq_dict, transNormFactor) = helpers.getTransitionFreq("alphanumeric.txt")	

print "Short Text: "

shorttext= "thequickbrownfoxjumpsoverthelazydog"
print shorttext
compareAlgorithms(shorttext)

print "Longer Text: "

text = open("songlyrics.txt").read()
longertext = re.sub('[^a-zA-Z\'.]', '', text)
print longertext
compareAlgorithms(longertext)

print "Nonsensical Text: "

nonsensicaltext = "willIfinishthisproblemsetintimeforvanillawhataresomewordsthatmightnotworkoutchocolatedon't"
print nonsensicaltext
compareAlgorithms(nonsensicaltext)

