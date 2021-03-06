import models
import re
import enchant
import helpers
import time

# Use "A Farewell to Arms" to see how we do on the same text as we use
# to find individual word frequencies and transition frequencies.

# start timing
start_time = time.time()

basetext = "farewell_to_arms.txt"
text = open(basetext).read()

# to set alphanumeric
helpers.parseBaseText()
print "Segmenting Text..."

# remove excess line breaks and all punctuation except periods
cleantext = re.sub('[^a-zA-Z\n\'.]', ' ', text)
# write to file (for testing purposes)
open('farewell_clean.txt', 'w').write(cleantext)

# parse excerpt into list of sentences
# sentences holds the correct sentences that we will then 
# compare the output of our algorithm with
# ignore the length 0 string after the last period
sentences = cleantext.split('.')[:-1]

# remove spaces from excerpt
nospaces = re.sub('[^a-zA-Z\'.]', '', text)
# write to file (for testing purposes)
open('farewell_nospaces.txt', 'w').write(nospaces)
# ignore the length 0 string after the last period
nospace_sentences = nospaces.split('.')[:-1]

# tally up sentences that are correct
tallyNaiveProb = 0
tallyTransProb = 0

# get frequencies from basetext
(freq_dict, normFactor) = helpers.getFreq("alphanumeric.txt")
(transition_freq_dict, transNormFactor) = helpers.getTransitionFreq("alphanumeric.txt")

# iterate over sentences
for (idx, sentence) in enumerate(nospace_sentences):
	# default max word length as 15 
	if len(sentence) == 0:
		continue
	mytext = models.NoSpaceText(sentence, 15)
	# set frequency dictionaries
	mytext.freq_dict = freq_dict
	mytext.normFactor = normFactor
	mytext.transition_freq_dict = transition_freq_dict
	mytext.transNormFactor = transNormFactor

	# find segmentation using naive frequencies
	mytext.dpGreedy()
	bestSeg = mytext.getBestSeg()
	if helpers.compare(bestSeg, sentences[idx]):
		tallyNaiveProb += 1

	# find segmentation using transition frequencies
	mytext.dpGreedy(transFreq = True)
	bestSeg = mytext.getBestSeg()
	if helpers.compare(bestSeg, sentences[idx]):
		tallyTransProb += 1

# print results
print "Using Naive Frequencies:"
print float(tallyNaiveProb)/(len(sentences))
print "Using Transition Frequencies:"
print float(tallyTransProb)/(len(sentences))

# print total time
print("--- %s total seconds ---\n" % (time.time() - start_time))



